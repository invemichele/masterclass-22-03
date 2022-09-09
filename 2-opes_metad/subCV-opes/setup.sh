#!/bin/bash

for i in {0..3}
do
  mkdir $i
  cp ../../inputs-ala2/input.$i.tpr $i/input.tpr || rmdir $i
done
