# SampleGeneration

## Setup
```
cmsrel CMSSW_12_4_6
cd CMSSW_12_4_6/src
git clone git@github.com:alintulu/SampleGeneration.git -b particlenet
scram b
```

## cmsDriver commands

You can find more examples (e.g. how to create miniaod) in [GenFragments/run](GenFragments/run).

### GEN to RAWMINIAOD

#### GEN -> SIM -> DIGI -> RAW (with pileup)

```
cmsDriver.py \
    SampleGeneration/GenFragments/python/fragment.py \
    --python_filename SampleGeneration/Analysis/config/gen2pu.py \
    --eventcontent RAWSIM \
    --datatier GEN-SIM-DIGI-RAW \
    --pileup 2022_LHC_Simulation_10h_2h \
    --fileout file:gen2pu.root \
    --pileup_input "dbs:/MinBias_TuneCP5_13p6TeV-pythia8/Run3Summer22GS-124X_mcRun3_2022_realistic_v10-v1/GEN-SIM" \
    --conditions auto:phase1_2022_realistic \
    --step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:@relval2022 \
    --geometry DB:Extended \
    --era Run3 \
    --no_exec \
    --mc \
    --customise_command "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)" \
    -n 10
```

#### RAW -> RAWMINIAOD

```
cmsDriver.py \
    step2 \
    --python_filename SampleGeneration/Analysis/config/pu2rawminiaod.py \
    --datatier MINIAODSIM \
    --eventcontent RAWMINIAODSIM \
    --filein file:gen2pu.root \
    --conditions auto:phase1_2022_realistic \
    --step RAW2DIGI,L1Reco,RECO,RECOSIM,PAT \
    --geometry DB:Extended \
    --fileout file:pu2rawminiaod.root \
    --era Run3 \
    --no_exec \
    --mc \
    -n 10
```

### GEN
```
cmsDriver.py \
    SampleGeneration/GenFragments/python/fragment.py \
    --python_filename SampleGeneration/Analysis/config/gen.py \
    --eventcontent GENRAW \
    --datatier GEN \
    --fileout file:gen.root \
    --conditions auto:phase1_2022_realistic \
    --step LHE,GEN \
    --geometry DB:Extended \
    --era Run3 \
    --no_exec \
    --mc \
    -n 10
```

### NanoGEN
```
cmsDriver.py \
    SampleGeneration/GenFragments/python/fragment.py \
    --python_filename SampleGeneration/Analysis/config/nanogen.py \
    --eventcontent NANOAODGEN \
    --datatier NANOAOD \
    --fileout file:nanogen.root \
    --conditions auto:phase1_2022_realistic \
    --step LHE,GEN,NANOGEN \
    --geometry DB:Extended \
    --era Run3 \
    --no_exec \
    --mc \
    -n 10
```

## How to use this repository

1. [Setup directory](#setup)
2. Add your fragment to [GenFragments/python](GenFragments/python)
3. Use one of the cmsDriver.py commands above to create a python configuration file. Make sure to change the first line after `cmsDriver.py` to point to your fragment
4. Create events
   1. Locally by running `cmsRun [python_filename]`
   2. With CRAB by going to [Analysis/run](Analysis/run). Change `config.JobType.psetName` to your python configuration file. Submit to crab with `crab submit -c [crab_file]`. Check status with `crab status`
