from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'HWminusJ_HToGamGam_gen2pu'
config.General.workArea = 'crab_projects_HWminusJ_HToGamGam_gen2pu'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../config/HWminusJ_HToGamGam_gen2pu_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 1

config.Data.outputPrimaryDataset = 'HWminusJ_HToGamGam_gen2pu_crab'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 50  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/ml/Tagging4ScoutingHackathon/Adelina/DAZSLE'
config.Data.publication = False
config.Data.outputDatasetTag = 'gen2pu'

config.Site.storageSite = 'T2_CH_CERN'
