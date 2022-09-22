import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13600.),
    RandomizedParameters = cms.VPSet(),
)

model = "BulkGraviton_hh_GF_HH_narrow"
mpoints=[]
mx = [600, 700, 820, 960, 1120, 1300, 1500]
mh = [34, 38, 44, 47, 50, 53, 57]
for x in mx:
    for h in mh:
        mpoints.append([x, h])

for point in mpoints:
    generator.RandomizedParameters.append(
        cms.PSet(
            ConfigWeight = cms.double(1),
            #GridpackPath = cms.string('/eos/cms/store/cmst3/user/adlintul/run3/gridpacks/bulkgraviton/decayed/%s_MX%s_MH%s_slc7_amd64_gcc900_CMSSW_12_0_2_tarball.tar.xz' % (model,point[0], point[1])),
            GridpackPath = cms.string('root://cms-xrd-global.cern.ch//store/cmst3/user/adlintul/run3/gridpacks/bulkgraviton/decayed/%s_MX%s_MH%s_slc7_amd64_gcc900_CMSSW_12_0_2_tarball.tar.xz' % (model,point[0], point[1])),
            scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_xrootd.sh'),
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


