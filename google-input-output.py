import pandas as pd
from googlesearch import search
import requests
import numpy as np
import ssl
import time
from lxml.html import fromstring

def Link_title(URL):
  x = requests.get(URL)
  tree = fromstring(x.content)
  return tree.findtext('.//title')

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#reading the file with the company or country names
df1 = pd.read_csv("input.csv")
#creating a new dataframe
df2 = pd.DataFrame(columns=['input','entrynr', 'title', 'url'])
count = 0
#going through the input list row by row
for row in range(0, len(df1)):
    input = df1.input[row]
    #creating search string for each country / company name
    query = "(AI OR artificial intelligence) AND (principles OR guidelines OR recommendations) AND (" + input + ")"
    print("Searching for ", query)
    count = count + 1
    #getting top 30 results
    results = search(query, num_results = 30)
    entrynr = 0
    for result in results:
        entrynr = entrynr + 1
        url = result
        try:
            #getting the title for each url
            title = Link_title(url)
            title = title.strip()
        except:
            if url[-4:] == ".pdf":
                title = "[[Pdf File]]"
            else:
                title = np.nan
        #adding each search result to the table
        df2.loc[len(df2)] = [input, entrynr, title, url]
        print(input, entrynr, title, url)
        #adding some short breaks to avoid being blocked
        time.sleep(1)
        if (entrynr % 7) == 0:
            time.sleep(5)
        if (entrynr % 10) == 0:
            time.sleep(10)
        if entrynr > 30:
            break
    print("Nr of searches conducted: ", count)
    #saving results to a .csv (after search for one input is completed)
    df2.to_csv("output.csv")
print("Done.")
print("Total number of searches: ", count)
print("Your file (output.csv) is in your folder.")
