import pandas as pd
#reading the file with the company or country names
df1 = pd.read_csv("input-domains.csv")
#creating a new dataframe
df2 = pd.DataFrame(columns=['url'])
count = 0
#going through the input list row by row
for row in range(0, len(df1)):
    input = df1.input[row]
    input2 = df1.input2[row]
    #creating search string for each country / company name
    print("Creating next url")
    url = "https://www.google.com/search?q=%22%28ethics+OR+ethical+OR+governance%29+AROUND%2810%29%22+AND+%28AI+OR+artificial+intelligence%29+AND+%28principles+OR+guidelines+OR+recommendations%29+AND+%28%22" + input + "%22%29+AND+site%3A" + input2
    print(url)
    df2.loc[len(df2)] = [url]
    count = count + 1
    #adding each search result to the table

df2.to_csv("output_Q4.csv")
print("Done.")
print("Your file (output_Q4.csv) is in your folder.")
