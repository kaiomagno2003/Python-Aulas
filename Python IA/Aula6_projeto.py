tarefas = {
    'nome': "Desenvolver projeto",
    'descricao': "Criar o projeto da aula 6",
    'categoria': "Curso Python",
    'prioridade': "Urgente",
    'concluida': False
}

#def adicionar_tarefa():
    
#def listar_tarefas():

#def status_tarefas():

#def listar_por_categorias():
    
#def listar_por_prioridade():
    

def menu():
    print('GERENCIAMENTO DE TAREFAS')
    while True:
        escolha = input("""
    1- ADICIONAR TAREFAS
    2- LISTAR TODAS AS TAREFAS
    3- LISTAR TAREFAS POR CARTEGORIA
    4- LISTAR TAREFAS POR PRIORIDADE
    5- ALTERAR STATUS DA TAREFA
    6- SAIR
    """)
        
        match escolha:
            case '1':
                adicionar_tarefas()
            case '2':
                listar_tarefas()
            case '3':
                listar_por_categoria()
            case '4':
                listar_por_prioridade()
            case '5':
                status_tarefa()
            case '6':
                clear()