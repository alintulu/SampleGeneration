#!/bin/bash

cmsDriver.py \
    step2 \
    --python_filename SampleGeneration/Analysis/config/pu2rawminiaod.py \
    --datatier MINIAODSIM \
    --eventcontent RAWMINIAODSIM \
    --filein file:htogammagamma_pu.root \
    --conditions auto:phase1_2021_realistic \
    --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI,PAT \
    --geometry DB:Extended \
    --fileout file:htogammagamma_rawminiaod.root \
    --era Run3 \
    --no_exec \
    --mc \
    -n 10
