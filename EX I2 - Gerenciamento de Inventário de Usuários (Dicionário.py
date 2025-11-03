usuarios = {"id": 101, "perfil": "Analista", "status": "Ativos"}

usuarios["ultimo_login"] = "2024-10-01"

tem_licenca = "licenca_premium" in usuarios
print(f"Licença premium presente? {tem_licenca}")

usuarios["status"] = "Inativo"

print("Dicionário final:", usuarios)

