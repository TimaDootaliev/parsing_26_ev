from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag


with open('template/index.html', 'r') as html:
    html_code = html.read()
    soup = BeautifulSoup(html_code, 'html.parser')
    # p = soup.find_all('p')
    # for tag in p:
    #     print(tag.text)
    # p_a1 = soup.find_all('p', class_='a1')
    # print(p_a1)
    # span = soup.find('span').find('p')
    # print(span.text)
    # image = soup.find('img').get('src')
    # print(image)




