# # import requests
# # response = requests.get("https://www.flipkart.com/")
# # print(response.text)

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html_code, "html.parser")
# import requests
# from bs4 import BeautifulSoup

# url = "https://www.flipkart.com/"
# response = requests.get(url)

# html_code = response.text   # ✅ NOW html_code exists

# soup = BeautifulSoup(html_code, "html.parser")

# print(soup.title.text)

import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/")
soup=BeautifulSoup(response.text,"html.parser")
print(soup.title.text)
print(soup.find("div", class_="uBUBH6").text)




#py -m pip install requests

#pip install beautifulsoup4
