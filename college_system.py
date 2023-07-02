# system in PYTHON to manage data of a school/college, as in students, teachers/professors, courses, classes, and enrolment
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

import json

# função escrever arquivo json; serve para incluir, alterar e excluir dados de uma lista
def escrever_json(dados, arquivo):
    with open(arquivo + ".json", "w") as file:
        json.dump(dados, file)
        file.close()

# função ler arquivo json
def ler_json(arquivo):
    dados = []
    try:
        with open(arquivo + ".json", "r") as file:
            dados = json.load(file)
            file.close()
            return dados
    except FileNotFoundError:
        escrever_json(dados, arquivo)
        return dados

# função para incluir dados novamente
def adicnovo(crud, acao, novo_dado):
    while True:
        parar = input(f"\nDeseja adicionar {novo_dado}? (s/n)  ")
        if parar.lower() == "n": # comando para retornar ao menu de opções
            crud()
        elif parar.lower() == "s":
            acao()
        else:
            print("\n----- Valor inválido. Use s para sim e n para não -----")
            continue

# função verificar se usuário quer tentar novamente após mostrar registro inexistente
def inexistente(crud, acao):
    while True:
        parar = input("\nDeseja tentar novamente? (s/n)  ")
        if parar.lower() == "n": # comando para retornar ao menu de opções
            print(" ")
            crud()
        elif parar.lower() == "s":
            acao()
            print("\n")
        else:
            print("\n----- Valor inválido. Use s para sim e n para não -----")
            continue


########## FUNÇÕES ESTUDANTES #################################################################################

# função incluir estudantes
def incluir_estudantes():
    try:
        dicio_alunos = {}
        alunos = ler_json("estudantes")
        while True:
            print("\nInsira o código, nome completo e CPF a serem incluídos.")
            codaluno = int(input("Código: "))
            nome = input("Nome completo: ")
            cpf = input("CPF: ")
            for i in alunos:
                if i["codaluno"] == codaluno:
                    print("\n----- Código já cadastrado para outro aluno -----")
                    incluir_estudantes()
            for i in alunos:
                if i["cpf"] == cpf:
                    print("\n----- CPF já cadastrado para outro aluno -----")
                    incluir_estudantes()
            dicio_alunos = {"codaluno": codaluno, "nome": nome, "cpf": cpf}
            alunos.append(dicio_alunos)
            escrever_json(alunos, "estudantes")
            print("\n----- Estudante salvo(a) com sucesso! -----")
            adicnovo(crud_estudantes, incluir_estudantes, "um novo nome")
    except ValueError:
        print("\n----- Valor inválido. Tente usar apenas números para código -----")
        incluir_estudantes()

# função listar estudantes
def listar_estudantes():
    alunos = ler_json("estudantes")
    if len(alunos) == 0:
        print("----- Não há estudantes cadastrados -----\n\n")
    else:
        print("----- ESTUDANTES: LISTAR ----- \n")
        print("#  [Código] - [Nome] - [CPF]\n")
        for i in range(len(alunos)):
            print(i+1, " ", '{:0>7}'.format(alunos[i]["codaluno"]), "-", alunos[i]["nome"].title(), "-", alunos[i]["cpf"])
        print("\n\n") 

# função alterar estudantes
def alterar_estudantes():
    try:
        alunos = ler_json("estudantes")
        registro = int(input("\nDigite o código do estudante que deseja alterar: "))
        registro_existente = False
        for i in alunos: # comando para verificar se o código do aluno existe
            if i["codaluno"] == registro:
                registro_existente = True
        if registro_existente is False:
            print("\n\n----- Registro inexistente -----\n")
            inexistente(crud_estudantes, alterar_estudantes)
        else:
            try:
                print("\nAlterar os dados de: Código:", i["codaluno"], "- Nome:", i["nome"], "- CPF:", i["cpf"])
                novo_codigo = int(input("Código: "))
                novo_nome = input("Nome: ")
                novo_cpf = input("CPF: ")
                for i in alunos:
                    if i["codaluno"] == registro:
                        i["codaluno"] = novo_codigo
                        i["nome"] = novo_nome
                        i["cpf"] = novo_cpf
            except ValueError:
                print("\n----- Valor inválido. Tente usar apenas números para código -----")
                alterar_estudantes()
            escrever_json(alunos, "estudantes")
            print("\n----- Estudante alterado(a) com sucesso! -----")
            registro_existente = True
    except ValueError:
        print("\n----- Valor inválido. Apenas números são aceitos -----")
        alterar_estudantes()

# função excluir estudantes
def excluir_estudantes():
    try:
        alunos = ler_json("estudantes")
        registro = int(input("\nDigite o código do estudante que deseja excluir: "))
        registro_existente = False
        for i in alunos: # comando para verificar se o código do aluno existe
            if i["codaluno"] == registro:
                print("\nRemovendo do sistema: ", i["codaluno"], "- Nome:", i["nome"], "- CPF:", i["cpf"])
                alunos.remove(i)
                escrever_json(alunos, "estudantes")
                print("\n----- Estudante apagado(a) com sucesso! -----")
                registro_existente = True
        if registro_existente is False:
            print("\n\n----- Registro inexistente -----\n")
            inexistente(crud_estudantes, excluir_estudantes)
    except ValueError:
        print("\n----- Valor inválido. Apenas números são aceitos -----")
        excluir_estudantes()


########## FUNÇÕES DISCIPLINAS #################################################################################

# função incluir disciplinas
def incluir_disciplinas():
    try:
        dicio_disciplinas = {}
        disciplinas = ler_json("disciplinas")
        while True:
            print("\nInsira o código e o nome da disciplina a serem incluídos.")
            coddisc = int(input("Código: "))
            nome = input("Nome: ")
            for i in disciplinas:
                if i["coddisc"] == coddisc:
                    print("\n----- Código já cadastrado para outra disciplina -----")
                    incluir_disciplinas()
            for i in disciplinas:
                if i["nome"] == nome:
                    print("\n----- Disciplina já cadastrada com outro código -----")
                    incluir_disciplinas()
            dicio_disciplinas = {"coddisc": coddisc, "nome": nome}
            disciplinas.append(dicio_disciplinas)
            escrever_json(disciplinas, "disciplinas")
            print("\n----- Disciplina incluída com sucesso! -----")
            adicnovo(crud_disciplinas, incluir_disciplinas, "uma nova disciplina")
    except ValueError:
        print("\n----- Valor inválido. Tente usar apenas números para código -----")
        incluir_disciplinas()

# função listar disciplinas
def listar_disciplinas():
    disciplinas = ler_json("disciplinas")
    if len(disciplinas) == 0:
        print("----- Não há disciplinas cadastradas -----\n\n")
    else:
        print("----- DISCIPLINAS: LISTAR ----- \n")
        print("#  [Código] - [Nome]\n")
        for i in range(len(disciplinas)):
            print(i+1, " ", '{:0>7}'.format(disciplinas[i]["coddisc"]), "-", disciplinas[i]["nome"].title())
        print("\n\n") 

# função alterar disciplinas
def alterar_disciplinas():
    try:
        disciplinas = ler_json("disciplinas")
        registro = int(input("\nDigite o código da disciplina que deseja alterar: "))
        registro_existente = False
        for i in disciplinas: # comando para verificar se o código da disciplina existe
            if i["coddisc"] == registro:
                registro_existente = True
        if registro_existente is False:
            print("\n\n----- Registro inexistente -----\n")
            inexistente(crud_disciplinas, alterar_disciplinas)
        else:
            for i in disciplinas:
                    if i["coddisc"] == registro:
                        try:
                            print("\nAlterar os dados de: Código:", i["coddisc"], "- Nome:", i["nome"])
                            novo_codigo = int(input("Código: "))
                            novo_nome = input("Nome: ")
                            i["coddisc"] = novo_codigo
                            i["nome"] = novo_nome
                            escrever_json(disciplinas, "disciplinas")
                            print("\n----- Disciplina alterada com sucesso! -----")
                            registro_existente = True
                        except ValueError:
                            print("\n----- Valor inválido. Tente usar apenas números para código -----")
                            alterar_disciplinas()
    except ValueError:
        print("\n----- Valor inválido. Apenas números são aceitos -----")
        alterar_disciplinas()

# função excluir disciplinas
def excluir_disciplinas():
    try:
        disciplinas = ler_json("disciplinas")
        registro = int(input("\nDigite o código da disciplina que deseja excluir: "))
        registro_existente = False
        for i in disciplinas: # comando para verificar se o código da disciplina existe
            if i["coddisc"] == registro:
                print("\nRemovendo do sistema: ", i["coddisc"], "- Nome:", i["nome"])
                disciplinas.remove(i)
                escrever_json(disciplinas, "disciplinas")
                print("\n----- Disciplina removida com sucesso! -----")
                registro_existente = True
        if registro_existente == False:
            print("\n\n----- Registro inexistente -----\n")
            inexistente(crud_disciplinas, excluir_disciplinas)
    except ValueError:
        print("\n----- Valor inválido. Apenas números são aceitos -----")
        excluir_disciplinas()


########## FUNÇÕES PROFESSORES #################################################################################

# função incluir professores
def incluir_professores():
    try:
        dicio_professores = {}
        professores = ler_json("professores")
        while True:
            print("\nInsira o código, nome completo e CPF a serem incluídos.")
            codprof = int(input("Código: "))
            nome = input("Nome completo: ")
            cpf = input("CPF: ")
            for i in professores:
                if i["codprof"] == codprof:
                    print("\n----- Código já cadastrado para outro professor -----")
                    incluir_professores()
            for i in professores:
                if i["cpf"] == cpf:
                    print("\n----- CPF já cadastrado para outro professor -----")
                    incluir_professores()
            dicio_professores = {"codprof": codprof, "nome": nome, "cpf": cpf}
            professores.append(dicio_professores)
            escrever_json(professores, "professores")
            print("\n----- Professor incluído com sucesso! -----")
            adicnovo(crud_professores, incluir_professores, "um novo professor")
    except ValueError:
        print("\n----- Valor inválido. Tente usar apenas números para código -----")
        incluir_professores()

# função listar professores
def listar_professores():
    professores = ler_json("professores")
    if len(professores) == 0:
        print("----- Não há professores cadastrados -----\n\n")
    else:
        print("----- PROFESSORES: LISTAR ----- \n")
        print("#  [Código] - [Nome] - [CPF]\n")
        for i in range(len(professores)):
            print(i+1, " ", '{:0>7}'.format(professores[i]["codprof"]), "-", professores[i]["nome"].title(), "-", professores[i]["cpf"])
        print("\n\n") 

# função alterar professores
def alterar_professores():
    try:
        professores = ler_json("professores")
        registro = int(input("\nDigite o código do professor que deseja alterar: "))
        registro_existente = False
        for i in professores: # comando para verificar se o código do professor existe
            if i["codprof"] == registro:
                registro_existente = True
        if registro_existente is False:
            print("\n\n----- Registro inexistente -----\n")
            inexistente(crud_professores, alterar_professores)
        else:
            try:
                for i in professores:
                    if i["codprof"] == registro: 
                        print("\nAlterar os dados de: Código:", i["codprof"], "- Nome:", i["nome"], "- CPF:", i["cpf"])
                        novo_codigo = int(input("Código: "))
                        novo_nome = input("Nome: ")
                        novo_cpf = input("CPF: ")
                        i["codprof"] = novo_codigo
                        i["nome"] = novo_nome
                        i["cpf"] = novo_cpf
                        escrever_json(professores, "professores")
                        print("\n----- Professor alterado com sucesso! -----")
                        registro_existente = True
            except ValueError:
                print("\n----- Valor inválido. Tente usar apenas números para código -----")
                alterar_professores()
    except ValueError:
        print("\n----- Valor inválido. Apenas números são aceitos -----")
        alterar_professores()

# função excluir professores
def excluir_professores():
    try:
        professores = ler_json("professores")
        registro = int(input("\nDigite o código do professor que deseja excluir: "))
        registro_existente = False
        for i in professores: # comando para verificar se o código do professor existe
            if i["codprof"] == registro:
                print("\nRemovendo do sistema: ", i["codprof"], "- Nome:", i["nome"], "- CPF:", i["cpf"])
                professores.remove(i)
                escrever_json(professores, "professores")
                print("\n----- Professor excluído com sucesso! -----")
                registro_existente = True
        if registro_existente is False:
            print("\n\n----- Registro inexistente -----\n")
            inexistente(crud_professores, excluir_professores)
    except ValueError:
        print("\n----- Valor inválido. Apenas números são aceitos -----")
        excluir_professores()


########## FUNÇÕES TURMAS #################################################################################

# função incluir turmas
def incluir_turmas():
    try:
        dicio_turmas = {}
        turmas = ler_json("turmas")
        professores = ler_json("professores")
        disciplinas = ler_json("disciplinas")
        novo_registro = False
        while True:
            print("\nInsira o código da turma, código do professor e código da disciplina a serem incluídos.")
            codturma = int(input("Código da turma: "))
            codprof = int(input("Código do professor: "))
            coddisc = int(input("Código da disciplina: "))
            for i in turmas:
                if i["codturma"] == codturma:
                    print("\n----- Código já cadastrado para outra turma -----")
                    incluir_turmas()
            for i in professores: # comando para verificar se código do professor existe
                if i["codprof"] == codprof:
                    for i in disciplinas: # comando para verificar se código da disciplina existe
                        if i["coddisc"] == coddisc:
                            novo_registro = True
            if novo_registro is False:
                print("\n---- Turma não pode ser cadastrada. Código(s) do professor e/ou da disciplina inválido(s) -----")
            else:
                dicio_turmas = {"codturma": codturma, "codprof": codprof, "coddisc": coddisc}
                turmas.append(dicio_turmas)
                escrever_json(turmas, "turmas")
                print("\n----- Turma incluída com sucesso! -----")        
            adicnovo(crud_turmas, incluir_turmas, "uma nova turma")
    except ValueError:
        print("\n----- Valor inválido. Tente usar apenas números -----")
        incluir_turmas()

# função listar turmas
def listar_turmas():
    turmas = ler_json("turmas")
    if len(turmas) == 0:
        print("----- Não há turmas cadastradas -----\n\n")
    else:
        print("----- TURMAS: LISTAR ----- \n")
        print("#  [Turma] - [Professor] - [Disciplina]\n")
        for i in range(len(turmas)):
            print(i+1, " ", '{:0>7}'.format(turmas[i]["codturma"]), "-", '{:0>7}'.format(turmas[i]["codprof"]), "-", '{:0>7}'.format(turmas[i]["coddisc"]))
        print("\n\n") 

# função alterar turmas
def alterar_turmas():
    try:
        turmas = ler_json("turmas")
        professores = ler_json("professores")
        disciplinas = ler_json("disciplinas")
        registro = int(input("\nDigite o código da turma que deseja alterar: "))
        registro_existente = False
        novo_registro = False
        for i in turmas: # comando para verificar se o código da turma existe
            if i["codturma"] == registro:
                registro_existente = True 
        if registro_existente is False:
            print("\n\n----- Registro inexistente -----\n")
            inexistente(crud_turmas, alterar_turmas)
        else:
            try:
                print("\nAlterar os dados de: Turma:", i["codturma"], "- Professor:", i["codprof"], "- Disciplina:", i["coddisc"])
                nova_turma = int(input("Código da turma: "))
                novo_professor = int(input("Código do professor: "))
                nova_disciplina = int(input("Código da disciplina: "))
                for i in professores: # comando para verificar se código do professor existe
                    if i["codprof"] == novo_professor:
                        for i in disciplinas: # comando para verificar se código da disciplina existe
                            if i["coddisc"] == nova_disciplina:
                                novo_registro = True
            except ValueError:
                print("\n----- Valor inválido. Tente usar apenas números -----")
                alterar_estudantes()
            if novo_registro is False:
                print("\n----- Turma não pode ser alterada. Código(s) do professor e/ou da disciplina inválido(s) -----")
            else:
                for i in turmas:
                    if i["codturma"] == registro:
                        i["codturma"] = nova_turma
                        i["codprof"] = novo_professor
                        i["coddisc"] = nova_disciplina
                        escrever_json(turmas, "turmas")
                        print("\n----- Turma alterada com sucesso! -----")
                        registro_existente = True
    except ValueError:
        print("\n----- Valor inválido. Apenas números são aceitos -----")
        alterar_turmas()

# função excluir turmas
def excluir_turmas():
    try:
        turmas = ler_json("turmas")
        registro = int(input("\nDigite o código da turma que deseja excluir: "))
        registro_existente = False
        for i in turmas: # comando para verificar se o código da turma existe
            if i["codturma"] == registro:
                print("\nRemovendo do sistema: Turma:", i["codturma"], "- Professor:", i["codprof"], "- Disciplina:", i["coddisc"])
                turmas.remove(i)
                escrever_json(turmas, "turmas")
                print("\n----- Turma excluída com sucesso -----")
                registro_existente = True
        if registro_existente is False:
            print("\n\n----- Registro inexistente -----\n")
            inexistente(crud_turmas, excluir_turmas)
    except ValueError:
        print("\n----- Valor inválido. Apenas números são aceitos -----")
        excluir_turmas()


########## FUNÇÕES MATRICULAS #################################################################################

# função incluir matriculas
def incluir_matriculas():
    try:
        matriculas = ler_json("matriculas")
        alunos = ler_json("estudantes")
        turmas = ler_json("turmas")
        dicio_matriculas = {}
        novo_registro = False
        while True:
            print("\nInsira o código da turma e o código do aluno a serem incluídos.")
            codturma = int(input("Código da turma: "))
            codaluno = int(input("Código do aluno: "))
            codmatricula = str(codturma) + "_" + str(codaluno)
            for i in matriculas: # comando para verificar se matrícula já existe no sistema
                if i["codmatricula"] == codmatricula:
                    print("\n----- Matrícula já existente -----")
                    crud_matriculas()
            for i in turmas: # comando para verificar se código da turma existe
                if i["codturma"] == codturma:
                    for i in alunos: # comando para verificar se código do aluno existe
                        if i["codaluno"] == codaluno:
                            novo_registro = True
            if novo_registro is False:
                print("----- Matrícula não pode ser cadastrada. Código(s) da turma e/ou do aluno inválido(s) -----")
            else:
                dicio_matriculas = {"codmatricula": codmatricula, "codturma": codturma, "codaluno": codaluno}
                matriculas.append(dicio_matriculas)
                escrever_json(matriculas, "matriculas")
                print("\n----- Matrícula incluída com sucesso! -----")
            adicnovo(crud_matriculas, incluir_matriculas, "uma nova matrícula")
    except ValueError:
        print("\n----- Valor inválido. Tente usar apenas números -----")
        incluir_matriculas()

# função listar matriculas
def listar_matriculas():
    matriculas = ler_json("matriculas")
    if len(matriculas) == 0:
        print("----- Não há matrículas cadastradas -----\n\n")
    else:
        print("----- MATRÍCULAS: LISTAR ----- \n")
        print("#  [Matrícula] - [Turma] - [Estudante]\n")
        for i in range(len(matriculas)):
            print(i+1, " ", '{:0>7}'.format(matriculas[i]["codmatricula"]), "-", '{:0>7}'.format(matriculas[i]["codturma"]), "-", '{:0>7}'.format(matriculas[i]["codaluno"]))
        print("\n\n") 

# função alterar matriculas
def alterar_matriculas():
    try:
        matriculas = ler_json("matriculas")
        alunos = ler_json("estudantes")
        turmas = ler_json("turmas")
        registro = input("\nDigite o código da matrícula que deseja alterar: ") # código de matrícula é string
        registro_existente = False
        novo_registro = False
        matricula_existente = False
        for i in matriculas: # comando para verificar se o código da matrícula existe
            if i["codmatricula"] == registro:
                print("\nAlterar os dados de: Turma:", i["codturma"], "- Estudante:", i["codaluno"])
                registro_existente = True
        if registro_existente is False:
            print("\n\n----- Registro inexistente -----\n")
            inexistente(crud_matriculas, alterar_matriculas)
        else:
            try:
                nova_turma = int(input("Código da turma: "))
                novo_aluno = int(input("Código do aluno: "))
                nova_matricula = str(nova_turma) + "_" + str(novo_aluno)
                for i in turmas: # comando para verificar se código da turma existe
                    if i["codturma"] == nova_turma:
                        for i in alunos: # comando para verificar se código do aluno existe
                            if i["codaluno"] == novo_aluno:
                                novo_registro = True
            except ValueError:
                print("\n----- Valor inválido. Tente usar apenas números -----")
                alterar_matriculas()
            if novo_registro is False:
                print("\n----- Matrícula não pode ser alterada. Código(s) da turma e/ou do aluno inválido(s) -----")
            else:
                for i in matriculas: # comando para verificar se matrícula já existe no sistema
                    if i["codmatricula"] == nova_matricula:
                        matricula_existente = True
                if matricula_existente is False:
                    for i in matriculas:
                        if i["codmatricula"] == registro:
                            i["codmatricula"] = nova_matricula
                            i["codturma"] = nova_turma
                            i["codaluno"] = novo_aluno
                            escrever_json(matriculas, "matriculas")
                            print("\n----- Matrícula alterada com sucesso! -----")
                            registro_existente = True
                else:
                    print("\n----- Matrícula já existente -----")
    except ValueError:
        print("\n----- Valor inválido. Apenas números são aceitos -----")
        alterar_matriculas()

# função excluir matriculas
def excluir_matriculas():
    try:
        matriculas = ler_json("matriculas")
        registro = input("\nDigite o código da matrícula que deseja excluir: ") # código de matrícula é string
        registro_existente = False
        for i in matriculas: # comando para verificar se o código da matrícula existe
            if i["codmatricula"] == registro:
                print("\nRemovendo do sistema: Matrícula:", i["codmatricula"], "Turma:", i["codturma"], "- Aluno:", i["codaluno"])
                matriculas.remove(i)
                escrever_json(matriculas, "matriculas")
                registro_existente = True
        if registro_existente is False:
            print("\n\n----- Registro inexistente -----\n")
            inexistente(crud_matriculas, excluir_matriculas)
    except ValueError:
        print("\n----- Valor inválido. Apenas números são aceitos -----")
        excluir_matriculas()


############### MENUS CRUD ##################################################################################

# função menu de ações com opções de listar, incluir, alterar e excluir
def crud(incluir, listar, alterar, excluir, TEMA):
    while True:
        try:
            print("Digite o número da ação desejada:\n\n1. Incluir\n2. Listar\n3. Alterar\n4. Excluir\n0. Retornar ao menu principal\n")
            acao = int(input("Opção escolhida: "))
            print("\n")
            if acao == 1: # comando para incluir dados
                print(f"----- {TEMA}: INCLUIR -----")
                incluir()
                print("\n")
            elif acao == 2: # comando para listar dados cadastrados
                listar()
            elif acao == 3: # comando para alterar dados cadastrados
                print(f"----- {TEMA}: ALTERAR -----")
                alterar()
                print("\n")
            elif acao == 4: # comando para excluir dados cadastrados
                print(f"----- {TEMA}: EXCLUIR -----")
                excluir()
                print("\n")
            elif acao == 0: # retorna ao menu principal
                print("Retornando ao menu principal...\n")
                gestao_dados()
        except ValueError:
            print("Opção inválida. Tente um número entre 1 e 4 ou 0 para sair do menu.\n\n")

def crud_estudantes(): # função menu gerenciar estudantes
    crud(incluir_estudantes, listar_estudantes, alterar_estudantes, excluir_estudantes, "ESTUDANTES")

def crud_disciplinas(): # função menu gerenciar disciplinas
    crud(incluir_disciplinas, listar_disciplinas, alterar_disciplinas, excluir_disciplinas, "DISCIPLINAS")

def crud_professores(): # função menu gerenciar professores
    crud(incluir_professores, listar_professores, alterar_professores, excluir_professores, "PROFESSORES")

def crud_turmas(): # função menu gerenciar turmas
    crud(incluir_turmas, listar_turmas, alterar_turmas, excluir_turmas, "TURMAS")

def crud_matriculas(): # função menu gerenciar matrículas
    crud(incluir_matriculas, listar_matriculas, alterar_matriculas, excluir_matriculas, "MATRÍCULAS")


################ MENU PRINCIPAL ##########################################################################################

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
                crud_disciplinas()
            elif opcao == 3:
                print("-"*10, "PROFESSORES", "-"*10,"\n")
                crud_professores()
            elif opcao == 4:
                print("-"*10, "TURMAS", "-"*10,"\n")
                crud_turmas()
            elif opcao == 5:
                print("-"*10, "MATRÍCULAS", "-"*10,"\n")
                crud_matriculas()
            elif opcao == 0:
                sair()
        except ValueError:
            print("Opção inválida. Digite uma opção de 1 a 5 ou 0 para sair do menu.\n\n")
gestao_dados()
