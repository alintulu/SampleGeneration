#!/bin/bash

cmsDriver.py \
    mini2nanoaod \
    --filein file:miniaod.root \
    --eventcontent NANOAODGEN \
    --datatier NANOAOD \
    --fileout file:nanoaod.root \
    --conditions auto:phase1_2022_realistic \
    --step NANOGEN \
    --geometry DB:Extended \
    --era Run3 \
    --no_exec \
    --mc \
    --customise PhysicsTools/NanoAOD/custom_run3scouting_cff_TEMP.PrepRun3ScoutingCustomNanoAOD_MC \
    --customise_commands "process.schedule.remove(process.nanoAOD_step)", "process.NANOAODSIMoutput.outputCommands.extend(['keep edmTriggerResults_*_*_*'])", "process.NANOAODGENoutput.isPFScouting=cms.untracked.bool(True)" \
    -n 50
    

#124X_dataRun3_HLT_v4 \
#--customise_commands "process.NANOAODGENoutput.outputCommands.extend(['keep edmTriggerResults_*_*_DQM'])" \
