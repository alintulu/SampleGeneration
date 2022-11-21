#!/bin/bash

cmsDriver.py \
    SampleGeneration/GenFragments/python/WminusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8.py \
    --python_filename SampleGeneration/Analysis/config/WminusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8.py \
    --eventcontent NANOAODGEN \
    --datatier NANOAOD \
    --fileout file:zh_qq.root \
    --conditions auto:phase1_2022_realistic \
    --step LHE,GEN,NANOGEN \
    --geometry DB:Extended \
    --era Run3 \
    --no_exec \
    --mc \
    -n 1
