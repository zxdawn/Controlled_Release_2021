

from loaddata import loaddata
from matchMethods import performMatching

import os

cwd = os.getcwd()

#def main():

    # Generate table of Stanford matched controlled releases
    # (1) Load data
operatorDF, meterDF_All, sonicDF_All = loaddata()
    # (2) match bridger data with release data
    
matchedDF_Bridger, matchedDF_GHGSat, matchedDF_CarbonMapper = performMatching(operatorDF, meterDF_All, sonicDF_All)



csvPath = os.path.join(cwd, 'matchedDF_Bridger.csv')
matchedDF_Bridger.to_csv(csvPath)

csvPath = os.path.join(cwd, 'matchedDF_GHGSat.csv')
matchedDF_GHGSat.to_csv(csvPath)

csvPath = os.path.join(cwd, 'matchedDF_CarbonMapper.csv')
matchedDF_CarbonMapper.to_csv(csvPath)

csvPath = os.path.join(cwd, 'meterDF_All.csv')
meterDF_All.to_csv(csvPath)

# COlumn names for export to teams:
    
cols = [
    "Stanford_timestamp",
    "cr_kgh_CH4_mean90", 
    "cr_kgh_CH4_lower90", 
    "cr_kgh_CH4_upper90", 
    "FacilityEmissionRate", 
    "FacilityEmissionRateUpper", 
    "FacilityEmissionRateLower", 
    "UnblindingStage", 
    "PipeSize_inch", 
    "MeterCode", 
    "PlumeEstablished", 
    "PlumeSteady", 
    "cr_kgh_CH4_mean30", 
    "cr_kgh_CH4_lower30", 
    "cr_kgh_CH4_upper30", 
    "cr_kgh_CH4_mean60", 
    "cr_kgh_CH4_lower60", 
    "cr_kgh_CH4_upper60", 
    "Operator_Timestamp"]

matchedDF_CarbonMapper_toTeam = matchedDF_CarbonMapper.reindex(cols)
csvPath = os.path.join(cwd, 'matchedDF_CarbonMapper_unblindedToCM.csv')
matchedDF_CarbonMapper_toTeam.to_csv(csvPath)


    # write matched results to csv
#    cwd = os.getcwd()

    #csvPath = os.path.join(cwd, 'MidlandTestAnalysisResults', 'StanfordMatchedPasses.csv')
    #matchedDF.to_csv(csvPath)




#if __name__ == '__main__':
#    main()
