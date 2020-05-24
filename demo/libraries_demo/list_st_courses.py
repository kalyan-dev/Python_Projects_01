# Display the batch schedule from Srikanth Technologies


import requests
from bs4 import BeautifulSoup

url = "http://srikanthtechnologies.com/"
resp = requests.get(url)
bs = BeautifulSoup(resp.text,"html.parser")

if resp.status_code != 200:
    print("Could not find the website")
    exit(1)
# else:
#     print(resp.text[:50])


for tag in bs.find_all("img"):
    # print(tag["src"])
    pass

# ctl00_ContentPlaceHolder1_GridView2

course_table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
# print(type(course_table))

# # # print(type(course_table.children))
# for c in course_table.children:
#     if "NavigableString" in str(type(c)):
#         continue
#     # print(c.name, type(c))
#     for d in c.contents:
#         if d.name == "td":
#             print(d.name,type(d),d.text)
#             # print(d.text)
#     # for r in course_table.findChildren(id="tr"):


for x in course_table.next_sibling:
    print(x.name)


