"""
The code in this streamlit script adds in a plotly 
chart to display a histogram of replications. The results shown in the 
histogram can be selected by the user.
"""

import streamlit as st

from callcentresim.model import Experiment, multiple_replications
from callcentresim.output_analysis import create_user_controlled_hist

from app_utility.file_io import read_file_contents
from app_utility.results import get_kpi_name_mappings

INTRO_FILE = "./resources/model_info.md"

#  update to wide page settings to help display results side by side
st.set_page_config(
    page_title="Urgent Care Sim App",
    layout="wide",
    initial_sidebar_state="expanded",
)

# We add in a title for our web app's page
st.title("Urgent care call centre")

# show the introductory markdown
st.markdown(read_file_contents(INTRO_FILE))

# side bar
with st.sidebar:

    # set number of resources
    n_operators = st.slider("Call operators", 1, 20, 13, step=1)
    n_nurses = st.slider("Nurses", 1, 15, 9, step=1)

    # inter-arrival time of calls
    mean_iat = st.slider("IAT", 0.1, 1.0, 0.6, step=0.05)

    # set chance of nurse
    chance_callback = st.slider(
        "Chance of nurse callback",
        0.1,
        1.0,
        0.4,
        step=0.05,
        help="Set the chance of a call back",
    )

    # warm-up and data collection parameters
    warm_up_period = st.number_input("Warm-up period", 0, 1_000, step=1)

    results_collection_period = st.number_input(
        "Data collection period", 1_000, 10_000, step=1
    )

    # set number of replications
    n_reps = st.number_input("No. of replications", 100, 1_000, step=1)

# create experiment
user_experiment = Experiment(
    n_operators=n_operators,
    n_nurses=n_nurses,
    mean_iat=mean_iat,
    chance_callback=chance_callback,
)

# A user must press a streamlit button to run the model
if st.button("Run simulation"):

    #  add a spinner and then display success box
    with st.spinner("Simulating the urgent care system..."):
        # run multiple replications of experment
        results = multiple_replications(user_experiment, n_reps=n_reps)

    st.success("Done!")

    col1, col2 = st.columns(2)
    with col1.expander("Tabular results", expanded=True):
        # show tabular results
        st.dataframe(results.describe().round(2).T)

    with col2.expander("Histogram", expanded=True):

        #  call updated plotly function
        fig = create_user_controlled_hist(
            results, 
            name_mappings=get_kpi_name_mappings()
        )

        st.plotly_chart(fig, use_container_width=True)
