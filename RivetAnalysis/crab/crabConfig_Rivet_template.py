from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'request_Rivet_INSHORT_DATE'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

# config.JobType.pluginName = 'PrivateMC'
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'ANALYZERCONFIG'
config.JobType.outputFiles = ['mc.yoda']
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = 'DATASETIN'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.outLFNDirBase = '/store/group/cmst3/user/gvonsem/Rivet/'
config.Data.publication = False
config.Data.outputDatasetTag = 'DATASETOUT'
config.Data.allowNonValidInputDataset = True

config.Site.storageSite = 'T2_CH_CERN'
config.Site.blacklist = ['T3_US_Baylor']
