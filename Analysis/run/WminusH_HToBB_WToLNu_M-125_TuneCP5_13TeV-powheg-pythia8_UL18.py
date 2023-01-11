from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'WminusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8_UL18'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../config/WminusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8_UL18.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 1

config.Data.outputPrimaryDataset = 'WminusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8_UL18'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 50  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/cmst3/user/adlintul/run3/gridpacks/hbb2022/samples'
config.Data.publication = False
config.Data.outputDatasetTag = 'NanoGEN'

config.Site.storageSite = 'T2_CH_CERN'
