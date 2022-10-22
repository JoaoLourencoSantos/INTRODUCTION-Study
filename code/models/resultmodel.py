
from datetime import date
from utils.dateutils import calcRate, dateWithIso, dateWithoutHours, diferenceInDays, diferenceInYears, getCurrentDate


class ResultModel:
            
    def toJson(nameWithOwner, primaryLanguage, stargazers, pullRequests, totalIssues, forks): 

        totalForks = forks if forks else 0
        totalStars = stargazers['totalCount'] if stargazers else 0
        totalIssues = totalIssues['totalCount'] if totalIssues else 0
        totalPullRequests = pullRequests['totalCount'] if pullRequests else 0 

        engagement = (totalIssues + totalPullRequests + totalForks) / 3

        return { 
            "ProjectName": nameWithOwner,  
            "PrimaryLanguage": primaryLanguage['name'] if primaryLanguage else "-",
            "Stars": totalStars,
            "TotalOfPullRequests": totalPullRequests,
            "TotalOfIssues": totalIssues,
            "TotalOfForks": totalForks,
            "Engagement": engagement,
        }