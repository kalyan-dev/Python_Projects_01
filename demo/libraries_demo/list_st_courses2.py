# Display the batch schedule from Srikanth Technologies


import requests
from bs4 import BeautifulSoup

url = "http://srikanthtechnologies.com/"
resp = requests.get(url)
bs = BeautifulSoup(resp.text,"html.parser")

# ctl00_ContentPlaceHolder1_GridView2
course_table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")

rows = course_table.findAll("tr")[1:]

for r in rows:
    cols = r.findAll("td")
    print(f"{cols[0].text:30}   {cols[1].text:20}    {cols[2].text:20}")


