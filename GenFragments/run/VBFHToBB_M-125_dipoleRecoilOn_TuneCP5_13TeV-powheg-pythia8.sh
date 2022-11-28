#!/bin/bash

cmsDriver.py \
    SampleGeneration/GenFragments/python/VBFHToBB_M-125_dipoleRecoilOn_TuneCP5_13TeV-powheg-pythia8.py \
    --python_filename SampleGeneration/Analysis/config/VBFHToBB_M-125_dipoleRecoilOn_TuneCP5_13TeV-powheg-pythia8.py \
    --eventcontent NANOAODGEN \
    --datatier NANOAOD \
    --fileout file:VBFHToBB_M-125_dipoleRecoilOn_TuneCP5_13TeV-powheg-pythia8.root \
    --conditions auto:phase1_2022_realistic \
    --step LHE,GEN,NANOGEN \
    --geometry DB:Extended \
    --era Run3 \
    --no_exec \
    --mc \
    -n 1
