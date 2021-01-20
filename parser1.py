import json

import requests
from bs4 import BeautifulSoup

url = "https://www.akchabar.kg/ru/loans/calculate/"

def get_table_data(data=None):
    sess = requests.Session()
    home_page = sess.get(url)

    print(home_page.cookies)
    home_cook=home_page.cookies.get_dict()['csrftoken']
    soup = BeautifulSoup(home_page.content, "html.parser")
    rvt = soup.find("input", attrs={"name": "csrfmiddlewaretoken"})['value']
    data1 = {
        'loan_type': 0,
        'loan_sum': 800000,
        'loan_currency': 'kgs',
        'loan_period': 12,
        'csrfmiddlewaretoken': sess.cookies.get_dict()['csrftoken']
    }
    # data['csrfmiddlewaretoken'] = rvt
    headers={
        'User-Agent': '...',
        'referer': 'https://...'

    }
    result = requests.post(url, data=data)
    print(result.headers)
    print(result)
    # print("your result is ",result)
    # soup1 = BeautifulSoup(result.text, 'html.parser')
    # table = soup1.find_all("table", class_="find_product")[0]
    # tr = table.find_all("tr")[1:]
    # td_row = []
    # index = 0
    # for d in tr:
    #     td_col = {}
    #     col_index = 0
    #     col_values = ["bank", 'percent', 'max_sum', 'period']
    #     for t in d.find_all("td")[:-3]:
    #         td_col[col_values[col_index]] = str(t.text.strip()).replace(u'\xa0', u' ')
    #         col_index = col_index + 1
    #     index = index + 1
    #     td_row.append(td_col)
    # return td_row
print(get_table_data())