# RivetStudies

Code to run [Rivet](https://twiki.cern.ch/twiki/bin/viewauth/CMS/Rivet) on GEN or MiniAOD samples. 
The following instructions were tested on lxplus.

## Installation

```
cmsrel CMSSW_10_6_0
cd CMSSW_10_6_0/src
cmsenv
git-cms-init
git-cms-addpkg GeneratorInterface/RivetInterface
git-cms-addpkg Configuration/Generator
git clone https://gitlab.cern.ch/cms-gen/Rivet.git
source Rivet/rivetSetup.sh
scram b -j 8
git clone https://github.com/gvonsem/RivetStudies.git
```

## Running Rivet on MiniAOD via crab
```
cd RivetStudies/RivetAnalysis/crab

source /cvmfs/cms.cern.ch/crab3/crab.sh
voms-proxy-init -voms cms
```
Adapt submitCrab_Rivet.sh for the desired use case and submit jobs
```
./submitCrab_Rivet.sh
```

## Merge Rivet output and make plots

```
cd CMSSW_10_6_0/src
source Rivet/rivetSetup.sh
cd RivetStudies/RivetAnalysis
mkdir plots; cd plots
```
Merge the yoda files if needed. Note: there are limitations to the [yodamerge](https://github.com/alisw/yoda/blob/master/bin/yodamerge) functionality; please check if they are applicable.
```
yodamerge <path_to_yoda_files>/*.yoda -o output_merged.yoda
```
Make actual plots:
```
rivet-mkhtml output_merged.yoda:"Legend title":'LineColor=red' --mc-errs
```
