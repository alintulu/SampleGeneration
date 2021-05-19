import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
 args = cms.vstring('root://xrootd-cms.infn.it//store/group/dpg_trigger/comm_trigger/TriggerStudiesGroup/Scouting/Run3/gridpacks/ZprimeToZH_MZprime600_MZ50_MH80_narrow_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz'),
 nEvents = cms.untracked.uint32(5000),
 numberOfParameters = cms.uint32(1),
 outputFile = cms.string('cmsgrid_final.lhe'),
 scriptName = cms.FileInPath('SampleGeneration/GenFragments/data/run_generic_tarball_xrootd.sh')
)

#Link to original datacards:
#https://github.com/cms-sw/genproductions/tree/master/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/exo_diboson/Spin-1/Zprime_Zh_Zhadhbb
#but modified (see gridpack content)

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(14000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring('23:onMode = off',
                                        '23:oneChannel = 1 0.33333 100 3 -3',
                                        '23:addChannel = 1 0.33333 100 2 -2',
                                        '23:addChannel = 1 0.33333 100 1 -1',
					'23:mWidth = 0.001',
                                        '25:onMode = off',
                                        '25:oneChannel = 1 0.33333 100 3 -3',
                                        '25:addChannel = 1 0.33333 100 2 -2',
                                        '25:addChannel = 1 0.33333 100 1 -1',
					'25:mWidth = 0.001',
                                        'ResonanceDecayFilter:filter = on'
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8PSweightsSettings',
                                    'processParameters',
                                    )
    )
)
