import requests

bank_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

try:
    res = requests.get(bank_url)
except:
    print('Some exception')
else:
    if 300 > res.status_code >= 200:
        try:
            resp_json = res.json()
        except:
            print('Json exception')
        else:
            print(type(resp_json))
            print(resp_json)

        with open('hw_16-txt.txt', 'wb') as file:
            file.write(res.content)

