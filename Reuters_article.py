import requests
from bs4 import BeautifulSoup


url = r"""
https://www.reuters.com/technology/biden-signs-executive-order-improve-us-cybersecurity-amid-colonial-pipeline-2021-05-12/
"""
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
paras = soup.find_all('p')
main_str = """"""

for i in range(len(paras)):
    main_str += f"{soup.find_all('p')[i].get_text()} \n \n "

with open("Reuters_article.txt", "w") as txt:
    txt.write(main_str)
    txt.close()
