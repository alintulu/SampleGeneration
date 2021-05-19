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
    SampleGeneration/GenFragments/python/QCD_Pt15to7000_TuneCP5_14TeV-pythia8_cfg.py \
    --python_filename gen2pu_cfg.py \
    --eventcontent RAWSIM \
    --datatier GEN-SIM-DIGI-RAW \
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
    --datatier MINIAODSIM \
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

[pu profile (Flat 0-80)](https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/TSG-Run3Winter21DRMiniAOD-00079)
[example premix](https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/PPD-RunIISummer17PrePremix-00020)
[minbias sample][(https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/PPD-Run3Winter21GS-00001)

```
cmsDriver.py \
    SampleGeneration/GenFragments/python/Neutrino_E-10_gun_cfg.py \
    --python_filename premix_cfg.py \
    --eventcontent PREMIX \
    --datatier GEN-SIM-DIGI-RAW \
    --pileup Flat_10_50_25ns \
    --customise_commands "process.mix.input.nbPileupEvents.probFunctionVariable = cms.vint32(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80) \n process.mix.input.nbPileupEvents.probValue = cms.vdouble(0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679,0.012345679)" \
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

#### gen only
```
cmsDriver.py \
    SampleGeneration/GenFragments/python/QCD_Pt15to7000_TuneCP5_14TeV-pythia8_cfg.py \
    --python_filename QCD_Pt-15to7000_gen_cfg.py \
    --eventcontent GENRAW \
    --datatier GEN \
    --fileout file:scouting.root \
    --conditions 112X_mcRun3_2021_realistic_v16 \
    --step GEN \
    --geometry DB:Extended \
    --era Run3 \
    --no_exec \
    --mc \
    -n 10
```

#### gen-pu

```
cmsDriver.py \
    SampleGeneration/GenFragments/python/QCD_Pt15to7000_TuneCP5_14TeV-pythia8_cfg.py \
    --python_filename gen2pu_premix_cfg.py \
    --eventcontent PREMIXRAW \
    --datatier GEN-SIM-DIGI-RAW \
    --customise HLTrigger/Configuration/customizeHLTforPatatrack.customizeHLTforPatatrackTriplets \
    --fileout file:scouting.root \
    --pileup_input "dbs:/Neutrino_E-10_gun_14TeV_112X_mcRun3_Flat0To80/mkomm-ML_210512-b09a2eecd62342c3650c8a5512506094/USER,instance=prod/phys03" \
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


### for fragments with randomized parameter

Add the following to cmsDriver to increase the randomization at lumi section transitions
```
--customise_commands "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(100)"
```

and for consistency also set the same number of events per lumi section in the crab config file:
```
config.JobType.eventsPerLumi = 100
```



