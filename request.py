import requests
import json

url = 'http://127.0.0.1:5000/calcular'

data_fatorial = {'operacao':'fatorial', 'numero': 5}
data_fibonacci = {'operacao':'fibonacci', 'numero':8}

response_fatorial = requests.post(url, json=data_fatorial)
response_fibonacci = requests.post(url, json=data_fibonacci)

if response_fatorial.status_code == 200:
    resultado_fatorial = response_fatorial.json()['resultado']
    print(f'Resultado do fatorial: {resultado_fatorial}')
else:
    print("Error:", result["error"])
    exit(1)

if response_fibonacci.status_code == 200: 
    resultado_fibonacci = response_fibonacci.json()['resultado']
    print(f'Resultado da seq. de Fibonacci: {resultado_fibonacci}')
else:
    print("Error:", result["error"])
    exit(1)

