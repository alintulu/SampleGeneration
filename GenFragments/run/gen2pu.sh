#!/bin/bash

cmsDriver.py \
   SampleGeneration/GenFragments/python/HWminusJ_HToGammaGamma.py \
   --python_filename SampleGeneration/Analysis/config/gen2pu_cfg.py \
   --eventcontent RAWSIM,LHE \
   --datatier LHE,GEN-SIM-DIGI-RAW \
   --pileup Run3_Flat55To75_PoissonOOTPU \
   --customise HLTrigger/Configuration/customizeHLTforPatatrack.customizeHLTforPatatrackTriplets \
   --fileout file:htogammagamma_pu.root \
   --pileup_input "dbs:/MinBias_TuneCP5_14TeV-pythia8/Run3Winter21GS-112X_mcRun3_2021_realistic_v15-v1/GEN-SIM" \
   --conditions auto:phase1_2021_realistic \
   --step LHE,GEN,SIM,DIGI,L1,DIGI2RAW,HLT:GRun \
   --geometry DB:Extended \
   --era Run3 \
   --no_exec \
   --mc \
   -n 10
