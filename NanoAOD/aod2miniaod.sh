#!/bin/bash

cmsDriver.py \
  --python_filename aod2miniaod.py \
  --eventcontent MINIAODSIM \
  --customise Configuration/DataProcessing/Utils.addMonitoring \
  --datatier MINIAODSIM \
  --fileout file:miniaod.root \
  --conditions auto:phase1_2022_realistic \
  --step PAT \
  --geometry DB:Extended \
  --filein "/store/mc/Run3Summer22DRPremix/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/AODSIM/124X_mcRun3_2022_realistic_v12-v2/80000/8dcd8212-ccc5-4538-8203-12f1f6a7dcab.root" \
  --era Run3 \
  --no_exec \
  --mc \
  -n 1 \
 --customise_commands "process.MINIAODSIMoutput.outputCommands.extend(['drop *_hlt*_*_*','keep *_hltScoutingEgammaPacker_*_*','keep *_hltScoutingMuonPacker_*_*','keep *_hltScoutingPFPacker_*_*','keep *_hltScoutingPrimaryVertexPacker_*_*','keep *_hltScoutingTrackPacker_*_*','drop *_*_*_PAT','keep *_*GenParticles_*_*','keep *_slimmedGenJets*_*_*', 'keep *_slimmedMET*_*_*', 'keep edmTriggerResults_*_*_PAT'])"
