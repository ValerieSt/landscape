#requirements: pandas, googlesearch (pip install googlesearch-python)

import pandas as pd
from googlesearch import search
from bs4 import BeautifulSoup
import requests
import numpy as np
import ssl
import time

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

df1 = pd.read_csv("input.csv")
df2 = pd.DataFrame(columns=['imput','entrynr', 'title', 'url'])
count = 0
for row in range(0, len(df1)):
    input = df1.input[row]
    query = input + " AI principles"
    print("Searching for ", query)
    count = count + 1
    results = search(query, num_results = 10)
    entrynr = 0
    for result in results:
        try:
            reqs = requests.get(result)
            soup = BeautifulSoup(reqs.text, 'html.parser')
            entrynr = entrynr + 1
            url = result
            try:
                title = soup.find_all('title')[0]
            except:
                title = np.nan
        except:
                pass
        title = str(title)
        title = title[7:-8]
        title = title.strip()
        df2.loc[len(df2)] = [input, entrynr, title, url]
        print(input, entrynr, title, url)
        if entrynr > 10:
            break
        time.sleep(0.01)
    print("Nr of searches conducted: ", count)
    df2.to_csv("output.csv")
print("Total number of searches: ", count)
print("Done. Your file (output.csv) is in your folder.")
print()
