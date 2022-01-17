# SampleGeneration

## Setup
```
export SCRAM_ARCH=slc7_amd64_gcc900
cmsrel CMSSW_11_2_1_Patatrack
cd CMSSW_11_2_1_Patatrack/src
git clone git@github.com:alintulu/SampleGeneration.git
scram b
```

#### GEN
```
cmsDriver.py \
    SampleGeneration/GenFragments/python/HWminusJ_HanythingJ_NNPDF31_13TeV_M125_Vhadronic.py \
    --python_filename SampleGeneration/Analysis/config/HWminusJ_HanythingJ_NNPDF31_13TeV_M125_Vhadronic.py \
    --eventcontent GENRAW \
    --datatier GEN \
    --fileout file:hwminus.root \
    --conditions 112X_mcRun3_2021_realistic_v16 \
    --step LHE,GEN \
    --geometry DB:Extended \
    --era Run3 \
    --no_exec \
    --mc \
    -n 10
```

#### NanoGEN
```
cmsDriver.py \
    SampleGeneration/GenFragments/python/HWminusJ_HanythingJ_NNPDF31_13TeV_M125_Vhadronic.py \
    --python_filename SampleGeneration/Analysis/config/HWminusJ_HanythingJ_NNPDF31_13TeV_M125_Vhadronic.py \
    --eventcontent NANOAODGEN \
    --datatier NANOAOD \
    --fileout file:hwminus-nanogen.root \
    --conditions 112X_mcRun3_2021_realistic_v16 \
    --step LHE,GEN,NANOGEN \
    --geometry DB:Extended \
    --era Run3 \
    --no_exec \
    --mc \
    -n 10
```
