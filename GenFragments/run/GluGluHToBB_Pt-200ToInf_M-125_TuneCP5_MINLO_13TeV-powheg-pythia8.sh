#!/bin/bash

cmsDriver.py \
    SampleGeneration/GenFragments/python/GluGluHToBB_Pt-200ToInf_M-125_TuneCP5_MINLO_13TeV-powheg-pythia8.py \
    --python_filename SampleGeneration/Analysis/config/GluGluHToBB_Pt-200ToInf_M-125_TuneCP5_MINLO_13TeV-powheg-pythia8.py \
    --eventcontent NANOAODGEN \
    --datatier NANOAOD \
    --fileout file:GluGluHToBB_Pt-200ToInf_M-125_TuneCP5_MINLO_13TeV-powheg-pythia8.root \
    --conditions auto:phase1_2022_realistic \
    --step LHE,GEN,NANOGEN \
    --geometry DB:Extended \
    --era Run3 \
    --no_exec \
    --mc \
    -n 1
