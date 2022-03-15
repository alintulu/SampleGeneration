#!/bin/bash

cmsDriver.py \
    SampleGeneration/GenFragments/python/HWminusJ_HanythingJ_NNPDF31_13TeV_M125_Vhadronic.py \
    --python_filename SampleGeneration/Analysis/config/HWminusJ_HanythingJ_NNPDF31_13TeV_M125_Vhadronic.py \
    --eventcontent NANOAODGEN \
    --datatier NANOAOD \
    --fileout file:hwminus-nanogen.root \
    --conditions auto:phase1_2021_realistic \
    --step LHE,GEN,NANOGEN \
    --geometry DB:Extended \
    --era Run3 \
    --no_exec \
    --mc \
    -n 10
