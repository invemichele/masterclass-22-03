DISCLAIMER: gromacs 2020 officially does not support simulations in vacuum

**useful commands**

gmx_mpi grompp -f md.mdp -p topol.top -c config.gro -o input.tpr

gmx_mpi trjconv -f unbiased/alanine.xtc -s input.tpr -skip 300 -sep -o unbiased/alanine..gro <<< "0"

for i in {0..3};do gmx_mpi grompp -f md.mdp -p topol.top -c unbiased/alanine.$i.gro -o input.$i.tpr; done
