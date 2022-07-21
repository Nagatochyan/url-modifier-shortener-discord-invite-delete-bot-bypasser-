
import requests
nagato = input(f'URL:')
payload={
    'name':"shorturl",
    'query1': nagato,
    'query2': "1",
    'auth': "auth"
}
header ={
}

url = 'https://url.onl.jp/gs_api/'
response = requests.post(url,data=payload)
print(response.json())