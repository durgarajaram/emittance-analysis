
CR emittance analysis

Quick start
===========

The basic execution of the analysis is done by a command like:

python scripts/bin/run_one_analysis.py scripts/config/config_reco.py 0
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^
       main program                    configuration file            specify which data set in
                                                                     the config file to analyse

The config file defines all of the run control variables, file locations, cut
parameters etc. It is possible to run several analyses in parallel by doing

python scripts/bin/run_many_analyses.py

Edit the "run_many_analyses.py" script to control which analyses to run. 

I often show tableaux of several plots from different analyses in a single 
canvas. This is done using the script

python scripts/bin/conglomerate_plots.py

Data cards are in the scripts/config subdir

Data-handling and loading via scripts/data_loader

Amplitude, kNN, fractional emittance analysis scripts are in scripts/mice-analysis subdir

Some stat utils and helpers in scripts/utilities subdir


Requires
=====
MAUS, ROOT

