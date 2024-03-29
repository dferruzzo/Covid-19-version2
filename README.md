# SIRSi-Vaccine Dynamical Model for the Covid-19 Pandemic repository

Welcome to the SIRSi-Vaccine Dynamical Model for the Covid-19 Pandemic repository, which is publicly available for reproducibility and dissemination purposes as part of the manuscript under review.

To use this repository, please follow the instructions below:

1. Clone or download the repository to your local machine.
2. Install the required dependencies as specified in the `requirements.txt` file.
3. Run the jupyter notebook file `main.ipynb` to reproduce the figures presented in the manuscript.
4. Feel free to modify the parameters in the notebook file to generate different scenarios and compare the results.
If you have any questions, please do not hesitate to contact the repository owner.

Thank you for your interest in our work!

## Description
In this repository are the databases corresponding to the reported confirmed cases of Covid-19 and the data on Social Distancing according to the official website of SEADE. This repository also contains the programs written in python that process the raw data, prepare it, perform the least squares fit, perform model prediction validation, and produce the figures.

The files that are part of the program include the functions:

* `mostrar_dados`, presents in a user-friendly way the data of confirmed cases and isolation rate used for processing.
* `loaddata`, loads the data corresponding to the chosen time window.
* `fit_isol`, produces the least squares fit for the isolation index.
* `fitting`, produces the least squares adjustment for data from confirmed cases of Covid-19.
* `validation`,performs a validation of the predictions generated by the model with adjusted parameters taking data in a later time window than the data used for the adjustment.
* `save_all`, saves tuning parameters and other statistical data in csv files for later use.
* `load_all`, loads the information previously saved in csv format for use.
* `gerar_figs_param`, generates most of the figures used in the article. Not all figures produced are used in the article.
* `simulations`, produces simulations and figures and allows changing parameters such as the vaccination rate 
 and the isolation index. It is used to simulate different scenarios as proposed in the article.
mapa1, produces a transcritical bifurcation map in parameter spaces that shows the trade-off of stability between disease-free and endemic equilibria, as well as the contours of peak peaks of infected associates.

## Functionality
This notebook can be run directly in a `Codespace` here on `Github`.

Run this notebook to:

* Load de data from the Covid-19 reported confirmed cases,
* Load the Isolation index data,
* Produce parameter adjustment for both the isolation data and the model paramters,
* Save the data produced in files for distribution and reproducibility,
* Produce the plots,
* For testing different scenarios.
