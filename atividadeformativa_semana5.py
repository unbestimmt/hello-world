# NOME: DANIELE CRISTINE ENDO PERES
# CURSO: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS

# sistema para gestão de dados acadêmicos


# função cabeçalho do menu principal
def espaco():
    print("\n"*5)
    print("#"*52)
    print("#", " "*48, "#")
    print("#", " "*8, "########   #      #   ########",   " "*8, "#")
    print("#", " "*8, "#      #   #      #   #       ",   " "*8, "#")
    print("#", " "*8, "#      #   #      #   #       ",   " "*8, "#")
    print("#", " "*8, "########   #      #   #       ",   " "*8, "#")
    print("#", " "*8, "#          #      #   #       ",   " "*8, "#")
    print("#", " "*8, "#          ########   ########",   " "*8, "#")
    print("#", " "*48, "#")
    print("#"*52)

# função sair do menu principal
def sair():
    print("Saindo do menu...\n\n")
    exit(0)

lista_alunos = [] # lista com dicionários com informações de estudantes
dicio_alunos = {}

# função incluir estudantes
def incluir_estudantes():
    while True:
        print("\nInsira o código, nome completo e CPF a serem incluídos.")
        codigo = int(input("Código: "))
        nome = input("Nome completo: ")
        cpf = int(input("CPF: "))
        dicio_alunos = {"codigo": codigo, "nome": nome, "cpf": cpf}
        lista_alunos.append(dicio_alunos)
        parar = input("\nDeseja adicionar um novo nome? (s/n)  ")
        if parar == "n": # comando para retornar ao menu de opções
            break

# função listar estudantes
def listar_estudantes():
    if len(lista_alunos) < 1:
        print("----- Não há estudantes cadastrados -----\n\n")
    else:
        print("----- ESTUDANTES: LISTAR ----- \n")
        for i in range(len(lista_alunos)):
            print(i+1, " ", lista_alunos[i])
        print("\n\n") 

# função alterar estudantes
def alterar_estudantes():
    registro = int(input("\nDigite o código do estudante que deseja alterar: "))
    registro_existente = False
    for i in lista_alunos:
        if i["codigo"] == registro:
            print("\nAlterar os dados de: Código:", i["codigo"], "- Nome:", i["nome"], "- CPF:", i["cpf"])
            novo_codigo = int(input("Código: "))
            novo_nome = input("Nome: ")
            novo_cpf = input("CPF: ")
            i["codigo"] = novo_codigo
            i["nome"] = novo_nome
            i["cpf"] = novo_cpf
            registro_existente = True
    if registro_existente == False:
        print("\n\n----- Registro inexistente -----\n")
        parar = input("Deseja tentar novamente?  (s/n)  ")
        if parar == "n":
            crud_estudantes()
        else:
            alterar_estudantes()
            print("\n")

# função excluir estudantes
def excluir_estudantes(): 
    registro = int(input("\nDigite o código do estudante que deseja excluir: "))
    registro_existente = False
    for i in lista_alunos:
        if i["codigo"] == registro:
            print("\nRemovendo do sistema: ", i["codigo"], "- Nome:", i["nome"], "- CPF:", i["cpf"])
            lista_alunos.remove(i)
            registro_existente = True
    if registro_existente == False:
        print("\n\n----- Registro inexistente -----\n")
        parar = input("Deseja tentar novamente?  (s/n)  ")
        if parar == "n":
            crud_estudantes()
        else:
            excluir_estudantes()
            print("\n")

# função menu estudantes com opções de listar, incluir, alterar e excluir
def crud_estudantes():
    while True:
        try:
            print("Digite o número da ação desejada:\n\n1. Incluir\n2. Listar\n3. Alterar\n4. Excluir\n0. Retornar ao menu principal\n")
            acao = int(input("Opção escolhida: "))
            print("\n")
            if acao == 1: # comando para incluir nome e sobrenome de alunos
                print("----- ESTUDANTES: INCLUIR -----")
                incluir_estudantes() # função para incluir estudantes
                print("\n")

            elif acao == 2: # comando para listar alunos cadastrados
                listar_estudantes() # função para listar estudantes

            elif acao == 3: # comando para alterar alunos cadastrados
                print("----- ESTUDANTES: ALTERAR -----")
                alterar_estudantes()
                print("\n")

            elif acao == 4: # comando para excluir alunos cadastrados
                print("----- ESTUDANTES: EXCLUIR -----")
                excluir_estudantes() # função para excluir estudantes
                print("\n")

            elif acao == 0: # retorna ao menu principal
                print("Retornando ao menu principal...\n")
                gestao_dados()
            else:
                print("Opção inválida. Tente um número entre 1 e 4 ou 0 para sair do menu.\n\n")
        except ValueError:
            print("Opção inválida.")

# função temporária para opções da 2 a 5 do menu principal
def crud():
    print("Em desenvolvimento. Retornando ao menu principal...")
    gestao_dados()

# função menu inicial com opções de estudantes, disciplinas, professores, turmas e matrículas
def gestao_dados():
    espaco()
    print("\nBem-vindo(a) ao sistema de gestão de dados da PUC-PR. \nDigite o número da opção desejada:\n")
    while True:
        try:
            print("1. Estudantes\n2. Disciplinas\n3. Professores\n4. Turmas\n5. Matrículas\n0. Sair do menu\n\n")
            opcao = int(input("Opção escolhida: "))
            print("\n")
            if opcao == 1:
                print("-"*10, "ESTUDANTES", "-"*10,"\n")
                crud_estudantes()

            elif opcao == 2:
                print("-"*10, "DISCIPLINAS", "-"*10,"\n")
                crud()

            elif opcao == 3:
                print("-"*10, "PROFESSORES", "-"*10,"\n")
                crud()

            elif opcao == 4:
                print("-"*10, "TURMAS", "-"*10,"\n")
                crud()

            elif opcao == 5:
                print("-"*10, "MATRÍCULAS", "-"*10,"\n")
                crud()
            
            elif opcao == 0:
                sair()
            
            else:
                print("Opção inválida. Digite uma opção de 1 a 5 ou 0 para sair do menu.\n\n")

        except ValueError:
            print("Opção inválida. Digite uma opção de 1 a 5 ou 0 para sair do menu.\n\n")

gestao_dados()