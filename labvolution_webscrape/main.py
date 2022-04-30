import requests
from bs4 import BeautifulSoup
url = 'https://www.labvolution.de/de/suche/?category=ep'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
print(soup)

# # get the last page of of the url
# page_num_url = "https://swapi.dev/about"
# response = requests.get(page_num_url)
# page_num_soup = soup(response.text, "html.parser")
# page_num_div = page_num_soup.find('div' ,class_='col-sm-2 col-lg-2 col-md-2')
# page_num = page_num_div.find('p')
# page_num = page_num.text 
# # extract int(num) from the html tag
# for i in page_num.split():
#     if i.isdigit():
#        page_num = int(i)
# # extracted page number   
# page_num
