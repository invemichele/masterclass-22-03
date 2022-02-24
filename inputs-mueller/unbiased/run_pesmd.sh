#!/bin/bash

### compulsory ###
ncore=1
outfile=log.plumed

### optional ###
extra_cmd="rm stats.out"

### commands ###
mpi_cmd="plumed pesmd input_md.dat |grep PLUMED"
submit="time mpirun -np $ncore ${mpi_cmd}"

### execute ###
bck.meup.sh -i $outfile
echo -e "\n$submit &>> $outfile"
eval "$submit &>> $outfile"
[ -z "$extra_cmd" ] || eval $extra_cmd

