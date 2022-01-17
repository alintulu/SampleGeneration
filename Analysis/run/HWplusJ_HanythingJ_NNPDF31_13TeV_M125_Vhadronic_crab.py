from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'HWplusJ_HanythingJ_NNPDF31_13TeV_M125_Vhadronic'
config.General.workArea = 'crab_projects_HWplusJ'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../config/HWplusJ_HanythingJ_NNPDF31_13TeV_M125_Vhadronic.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 1

config.Data.outputPrimaryDataset = 'HWplusJ_HanythingJ_Vhadronic'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 50  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/ml/Tagging4ScoutingHackathon/Adelina/DAZSLE'
config.Data.publication = False
config.Data.outputDatasetTag = 'NanoGEN-Hbb'

config.Site.storageSite = 'T2_CH_CERN'
