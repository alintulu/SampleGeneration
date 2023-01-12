from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'AOD2NANOAOD'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'aod2nanoaod.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 1

config.Data.inputDataset = '/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v2/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/group/cmst3/user/adlintul/run3/samples/scouting'
config.Data.publication = False
config.Data.outputDatasetTag = 'AOD2NANOAOD'

config.Site.storageSite = 'T2_CH_CERN'

