#useful commands
gmx_mpi grompp -f md.mdp -p topol.top -c config.gro -o input.tpr

gmx_mpi trjconv -f unbiased-sA/alanine.xtc -s input.tpr -skip 300 -sep -o unbiased-sA/alanine..gro <<< "0"

for i in {0..3};do gmx_mpi grompp -f md.mdp -p topol.top -c unbiased-sA/alanine.$i.gro -o input.$i.tpr; done
