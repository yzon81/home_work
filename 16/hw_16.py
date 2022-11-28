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
        if resp_json is not None:
            counter = 1
            with open('hw_16-txt.txt', 'w') as file:
                file.write(f"{resp_json[0]['exchangedate']}\n")
                for res in resp_json:
                    file.write(f"{counter}. {res['txt']} to UAH: {res['rate']}\n")
                    counter += 1
        else:
            with open('hw_16-txt.txt', 'w') as file:
                file.write(res.content)
