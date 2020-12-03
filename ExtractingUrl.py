#this program will webscrape all the <a> tags from a URL!

#step 1: always import these two libraries 
from bs4 import BeautifulSoup
import requests


#step 2: select the target URL(the url you want to webscrape)
url = "https://boston.craigslist.org/d/software-qa-dba-etc/search/sof"

#step 3: create a response object to get the URL
response = requests.get(url)

#step 4: extract the source code of the URL/Website
data = response.text

#step 5: to navigate, you need to pass the source code into beautiful soup.
#this will make the text easier to read!
soup = BeautifulSoup(data, 'html.parser')
#now we will be able to extract certain html tags!

#step 6: get the tags you want to take out!
tags = soup.find_all('a')

#step 7: get all the links from the <a> tags
for tag in tags:
    print(tag.get('href'))
