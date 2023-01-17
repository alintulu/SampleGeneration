# How to test https://github.com/cms-sw/cmssw/pull/40438

## Setup

```
cmsrel CMSSW_13_0_0_pre2
cd CMSSW_13_0_0_pre2/src
cmsenv
git cms-init
git cms-addpkg CommonTools PhysicsTools RecoBTag
mkdir data
git remote add alintulu git@github.com:alintulu/cmssw.git
git fetch alintulu scoutingNanoAOD-13_0_0_pre2-prod
git checkout --track alintulu/scoutingNanoAOD-13_0_0_pre2-prod
scram b -j 8
```
## Run

```
wget https://raw.githubusercontent.com/alintulu/SampleGeneration/hbb2022/NanoAOD/scouting_NANOGEN.py
cmsRun scouting_NANOGEN.py
```


