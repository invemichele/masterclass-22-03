# PLUMED Masterclass-22-03: OPES method
Repository of the data for [PLUMED Masterclass 22.3](https://plumed-school.github.io/lessons/22/003/data/NAVIGATION.html) (see also [here](https://www.plumed.org/masterclass)).

The slides of the masterclass can be found at [this link](https://docs.google.com/presentation/d/1G94Kjq3kn3sNxFi2fZoISG3OMNq_erGIgleyr8y2YEA).
The video recording is also available for both the [lecture](https://youtu.be/1XYGfA4kJ1c) and the [tutorial correction](https://youtu.be/Rn5JgItgKX4).

The `notebooks` directory contains two Jupyter notebooks with all the instructions of the tutorials.

## installation
For a quick start use conda (or mamba):
```
# install some basic analysis tool and the default plumed version
conda install -c conda-forge plumed py-plumed numpy pandas matplotlib notebook mdtraj mdanalysis git

# install plumed 2.8.0 and gromacs 2020.6 with MPI and all modules enabled
conda install --strict-channel-priority -c plumed/label/masterclass-2022 -c conda-forge plumed gromacs
```
For better performance see instructions for compiling [plumed](https://www.plumed.org/doc-v2.8/user-doc/html/_installation.html) and [gromacs](https://manual.gromacs.org/documentation/2020/install-guide/index.html).
