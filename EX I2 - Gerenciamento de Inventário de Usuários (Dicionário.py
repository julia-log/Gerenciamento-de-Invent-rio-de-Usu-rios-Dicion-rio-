# I2: Gerenciamento de Inventário de Usuários (Dicionário)

# 1. Criar um dicionário inicial com informações do usuário
usuarios = {
    "id": 101,            # Identificador único do usuário
    "perfil": "Analista", # Tipo de perfil do usuário
    "status": "Ativo"     # Status atual do usuário
}

# 2. Adicionar um novo par chave-valor: "ultimo_login"
usuarios["ultimo_login"] = "2024-10-01"  # Registro da última data de login do usuário

# 3. Verificar se a chave "licenca_premium" existe no dicionário
tem_licenca = "licenca_premium" in usuarios  # Retorna True se existir, False caso contrário
print("Licença premium presente?", tem_licenca)

# 4. Modificar o status do usuário para "Inativo"
usuarios["status"] = "Inativo"  # Atualiza o valor da chave "status"

# 5. Exibir o dicionário final
print("Dicionário final de usuários:", usuarios)

