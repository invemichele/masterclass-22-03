#!/bin/bash

if [ $# -eq 1 ]
then
  rep=$1
else
  echo "missing replica number"
  exit
fi

### compulsory ###
ncore=1
outfile=log.plumed

### optional ###
extra_cmd="rm stats.out"

### commands ###
mpi_cmd="plumed pesmd ../../../inputs-mueller/input_md.${rep}.dat |grep PLUMED"
submit="time mpirun -np $ncore ${mpi_cmd}"

### execute ###
bck.meup.sh -i $outfile
echo -e "\n$submit &>> $outfile"
eval "$submit &>> $outfile"
[ -z "$extra_cmd" ] || eval $extra_cmd

