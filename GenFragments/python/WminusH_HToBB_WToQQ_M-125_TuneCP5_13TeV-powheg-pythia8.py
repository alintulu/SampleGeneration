import FWCore.ParameterSet.Config as cms

# link to datacards: 
# https://github.com/cms-sw/genproductions/blob/abd5e620174f05eada6dac35f9e366f3019fd6ef/bin/Powheg/production/2017/13TeV/Higgs/WminusHJ_HanythingJ_NNPDF31_13TeV/HWminusJ_HanythingJ_NNPDF31_13TeV_M125_Vhadronic.input

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('root://cms-xrd-global.cern.ch//store/cmst3/user/adlintul/run3/gridpacks/hbb2022/HWJ_slc7_amd64_gcc700_CMSSW_10_2_29_WminusH_HToBB_WToQQ.tgz'),
    nEvents = cms.untracked.uint32(10),
    generateConcurrently = cms.untracked.bool(True),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_xrootd.sh')
)

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *

generator = cms.EDFilter("Pythia8ConcurrentHadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13600.),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        pythia8PowhegEmissionVetoSettingsBlock,
        processParameters = cms.vstring(
            'POWHEG:nFinal = 3',   ## Number of final state particles
                                   ## (BEFORE THE DECAYS) in the LHE
                                   ## other than emitted extra parton
            '25:m0 = 125.0',
            '25:onMode = off',
            '25:onIfMatch = 5 -5', #Decay H -> bb only
          ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8PSweightsSettings',
                                    'pythia8PowhegEmissionVetoSettings',
                                    'processParameters'
                                    )
        )
                         )

ProductionFilterSequence = cms.Sequence(generator)

