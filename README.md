# SampleGeneration

## Setup
```
export SCRAM_ARCH=slc7_amd64_gcc900
cmsrel CMSSW_11_2_1_Patatrack
cd CMSSW_11_2_1_Patatrack/src
git clone git@github.com:alintulu/SampleGeneration.git
scram b
```

## cmsDriver commands

You can find more examples (e.g. how to create miniaod) in [GenFragments/run](GenFragments/run).

### GEN
```
cmsDriver.py \
    SampleGeneration/GenFragments/python/HWminusJ_HanythingJ_NNPDF31_13TeV_M125_Vhadronic.py \
    --python_filename SampleGeneration/Analysis/config/HWminusJ_HanythingJ_NNPDF31_13TeV_M125_Vhadronic.py \
    --eventcontent GENRAW \
    --datatier GEN \
    --fileout file:hwminus.root \
    --conditions auto:phase1_2021_realistic \
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
    SampleGeneration/GenFragments/python/HWminusJ_HanythingJ_NNPDF31_13TeV_M125_Vhadronic.py \
    --python_filename SampleGeneration/Analysis/config/HWminusJ_HanythingJ_NNPDF31_13TeV_M125_Vhadronic.py \
    --eventcontent NANOAODGEN \
    --datatier NANOAOD \
    --fileout file:hwminus-nanogen.root \
    --conditions auto:phase1_2021_realistic \
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
