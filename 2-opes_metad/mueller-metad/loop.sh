#!/bin/bash

for i in {0..4}
do
  mkdir $i
  cd $i
  ../run_pesmd.i.sh $i &
  cd ..
done
