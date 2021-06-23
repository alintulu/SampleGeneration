import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(14000.),
    RandomizedParameters = cms.VPSet(),
)

model = "BulkGraviton_hh_GF_HH_narrow"
mpoints=[]
mH_l=60
mH_r=180
mH_step=10
mX_l=600
mX_r=1500
mX_step=100
mX_tmp=mX_l
while mX_tmp <= mX_r:
        mH_tmp=mH_l;
        while mH_tmp <=mH_r:
                mpoints.append([mX_tmp,mH_tmp]);
		if mH_tmp < 30: mH_step=5;
		else: mH_step=10;
                mH_tmp+=mH_step;
        mX_tmp+=mX_step;

for point in mpoints:
    generator.RandomizedParameters.append(
        cms.PSet(
            ConfigWeight = cms.double(1),
            GridpackPath = cms.string('root://xrootd-cms.infn.it//store/group/dpg_trigger/comm_trigger/TriggerStudiesGroup/Scouting/Run3/gridpacks/BulkGraviton_hh_GF_HH/%s_MX%s_MH%s_slc7_amd64_gcc700_CMSSW_10_6_25_tarball.tar.xz' % (model,point[0], point[1])),
            scriptName = cms.FileInPath('SampleGeneration/GenFragments/data/run_generic_tarball_xrootd.sh'),
            ConfigDescription = cms.string('%s_MX%s_MH%s' % (model, point[0], point[1])),
            PythiaParameters = cms.PSet(
                pythia8CommonSettingsBlock,
                pythia8CP5SettingsBlock,
                pythia8PSweightsSettingsBlock,
                processParameters = cms.vstring('25:onMode = off',
                                                '25:oneChannel = 1 0.33333 100 5 -5',
                                                '25:addChannel = 1 0.33333 100 4 -4',
                                                '25:addChannel = 1 0.11111 100 3 -3',
                                                '25:addChannel = 1 0.11111 100 2 -2',
                                                '25:addChannel = 1 0.11111 100 1 -1',
                                                'ResonanceDecayFilter:filter = on'
                ),
		parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8PSweightsSettings',
                			        'processParameters',
		)
            )
        )
    )


