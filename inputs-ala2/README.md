DISCLAIMER: gromacs 2020 officially does not support simulations in vacuum, see [here](https://manual.gromacs.org/2020/release-notes/2020/major/removed-functionality.html).

The idea is to run short unbiased simulations in the basins, `unbiased-s[AB]`, and from these trajectories (.xtc) take several configuration files (.gro) that are then used to create new input files (.tpr) based on the ala2 topology (.top) and with the same MD parameters (.mdp)


**useful commands:**

gmx_mpi grompp -f md.mdp -p topol.top -c config.gro -o input.tpr

gmx_mpi trjconv -f unbiased-sA/alanine.xtc -s input.tpr -skip 300 -sep -o unbiased-sA/alanine..gro <<< "0"

for i in {0..3};do gmx_mpi grompp -f md.mdp -p topol.top -c unbiased-sA/alanine.$i.gro -o input.$i.tpr; done
