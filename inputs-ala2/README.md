DISCLAIMER: gromacs 2020 officially does not support simulations in vacuum, see [here](https://manual.gromacs.org/2020/release-notes/2020/major/removed-functionality.html).

**useful commands:**

#generate a .tpr file from the configuration in a .gro file, using the options in the .mdp file
gmx_mpi grompp -f md.mdp -p topol.top -c config.gro -o input.tpr

#generate various .gro files from an .xtc trajectory
gmx_mpi trjconv -f unbiased-sA/alanine.xtc -s input.tpr -skip 300 -sep -o unbiased-sA/alanine..gro <<< "0"

#generate several .tpr files, as above
for i in {0..3};do gmx_mpi grompp -f md.mdp -p topol.top -c unbiased-sA/alanine.$i.gro -o input.$i.tpr; done
