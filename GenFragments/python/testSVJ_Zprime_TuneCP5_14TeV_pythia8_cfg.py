import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP2Settings_cfi import * 

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(14000.),
    RandomizedParameters = cms.VPSet(),
)

points = [{'processParameters': [
    'HiddenValley:ffbar2Zv = on', 
        'HiddenValley:Ngauge = 2', 
    'HiddenValley:spinFv = 0', 
    'HiddenValley:FSR = on', 
    'HiddenValley:fragment = on', 
    'HiddenValley:alphaOrder = 1', 
    'HiddenValley:Lambda = 3.2',
     'HiddenValley:nFlav = 2', 
     'HiddenValley:probVector = 0.75', 
    
    '4900023:m0 = 1500', 
    '4900023:mMin = 1499', 
    '4900023:mMax = 1501', 
    '4900023:mWidth = 0.01', 
    '4900023:oneChannel = 1 0.982 102 4900101 -4900101', 
    '4900023:addChannel = 1 0.003 102 1 -1', 
    '4900023:addChannel = 1 0.003 102 2 -2', 
    '4900023:addChannel = 1 0.003 102 3 -3', 
    '4900023:addChannel = 1 0.003 102 4 -4', 
    '4900023:addChannel = 1 0.003 102 5 -5', 
    '4900023:addChannel = 1 0.003 102 6 -6', 
    '4900101:m0 = 0.5', 
    '4900111:m0 = 1', 
    '4900211:m0 = 1', 
    '51:m0 = 0.0', 
    '51:isResonance = false', 
    '4900113:m0 = 1', 
    '4900213:m0 = 1', 
    '53:m0 = 0.0', 
    '53:isResonance = false', 

     '4900001:m0 = 5000', 
     '4900002:m0 = 5000', 
     '4900003:m0 = 5000', 
     '4900004:m0 = 5000', 
     '4900005:m0 = 5000', 
     '4900006:m0 = 5000', 
     '4900011:m0 = 5000', 
     '4900012:m0 = 5000', 
     '4900013:m0 = 5000', 
     '4900014:m0 = 5000', 
     '4900015:m0 = 5000', 
     '4900016:m0 = 5000', 
     '4900111:oneChannel = 1 0.3 0 51 -51', 
     '4900111:addChannel = 1 0.233333 91 2 -2', 
     '4900111:addChannel = 1 0.233333 91 1 -1', 
     '4900111:addChannel = 1 0.233333 91 3 -3', 
     '4900211:oneChannel = 1 0.3 0 51 -51', 
     '4900211:addChannel = 1 0.233333 91 2 -2', 
     '4900211:addChannel = 1 0.233333 91 1 -1', 
     '4900211:addChannel = 1 0.233333 91 3 -3', 
     '4900113:oneChannel = 1 0.3 0 53 -53', 
     '4900113:addChannel = 1 0.233333 91 2 -2', 
     '4900113:addChannel = 1 0.233333 91 1 -1', 
     '4900113:addChannel = 1 0.233333 91 3 -3', 
     '4900213:oneChannel = 1 0.3 0 53 -53', 
     '4900213:addChannel = 1 0.233333 91 2 -2', 
     '4900213:addChannel = 1 0.233333 91 1 -1', 
     '4900213:addChannel = 1 0.233333 91 3 -3'], 
     
     'name': 'SVJ_mZprime-1500_mDark-1_rinv-0.3_alpha-peak', 
     
     'weight': 2.0}, 
]

for point in points:
    basePythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock, 
        pythia8CP2SettingsBlock,
        processParameters = cms.vstring(point['processParameters']),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP2Settings',
            'processParameters',
        )
    )

    generator.RandomizedParameters.append(
        cms.PSet(
            ConfigWeight = cms.double(point['weight']),
            ConfigDescription = cms.string(point['name']),
            PythiaParameters = basePythiaParameters,
        ),
    )

darkhadronZ2filter = cms.EDFilter("MCParticleModuloFilter",
    moduleLabel = cms.InputTag('generator','unsmeared'),
    particleIDs = cms.vint32(51,53),
    multipleOf = cms.uint32(4),
    absID = cms.bool(True),
)

darkquarkFilter = cms.EDFilter("MCParticleModuloFilter",
    moduleLabel = cms.InputTag('generator','unsmeared'),
    particleIDs = cms.vint32(4900101),
    multipleOf = cms.uint32(2),
    absID = cms.bool(True),
    min = cms.uint32(2),
    status = cms.int32(23),
)

ProductionFilterSequence = cms.Sequence(generator+darkhadronZ2filter+darkquarkFilter)

