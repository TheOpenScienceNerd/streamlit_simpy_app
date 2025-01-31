# A streamlit app of a simpy urgent care call centre model.

The materials in this repo provide a simple example of converting and deploying an existing simulation model as `streamlit` web app.  

## License

The materials have been made available under an MIT license.  Please provide credit if you reuse the code in your own work.

## Installation instructions

### Installing dependencies

All dependencies can be found in [`environment.yml`]() and are pulled from conda-forge.  To run the code locally, we recommend installing [miniforge](https://github.com/conda-forge/miniforge);

> miniforge is Free and Open Source Software (FOSS) alternative to Anaconda and miniconda that uses conda-forge as the default channel for packages. It installs both conda and mamba (a drop in replacement for conda) package managers.  We recommend mamba for faster resolving of dependencies and installation of packages. 

navigating your terminal (or cmd prompt) to the directory containing the repo and issuing the following command:

```bash
mamba env create -f environment.yml
```

Activate the mamba environment using the following command:

```bash
mamba activate simpy_app
```

Run the app

```bash
streamlit run Overview.py
```

## Repo overview

```
.
├── binder
│   └── environment.yml
├── CHANGELOG.md
├── CITATION.cff
├── LICENSE
├── app_utility
│   ├── __init__.py
│   ├── file_io.py
│   └── results.py
├── callcentresim
│   ├── __init__.py
│   ├── model.py
│   └── output_analysis.py
├── pages
│   ├── 1_🎱_Interactive_Simulation.py
│   ├── 2_🧪_Batch_Experiment_Runner.py
│   ├── 3_⚖️_License.py
│   └── 4_ℹ️_About.py
├── resources
│   └── ...
├── main.py
├── Overview.py
├── README.md
└── requirements.txt
```

* `environment.yml` - contains the conda environment if you wish to work locally with the app code.
* `app_utility` - local python package of code that can be used across multiple web apps.
* `callcentresim` - local python package containing the urgent care call centre SimPy model.
* `pages` - all `streamlit` app pages
* `resources` - markdown and images for app
* `CHANGES.md` - changelog with record of notable changes to project between versions.
* `CITATION.cff` - citation information for the package.
* `LICENSE` - details of the MIT permissive license of this work.
* `requirements.txt` - pip file for streamlit install (although streamlit will use `environment.yml` as the priority.).

