import json, requests, sys

#Checks title for spacing so that the space can be replaced with an underscore in the parameters for the URL.
title = sys.argv[1]
if " " in title:
    x = title.replace(" ", "_")
else:
    x = title
    
#Parameters to be passed into the url
parameters = {'format' : 'json', 'action' : 'query', 'titles' : x, 'prop' : 'extracts', 'rvprop' : 'content', 'continue' : '', "exsectionformat" : "plain", "redirects" : ""}

#getting the content of the url
r = requests.get('http://en.wikipedia.org/w/api.php', params=parameters)

#turning that content into json and loading it
data = r.json()

#writing json content to file
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

#writing plaintext to file
with open('data2.txt', 'w') as file2:
    file2.write(str(data["query"]["pages"]))

