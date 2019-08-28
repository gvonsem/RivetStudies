import FWCore.ParameterSet.Config as cms


# When running on GEN or GEN-SIM, one should set convert=False. When running on MiniAODSIM, put convert=True
# This is because the HEPMC dataformat has to be reproduced in the latter case. See e.g. https://twiki.cern.ch/twiki/bin/viewauth/CMS/GenParticles2HepMCConverter
convert=True

process = cms.Process("runRivetAnalysis")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)

process.maxEvents = cms.untracked.PSet(
#    input = cms.untracked.int32(-1)    
    input = cms.untracked.int32(10)    
)

#process.load("infile_ttbar_CH3Tune_cff")

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/TT_TuneCH3_13TeV-powheg-herwig7/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/09A0595C-A771-0A4A-8CE5-39C60D3B776D.root'),
    secondaryFileNames = cms.untracked.vstring(),
    noEventSort = cms.untracked.bool(True)
)


process.load("GeneratorInterface.RivetInterface.rivetAnalyzer_cfi")


process.rivetAnalyzer.AnalysisNames = cms.vstring("CMS_2016_I1491950","CMS_2018_I1663958","CMS_2018_I1662081","CMS_2017_TOP_17_015","CMS_2018_I1690148")  
process.rivetAnalyzer.CrossSection = cms.double(831.76) # NNLO (arXiv:1303.6254)
process.rivetAnalyzer.LHECollection = cms.InputTag('externalLHEProducer')
process.rivetAnalyzer.HepMCCollection = cms.InputTag('generatorSmeared') # generator generatorSmeared
#process.rivetAnalyzer.HepMCCollection = cms.InputTag('generator:unsmeared')
process.rivetAnalyzer.GenEventInfoCollection = cms.InputTag('generator') 
process.rivetAnalyzer.OutputFile = cms.string("mc.yoda") 
process.rivetAnalyzer.UseExternalWeight = cms.bool(True)
#process.rivetAnalyzer.UseExternalWeight = cms.bool(False)
process.rivetAnalyzer.useLHEweights = cms.bool(False)
#process.rivetAnalyzer.LHEweightNumber = cms.string("1001")  #1001: nominal; 1009: 0.5; 1005: 2.0  
process.rivetAnalyzer.LHEweightNumber = cms.int32(0)  #0: nominal 
process.rivetAnalyzer.DoFinalize = cms.bool(True)

if convert:
    process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
    process.load("GeneratorInterface.RivetInterface.genParticles2HepMC_cfi")
    process.load("GeneratorInterface.RivetInterface.mergedGenParticles_cfi")
    process.genParticles2HepMC.genParticles = cms.InputTag("mergedGenParticles")
    process.rivetAnalyzer.HepMCCollection = cms.InputTag("genParticles2HepMC:unsmeared")


#agrohsje for debugging 
process.dump=cms.EDAnalyzer('EventContentAnalyzer')

if convert: 
    process.p = cms.Path(process.mergedGenParticles*process.genParticles2HepMC*process.rivetAnalyzer)
else:
    process.p = cms.Path(process.rivetAnalyzer)
