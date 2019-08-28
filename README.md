# RivetStudies

Code to run Rivet on GEN or MiniAOD samples

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

```
cd RivetStudies
```
