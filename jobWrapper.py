#in this peice of code, we will scrape craigslist for jobs!

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

#step 6: get the jobs wrapper
jobs = soup.find_all('p',{'class':'result-info'})

#steps 7: loop through the wrapper to extract the jobs
for job in jobs:
    title = job.find('a',{'class':'result-title'}).text
    location_tag = job.find('span',{'class':'result-hood'})
    location = location_tag.text[2:-1] if location_tag else "N/A"
    date = job.find('time',{'class':'result-date'}).text
    link = job.find('a',{'class':'result-title'}).get('href')
    print('Job Title:', title, '\nLocation', location, '\nDate:', date, '\nLink:', link, '\n---')


