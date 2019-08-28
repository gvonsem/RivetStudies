#!/bin/zsh

for i in `ls crab_projects/|grep Rivet`; do
  echo $i
  crab status -d crab_projects/$i
  #crab resubmit -d crab_projects/$i  --maxjobruntime 1800 --maxmemory 2500
  crab resubmit -d crab_projects/$i
done
