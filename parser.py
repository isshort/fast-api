import json

import requests
from bs4 import BeautifulSoup

url = "https://www.akchabar.kg/ru/loans/calculate/"
import requests
import json

sess = requests.Session()
home_page = sess.get(url)
soup = BeautifulSoup(home_page.content, "html.parser")
rvt = soup.find("input", attrs={"name": "csrfmiddlewaretoken"})['value']
sess_id = home_page.cookies.get_dict()
sess_token = sess_id['csrftoken']
# print("ses1_token ", sess_token)
# print("ses2_token ", sess_token)
data = {'loan_type': '0', 'loan_sum': 10000, 'loan_currency': 'kgs', 'loan_period': '12',
            'csrfmiddlewaretoken': "uRUGPIsVXnOGnGlk4Inm97A8liHafgt1b5CJSBoUSRVPwxPs2fprYVk2uIQv3yEz"}

headers = {'content-type': 'application/json'}

post_res=sess.patch(url,data=data,headers=headers)

print(post_res)
# sess_id = home_page.cookies.get_dict()
# sess_token = sess_id['csrftoken']
# print("ses1_token ", sess_token)
# print("ses2_token ", sess_token)
# data = {'loan_type': '0', 'loan_sum': 10000, 'loan_currency': 'kgs', 'loan_period': '12',
#         'csrfmiddlewaretoken': sess_token}
# # html= urlopen(url)
# # print(html)
# post = requests.post(url, data=data)
# print(post.status_code, post.reason)

#
# def get_table_data(data=None):
#     sess = requests.Session()
#     home_page = sess.get(url)
#     soup = BeautifulSoup(home_page.content, "html.parser")
#     rvt = soup.find("input", attrs={"name": "csrfmiddlewaretoken"})['value']
#
#     # if data.__contains__("deposit2"):
#     #     data.pop("deposit2")
#     # print("Your data is",data)
#     data = {'loan_type': '0', 'loan_sum': 10000, 'loan_currency': 'kgs', 'loan_period': '12',
#             'csrfmiddlewaretoken': rvt}
#     headers = {'content-type': 'application/json', 'User-Agent': 'curl/7.47.1'}
#     result = requests.post(url, data=json.dumps(data), headers=headers)
#     print("result is ", result)
#
#
# get_table_data()
