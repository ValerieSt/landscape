import pandas as pd
#reading the file with the company or country names
df1 = pd.read_csv("input.csv")
#creating a new dataframe
df2 = pd.DataFrame(columns=['url'])
count = 0
#going through the input list row by row
for row in range(0, len(df1)):
    input = df1.input[row]
    #creating search string for each country / company name
    print("Creating next url")
    url = "https://www.google.com/search?q=(AI+OR+artificial+intelligence)+AND+(principles+OR+guidelines+OR+recommendations)+AND+(%22" + input + "%22)"
    print(url)
    df2.loc[len(df2)] = [url]
    count = count + 1
    #adding each search result to the table

df2.to_csv("output_Q1.csv")
print("Done.")
print("Your file (output_Q1.csv) is in your folder.")
