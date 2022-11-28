from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../config/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 1

config.Data.outputPrimaryDataset = 'ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 50  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/cmst3/user/adlintul/run3/gridpacks/hbb2022/samples'
config.Data.publication = False
config.Data.outputDatasetTag = 'NanoGEN'

config.Site.storageSite = 'T2_CH_CERN'
