"""
Collections of objects that are helpful for the parsers
"""

RES_DATA_NO_UNCS = {
    "resMemsize",
    "totNuclides",
    "fissionProductInhTox",
    "ingestionToxicity",
    "totSfRate",
    "electronDecaySource",
    "uresDiluCut",
    "implNxn",
    "neutronErgTol",
    "useDbrc",
    "actinideActivity",
    "actinideInhTox",
    "photonDecaySource",
    "te132Activity",
    "implCapt",
    "alphaDecaySource",
    "totActivity",
    "fissionProductActivity",
    "simulationCompleted",
    "sourcePopulation",
    "useUres",
    "lostParticles",
    "iniFmass",
    "totPhotonNuclides",
    "totTransmuRea",
    "uresEmax",
    "uresUsed",
    "i132Activity",
    "cpuUsage",
    "xsMemsize",
    "memsize",
    "totDecayNuclides",
    "tmsMode",
    "actinideIngTox",
    "totDosimetryNuclides",
    "cs134Activity",
    "uresEmin",
    "totCells",
    "neutronErgNe",
    "fissionProductIngTox",
    "sampleCapt",
    "actinideDecayHeat",
    "runningTime",
    "uresAvail",
    "cycleIdx",
    "neutronEmin",
    "neutronDecaySource",
    "totDecayHeat",
    "dopplerPreprocessor",
    "matMemsize",
    "inhalationToxicity",
    "sampleFiss",
    "totFmass",
    "useDelnu",
    "cs137Activity",
    "availMem",
    "neutronEmax",
    "miscMemsize",
    "sampleScatt",
    "unusedMemsize",
    "unionCells",
    "sr90Activity",
    "totCpuTime",
    "implFiss",
    "allocMemsize",
    "unknownMemsize",
    "ompParallelFrac",
    "fissionProductDecayHeat",
    "totReaChannels",
    "totTransportNuclides",
    "ifcMemsize",
    "i131Activity",
    "balaSrcNeutronTot",
    "balaSrcNeutronFiss",
    "balaSrcNeutronNxn",
    "balaLossNeutronFiss",
    "balaLossNeutronTot",
    "balaLossNeutronCapt",
    "balaLossNeutronLeak",
    "transportCycleTime",
    "processTime",
    "initTime",
}
"""
Set containing keys for objects stored in :attr:`ResultsReader.resdata`
that do not contain uncertainties.
"""
