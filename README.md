# SampleGeneration

## Setup
```
export SCRAM_ARCH=slc7_amd64_gcc900
cmsrel CMSSW_11_2_1_Patatrack
cd CMSSW_11_2_1_Patatrack/src
git clone https://github.com/CMSALPS/SampleGeneration.git
scram b
```

### no premix

[example](https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_test/PPD-Run3Winter21DRMiniAOD-00006)

```
cmsDriver.py \
    SampleGeneration/GenFragments/python/QCD_Pt-15to7000_TuneCUETP8M1_Flat_14TeV-pythia8_cfg.py \
    --python_filename gen2pu_cfg.py \
    --eventcontent RAWSIM \
    --pileup Run3_Flat55To75_PoissonOOTPU \
    --customise HLTrigger/Configuration/customizeHLTforPatatrack.customizeHLTforPatatrackTriplets \
    --fileout file:QCD_pu.root \
    --pileup_input "dbs:/MinBias_TuneCP5_14TeV-pythia8/Run3Winter21GS-112X_mcRun3_2021_realistic_v15-v1/GEN-SIM" \
    --conditions 112X_mcRun3_2021_realistic_v16 \
    --step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:GRun \
    --geometry DB:Extended \
    --era Run3 \
    --no_exec \
    --mc \
    -n 10
```

```
cmsDriver.py \
    step2 \
    --python_filename pu2rawminiaod.py \
    --eventcontent RAWMINIAODSIM \
    --filein file:QCD_pu.root \
    --conditions 112X_mcRun3_2021_realistic_v16 \
    --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI,PAT \
    --geometry DB:Extended \
    --fileout file:QCD_rawminiaod.root \
    --era Run3 \
    --no_exec \
    --mc \
    -n 10
```

### Premix

[example](https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/PPD-RunIISummer17PrePremix-00020)

```
cmsDriver.py \
    SampleGeneration/GenFragments/python/Neutrino_E-10_gun_cfg.py \
    --python_filename premix_cfg.py \
    --eventcontent PREMIX \
    --pileup Run3_Flat55To75_PoissonOOTPU \
    --fileout file:Neutrino_E-10_gun_premix.root \
    --pileup_input "dbs:/MinBias_TuneCP5_14TeV-pythia8/Run3Winter21GS-112X_mcRun3_2021_realistic_v15-v1/GEN-SIM" \
    --conditions 112X_mcRun3_2021_realistic_v16 \
    --step GEN,SIM,DIGI,L1,DIGI2RAW \
    --procModifiers premix_stage1 \
    --era Run3 \
    --no_exec \
    --mc \
    -n 10
```

### use premix

```
cmsDriver.py \
    SampleGeneration/GenFragments/python/QCD_Pt-15to7000_TuneCUETP8M1_Flat_14TeV-pythia8_cfg.py \
    --python_filename gen2pu_premix_cfg.py \
    --eventcontent PREMIXRAW \
    --customise HLTrigger/Configuration/customizeHLTforPatatrack.customizeHLTforPatatrackTriplets \
    --fileout file:QCD_pu.root \
    --pileup_input file:Neutrino_E-10_gun_premix.root \
    --procModifiers premix_stage2 \
    --datamix PreMix \
    --conditions 112X_mcRun3_2021_realistic_v16 \
    --step GEN,SIM,DIGI,DATAMIX,L1,DIGI2RAW,HLT:GRun \
    --geometry DB:Extended \
    --era Run3 \
    --no_exec \
    --mc \
    -n 10
```

