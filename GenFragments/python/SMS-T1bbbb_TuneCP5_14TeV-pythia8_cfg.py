import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

import math
from string import Template

baseSLHATmpl=Template("""
BLOCK MODSEL      # Model selection
    1    1        # sugra

BLOCK SPINFO      # Spectrum calculator information
    1    Minimal  # spectrum calculator
    2    1.0.0    # version number

BLOCK SMINPUTS  # Standard Model inputs
     1     1.27934000E+02   # alpha_em^-1(M_Z)^MSbar
     2     1.16637000E-05   # G_F [GeV^-2]
     3     1.18000000E-01   # alpha_S(M_Z)^MSbar
     4     9.11876000E+01   # M_Z pole mass
     5     4.25000000E+00   # mb(mb)^MSbar
     6     1.75000000E+02   # mt pole mass
     7     1.77700000E+00   # mtau pole mass

BLOCK MINPAR  # Input parameters - minimal models
     1     1.00000000E+02   # m0                  
     2     2.50000000E+02   # m12                 
     3     1.00000000E+01   # tanb                
     4     1.00000000E+00   # sign(mu)            
     5    -1.00000000E+02   # A0                  

    
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
   1000001     1.00000000E+05   # ~d_L
   2000001     1.00000000E+05   # ~d_R
   1000002     1.00000000E+05   # ~u_L
   2000002     1.00000000E+05   # ~u_R
   1000003     1.00000000E+05   # ~s_L
   2000003     1.00000000E+05   # ~s_R
   1000004     1.00000000E+05   # ~c_L
   2000004     1.00000000E+05   # ~c_R
   1000005     1.00000000E+05   # ~b_1
   2000005     1.00000000E+05   # ~b_2
   1000006     1.00000000E+05   # ~t_1
   2000006     1.00000000E+05   # ~t_2
   1000011     1.00000000E+05   # ~e_L
   2000011     1.00000000E+05   # ~e_R
   1000012     1.00000000E+05   # ~nu_eL
   1000013     1.00000000E+05   # ~mu_L
   2000013     1.00000000E+05   # ~mu_R
   1000014     1.00000000E+05   # ~nu_muL
   1000015     1.00000000E+05   # ~tau_1
   2000015     1.00000000E+05   # ~tau_2
   1000016     1.00000000E+05   # ~nu_tauL
   1000021     ${mgluino}       # ~g
   1000022     ${mlsp}          # ~chi_10
   1000023     1.00000000E+05   # ~chi_20
   1000025     1.00000000E+05   # ~chi_30
   1000035     1.00000000E+05   # ~chi_40
   1000024     1.00000000E+05   # ~chi_1+
   1000037     1.00000000E+05   # ~chi_2+
#
# DECAY TABLE
#         PDG            Width
DECAY   1000001     0.00000000E+00   # sdown_L decays
DECAY   2000001     0.00000000E+00   # sdown_R decays
DECAY   1000002     0.00000000E+00   # sup_L decays
DECAY   2000002     0.00000000E+00   # sup_R decays
DECAY   1000003     0.00000000E+00   # sstrange_L decays
DECAY   2000003     0.00000000E+00   # sstrange_R decays
DECAY   1000004     0.00000000E+00   # scharm_L decays
DECAY   2000004     0.00000000E+00   # scharm_R decays
DECAY   1000005     0.00000000E+00   # sbottom1 decays
DECAY   2000005     0.00000000E+00   # sbottom2 decays
DECAY   1000006     0.00000000E+00   # stop1 decays
DECAY   2000006     0.00000000E+00   # stop2 decays
DECAY   1000011     0.00000000E+00   # selectron_L decays
DECAY   2000011     0.00000000E+00   # selectron_R decays
DECAY   1000012     0.00000000E+00   # snu_elL decays
DECAY   1000013     0.00000000E+00   # smuon_L decays
DECAY   2000013     0.00000000E+00   # smuon_R decays
DECAY   1000014     0.00000000E+00   # snu_muL decays
DECAY   1000015     0.00000000E+00   # stau_1 decays
DECAY   2000015     0.00000000E+00   # stau_2 decays
DECAY   1000016     0.00000000E+00   # snu_tauL decays
##### gluino decays - no offshell decays needed
DECAY   1000021     ${width}   # gluino decays
#           BR         NDA      ID1       ID2       ID3
      1.0000000E+00    3     1000022        -5         5   # BR(~gl -> N1 bbar b)
DECAY   1000022     0.00000000E+00   # neutralino1 decays
DECAY   1000023     0.00000000E+00   # neutralino2 decays
DECAY   1000024     0.00000000E+00   # chargino1+ decays
DECAY   1000025     0.00000000E+00   # neutralino3 decays
DECAY   1000035     0.00000000E+00   # neutralino4 decays
DECAY   1000037     0.00000000E+00   # chargino2+ decays
""")

#ctau in mm; returns width in GeV
def ctauToWidth(ctau):
    f = 1.97326979e-13 #[mm*GeV] (=c*hbar)
    return f/ctau
    
generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(14000.),
    RandomizedParameters = cms.VPSet(),
)

scenarios = []
for ctau in [1e-1,1e0,1e1,1e2,1e3]:
    for mgluino in [1000,2000,3000]:
        scenarios.append({'ctau':ctau,'mgluino':mgluino,'mlsp':100})
        scenarios.append({'ctau':ctau,'mgluino':mgluino,'mlsp':mgluino-100})

print len(scenarios)

for scenario in scenarios:
    basePythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            'SUSY:gg2gluinogluino = on',
            'SUSY:qqbar2gluinogluino = on',
            'SUSY:idA = 1000021',
            'SUSY:idB = 1000021',
            '1000021:tau0 = %E' % scenario['ctau'],
            'RHadrons:allow = on',
            'ParticleDecays:tau0Max = 10000.0'
        ),
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
                ('SMS_T1bbbb_mgluino%.1e_mlsp%.1e_ctau%.1e' % (scenario['mgluino'], scenario['mlsp'], scenario['ctau'])).replace('+','')
            ),
            SLHATableForPythia8 = cms.string(baseSLHATmpl.substitute(
                mgluino='%E'%(scenario['mgluino']),
                mlsp='%E'%(scenario['mlsp']),
                width='%E'%(ctauToWidth(scenario['ctau'])),
            )),
            PythiaParameters = basePythiaParameters,
        ),
    )


