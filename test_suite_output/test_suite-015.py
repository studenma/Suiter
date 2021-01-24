import requests

url = http://127.0.0.1:5000/api/calculator

payload = {"operation": "add","num1": 3,"num2": 2}
headers = {"Content-Type": "application/json"}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
