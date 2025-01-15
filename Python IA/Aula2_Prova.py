contato = {
    'nome': '',
    'telefone': '',
    'email': ''
}

nome = input("Digite o nome do contato: ")
telefone = input("Digite o telefone: ")
email = input("Digite o email: ")

contato['nome'] = nome
contato['telefone'] = telefone
contato['email'] = email
print('Contato cadastrado com sucesso!')
print('-'*50)
print(contato)