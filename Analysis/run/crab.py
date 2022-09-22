from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'BulkGraviton'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../config/gen2pu.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 1

config.Data.outputPrimaryDataset = 'BulkGraviton_hh_GF_HH_narrow'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 1  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/ml/Tagging4ScoutingHackathon/Adelina/Run3/samples/ParticleNet'
config.Data.publication = False
config.Data.outputDatasetTag = 'BulkGraviton'

config.Site.storageSite = 'T2_CH_CERN'
