import json
from models.resultmodel import ResultModel

def parseDataTables(data):

    result = []
    for value in data:    
        singleResult    =  ResultModel.toJson( 
            value['nameWithOwner'], 
            value['primaryLanguage'],
            value['stargazers'],
            value['pullRequests'], 
            value['totalIssues'],
            value['forkCount'] 
        )
  
        result.append(singleResult)

    return result 


