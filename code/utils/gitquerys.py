
def getPage(page) :
   return (  "null"  if page == None else "\"" + str(page) + "\"")

def getFirstQuery(size, page):
    return """
      {
        search(query: "stars:>100 language:Typescript", type: REPOSITORY, first: """ + str(size) + """, after: """ + getPage(page) + """) { 
          pageInfo {
            hasNextPage
            endCursor
          }
          nodes {
            ... on Repository {
              id
              nameWithOwner
              createdAt
              updatedAt
              primaryLanguage {
                name
              }
              stargazers {
                totalCount
              }
              pullRequests {
                totalCount
              }
              totalIssues: issues {
                totalCount
              }
              forkCount
            }
          }
        }
      }

"""  