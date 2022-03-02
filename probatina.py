import requests

r = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC?apikey=8B34D51A-91D5-4297-A351-4CCE54D30D97")

print(r.status_code)
print(r.json()["rates"][-599:-598])