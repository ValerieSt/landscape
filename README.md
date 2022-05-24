# landscape

'google-input-output.py' is a python script that automates a google search

Input: csv file with countries or company names in first column, column title 'input'

Search string (can be adapted): "(AI OR artificial intelligence) AND (principles OR guidelines OR recommendations) AND ("[input from csv file]")

Output: overview of search results (top 30 results for each entry)

Requirements: python, pandas, googlesearch (pip install googlesearch-python), requests, numpy, lxml

If 'import search' from googlesearch does not work, use a virtual environment

You can use the file 'input.csv' as an example file
