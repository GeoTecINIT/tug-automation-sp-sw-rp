# Reproducible Package for _"Implementing and evaluating the Timed Up and Go test automation using smartphones and smartwatches"_

[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/GeoTecINIT/tug-automation-sp-sw-rp/)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GeoTecINIT/tug-automation-sp-sw-rp/HEAD)
[![Paper DOI](https://img.shields.io/badge/Paper%20DOI-10.1109%2FJBHI.2024.3456169-yellow.svg)](https://doi.org/10.1109/JBHI.2024.3456169)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7991797.svg)](https://doi.org/10.5281/zenodo.7991797)


This repository is the reproducibility package for the _“Implementing and evaluating the Timed Up and Go test automation using smartphones and smartwatches"_ journal paper, published in the _IEEE Journal of Biomedical and Health Informatics_. 

> M. Matey-Sanz, A. González-Pérez, S. Casteleyn and C. Granell, "Implementing and evaluating the Timed Up and Go test automation using smartphones and smartwatches", 
> in _IEEE Journal of Biomedical and Health Informatics_, doi: 10.1109/JBHI.2024.3456169.

## Reproducibility

### Reproduce online
Click the on the "Binder" badge above to open an interactive Jupyter environment with all required software installed.


### Reproduce locally
Install Python 3.8, download the repository, open a command line in the root of the directory and install the required software by executing:

```bash
pip install -r requirements.txt
```

### Reproduce locally with Docker
Install [Docker](https://www.docker.com) for building an image based on a `Dockerfile` with a Jupyter environment and running a container based on the image.

Download the repository, open a command line in the root of the directory and:

1. Build the image:

```bash
docker build . --tag tug-automation-sp-sw-rp
```

2. Run the image:

```bash
docker run -it -p 8888:8888 tug-automation-sp-sw-rp
```

3. Click on the login link (or copy and paste in the browser) shown in the console to access to a Jupyter environment.

### Reproduce the analysis
Open the desired Jupyter Notebook (*.ipynb) file. Each notebook contains the used code and its outputs. You can execute
the code to reproduce the obtained results.

> [!NOTE] 
> When executing an analysis with a component of randomness (i.e., ML models training), the obtained results could be slightly different
than the reported ones. Notwithstanding, the conclusions should be similar as the reported ones.


## Repository structure

Common files:
- [`Dockerfile`](./Dockerfile): a recipe for the computational environment using Docker.
- [`requirements.txt`](./requirements.txt): file with the dependencies and versions used through all the code.

Notebooks and code files:

- [`functions`](functions/): Pythons scripts defining common functions used in the notebooks.
- [`01_sensor-data-processing.ipynb`](./01_sensor-data-processing.ipynb): Jupyter Notebook containing all the code used for data processing. It obtains the data from [`01_SENSOR-DATA/01_RAW`](./01_SENSOR-DATA/01_RAW) and process it to clean it (stored at [`01_SENSOR-DATA/02_CLEAN`](./01_SENSOR-DATA/02_CLEAN)) and arange it as windows (stored at [`01_SENSOR-DATA/03_WINDOWED`](./01_SENSOR-DATA/03_WINDOWED)).
- [`02_ml.ipynb`](./02_ml.ipynb): Jupyter Notebook containing all the code used for training the ML models. It loads the data from [`01_SENSOR-DATA/03_WINDOWED`](./01_SENSOR-DATA/03_WINDOWED) and uses it to compare the two activities splitting methods and to train the ML models used by the application. The models are stored in [`02_ML`](./02_ML).

> [!WARNING]
> Retraining the models might take a while. The outcomes of the contained analyses can be reproduced by loading the results in `02_ML/01_splitting-approaches-reports.json`.

- [`03_experiment.ipynb`](./03_experiment.ipynb): Jupyter Notebook containing all the analysis performed. It loads the application and manual results from [`03_EXPERIMENT/01_INPUT`](./03_EXPERIMENT/01_INPUT) to analyse the reliability of the system. The output of the analysis is stored in [`03_EXPERIMENT/02_OUTPUT`](./03_EXPERIMENT/02_OUTPUT).
- [`04_battery-consumption`](./battery-consumption.ipynb): Jupyter Notebook containing the battery consumption analysis. It loads the battery consumption records from [`04_BATTERY/00_battery-historian.csv`](./04_BATTERY/00_battery-historian.csv) to compute the consumption estimates per device and TUG execution, which are stored in [`04_BATTERY/01_battery-consumption.csv`](./04_BATTERY/01_battery-consumption.csv) 

Directories and data files:

- [`01_SENSOR-DATA`](./01_SENSOR-DATA):
  - [`01_RAW`](./01_SENSOR-DATA/01_RAW): contains a raw accelerometer and gyroscope data collected from the participants of the study while they were performing the TUG test.
    - `sXX`: directory containing the raw data obtained from the subject XX. Each directory contains a `json` file for each
    TUG execution and for each device. Files have the following naming convention: `{subject_id}_{execution}_{sw|sp}.json`. It also contains the file `sXX_segments.txt`, which contains the boundaries between each TUG subphase, manually extracted from video analysis.
    - [`subjects.csv`](./01_SENSOR-DATA/01_RAW/subjects.csv): information (e.g., age, gender) regarding the participants of the study.
  - [`02_CLEAN`](./01_SENSOR-DATA/02_CLEAN): contains the processed accelerometer and gyroscope data, where each sample is labelled with an associated activity.
    - [`01_TURNING-AND-SITTING`](./01_SENSOR-DATA/02_CLEAN/01_TURNING-AND-SITTING): the samples are labelled with the SEATED, STANDING_UP, WALKING, TURNING and SITTING_DOWN activities. Contains a directory for each subject, and each directory has a `csv` file with the labeled data corresponding to one execution. The `csv` files follow this format: `{subject_id}_{execution}_{sw|sp}.csv`
    - [`02_TURN-TO-SIT`](./01_SENSOR-DATA/02_CLEAN/02_TURN-TO-SIT): the samples are labelled with the SEATED, STANDING_UP, WALKING, TURNING and TURN-TO-SIT activities. Contains a directory for each subject, and each directory has a `csv` file with the labeled data 
    corresponding to one execution. The `csv` files follow this format: `{subject_id}_{execution}_{sw|sp}.csv`
    - `01_sp_{acc|gyro}-boundaries.pdf`: plots containing accelerometer and gyroscope data and their associated activties. These plots correspond to the **Figure 5** of the paper.
  - [`03_WINDOWED`](./01_SENSOR-DATA/03_WINDOWED): contains the windows generated from the clean data.
    - [`01_TURNING-AND-SITTING`](./01_SENSOR-DATA/03_WINDOWED/01_TURNING-AND-SITTING): the windows are labelled with the SEATED, STANDING_UP, WALKING, TURNING and SITTING_DOWN activities. Contains a directory for each subject.
    - [`02_TURN-TO-SIT`](./01_SENSOR-DATA/03_WINDOWED/02_TURN-TO-SIT): the windows are labelled with the SEATED, STANDING_UP, WALKING, TURNING and TURN-TO-SIT activities. Contains a directory for each subject.
- [`02_ML`](./02_ML): contains the ML models trained with the collected data. Contains:
  - [`01_splitting-approaches-reports.json`](./02_ML/01_splitting-approaches-reports.json): results from models trained with both splitting approaches.
  - [`02_splitting-approaches-comparison.csv`](./02_ML/02_splitting-approaches-comparison.csv): comparison analysing the results of both splitting approaches. This information is reported in the **Table II** of the paper.
  - `03_sp_data_model.tflite`: CNN model trained with the data collected from the smartphone's sensors.
  - `03_sw_data_model.tflite`: CNN model trained with the data collected from the smartwatch's sensors.
  - `03_labels.txt`: activity labels file embedded into models as metadata.
- [`03_EXPERIMENT`](./03_EXPERIMENT): contains the input and the output of the analysis performed about the results of the systems.
  - [`01_INPUT`](./03_EXPERIMENT/01_INPUT): directory with the inputs of the experiment (i.e., results obtained from the TUG system)
    - `sXX`: directory containing the experiments results of the subject XX. Each directory contains:
      - `sXX_{sp|sw}.json`: results obtained from the sw and the sp device.
      - `sXX_results.csv`: results obtained manually from visual inspection.
  - [`02_OUTPUT`](./03_EXPERIMENT/02_OUTPUT): directory with the results of the analyses.
    - `01_{c1|c2|man}-results.csv`: TUG executions measurements from the system and the manual ones.
    - [`02_errors.csv`](./03_EXPERIMENT/02_OUTPUT/02_errors.csv): measurement error of each TUG execution and subphases.
    - [`03_execution-status.csv`](./03_EXPERIMENT/02_OUTPUT/03_execution-status.csv): number of executions classified as _success_, _partial_success_ and _failure_. This information is reported in the **Table III** of the paper.
    - [`04_error-distribution.pdf`](./03_EXPERIMENT/02_OUTPUT/04_error-distribution.pdf): boxplot with the distribution of the measurement errors. This plot corresponds to the **Figure 6** of the paper.
    - [`05_subjects-rmse.csv`](./03_EXPERIMENT/02_OUTPUT/05_subjects-rmse.csv): intra-subject measurements RMSE.
    - [`05_comparison-rmse.csv`](./03_EXPERIMENT/02_OUTPUT/05_comparison-rmse.csv): inter-subject measurements RMSE. This information is reported in the **Table IV** of the paper.
    - `06_{c1|c2}-duration-ba.pdf`: Bland-Altman plots of the total duration of the executions. These plots correspond to the **Figure 7** of the paper.
    - `07_{c1|c2}-phases-ba.pdf`: Bland-Altman plots of the subphases duration of the executions. These plots correspond to the **Figure 8** of the paper.
    - [`08_icc-results.csv`](./03_EXPERIMENT/02_OUTPUT/08_icc-results.csv): ICC<sub>(2,1)</sub> reliability metric comparing each system configuration with the manual results. This information is reported in the **Table V** of the paper.
- [`04_BATTERY`](./04_BATTERY): contains the system's battery consumption information. Contains:
  - [`bug-reports`](./04_BATTERY/bug_reports): `bugreports` generated after the execution of the TUG system on the devices. The `bugreports` have the following naming 
  format: `br_{sXX[-sYY]}_{sp|sp-paired|sw}`.
  - [`00_battery-historian.csv`](./04_BATTERY/00_battery-historian.csv): battery consumption data extracted from the `bugreports`.
  - [`01_battery-consumption.csv`](./04_BATTERY/01_battery-consumption.csv): battery consumption information processed from the Battery Historian data. This information is reported in the **Table VII** of the paper.
    

## License
The documents in this repository are licensed under [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

All contained code is licensed under the [Apache License 2.0](./LICENSE).

All data used in this repository is licensed under [Open Data Commons Attribution License](http://opendatacommons.org/licenses/by/1.0/).


## Acknowledgements

This work has been funded by the Spanish Ministry of Universities [grants FPU19/05352 and FPU17/03832] and by the Spanish Ministry of Science and Innovation (MCIN/AEI/10.13039/501100011033) and ''ERDF A way of making Europe'' [grants PID2020-120250RB-I00, PID2022-1404475OB-C21 and PID2022-140475OB-C22]. 