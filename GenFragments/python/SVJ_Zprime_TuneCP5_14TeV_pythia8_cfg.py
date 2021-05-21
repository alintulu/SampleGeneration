import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

from svjHelper import *

import copy




benchmark = {'mzprime':1000,'mDark':20,'rinv':0.3,'alpha':'peak'}

scenarios = []
#scenarios.append(benchmark)


for rinv in [0.3,0.7]:
    for mzprime in [500,750,1000,1500]:
        scenario = copy.deepcopy(benchmark)
        scenario['mzprime']=mzprime
        scenario['rinv']=rinv
        scenarios.append(scenario)
        
    for mDark in [5,10,20,40,80]:
        scenario = copy.deepcopy(benchmark)
        scenario['mDark']=mDark
        scenario['rinv']=rinv
        scenarios.append(scenario)
    
for alpha in ['low','high']:
    scenario = copy.deepcopy(benchmark)
    scenario['alpha']=alpha
    scenarios.append(scenario)
    
print len(scenarios)


generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(14000.),
    RandomizedParameters = cms.VPSet(),
)

for scenario in scenarios:
    helper = svjHelper()
    helper.setModel('s',scenario['mzprime'],scenario['mDark'],scenario['rinv'],scenario['alpha'])

    basePythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(helper.getPythiaSettings()),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'processParameters',
        )
    )

    generator.RandomizedParameters.append(
        cms.PSet(
            ConfigWeight = cms.double(1.),
            ConfigDescription = cms.string(
                ('SVJ_mzprime%.1e_mdark%.1f_rinv%.1f_%s' % (scenario['mzprime'], scenario['mDark'], scenario['rinv'],scenario['alpha'])).replace('+','')
            ),
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


