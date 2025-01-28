'''
The code in this streamlit provides a way to add multiple simulation control
to the simulation model.
'''
import streamlit as st
import pandas as pd

from callcentresim.model import Experiment, run_all_experiments
from callcentresim.output_analysis import create_example_csv, experiment_summary_frame

from app_utility.file_io import read_file_contents


INFO_1 = '**Execute multiple experiments in a batch**'
INFO_2 = '### Upload a CSV containing input parameters.'

def create_experiments(df_experiments):
    '''
    Returns dictionary of Experiment objects based on contents of a dataframe

    Params:
    ------
    df_experiments: pandas.DataFrame
        Dataframe of experiments. First two columns are id, name followed by 
        variable names.  No fixed width

    Returns:
    --------
    dict
    '''
    experiments = {}
    
    # experiment input parameter dictionary
    exp_dict = df_experiments[df_experiments.columns[1:]].T.to_dict()
    # names of experiments
    exp_names = df_experiments[df_experiments.columns[0]].T.to_list()
    
    print(exp_dict)
    print(exp_names)

    # loop through params and create Experiment objects.
    for name, params in zip(exp_names, exp_dict.values()):
        print(name)
        experiments[name] = Experiment(**params)
    
    return experiments

# We add in a title for our web app's page
st.title("Urgent care call centre")

# show the introductory markdown
st.markdown(INFO_1)

#download_file = st.download_button()

with st.expander("Template to use for experiments"):
    st.markdown(read_file_contents("resources/batch_upload_txt.md"))
    template = create_example_csv()
    st.dataframe(template, hide_index=True)


st.markdown(INFO_2)
uploaded_file = st.file_uploader("Choose a file")
df_results = pd.DataFrame()
if uploaded_file is not None:
    # assumes CSV
    df_experiments = pd.read_csv(uploaded_file)
    st.write('**Loaded Experiments**')
    st.table(df_experiments)

    # loop through scenarios, create and run model
    n_reps = st.slider('Replications', 3, 30, 5, step=1)
    # warm-up and data collection parameters
    warm_up_period = st.number_input("Warm-up period", 0, 1_000, step=1)

    results_collection_period = st.number_input(
        "Data collection period", 1_000, 10_000, step=1
    )

    if st.button('Execute Experiments'):
        # create the batch of experiments based on upload
        experiments = create_experiments(df_experiments) 
        print(experiments)
        with st.spinner('Running all experiments'):
            
            results = run_all_experiments(
                experiments, 
                warm_up_period,
                results_collection_period,
                n_reps
            )
            st.success('Done!')
            
            # combine results into a single summary table.
            df_results = experiment_summary_frame(results)
            print(df_results.round(2))
            # display in the app via table
            st.dataframe(df_results.round(2))

