import os

#----------------------------------------------------CURSOS-----------------------------------------------------------------------------------

#dicCursos == CodCurso : [NomeCurso, Cidade, Nro_Vagas, Período ]

def existeCurso(chave, dic):
    if chave in dic:
        return True
    else:
        return False

def cadastrarCurso(dic):
    cod=input('Código do curso: ')
    chave=cod
    if not existeCurso(chave,dic):
        nome=input('Nome do curso: ')
        cidade=input('Cidade: ')
        numero=input('Número de vagas: ')
        periodo=input('Período (noturno/diurno/matutino): ')
        
        dados=[nome,cidade,numero,periodo]
        dic[chave]=dados

        print('Cadastro realizado com sucesso!')
    else:
        print('Curso já cadastrado!')

def alterarCurso(dic):
    cod=input('Código do curso que deseja alterar: ')
    chave=cod
    if existeCurso(chave,dic):
        nome=input('Nome do curso: ')
        cidade=input('Cidade: ')
        numero=input('Número de vagas: ')
        periodo=input('Período (noturno/diurno/matutino): ')
        
        dados=[nome,cidade,numero,periodo]
        dic[chave]=dados
        print('Alteração de dados concluída')
    else:
        print('Curso não cadastrado!')

def excluirCurso(dic):
    cod=input('Código do curso que deseja excluir: ')
    chave=cod
    if existeCurso(chave,dic):
        del dic[chave]
        print('Curso excluída com sucesso!')
    else:
        print('Curso não cadastrado! ')

def listarCurso(dic):
    cod=input('Código do curso que deseja listar dados: ')
    chave=cod
    if existeCurso(chave,dic):
        dados=dic[chave]
        print(f'Nome do curso: {dados[0]}')
        print(f'Cidade: {dados[1]}')
        print(f'Numero de vagas: {dados[2]}')
        print(f'Período: {dados[3]}')

def listarCursos(dic):
    for chave in dic:
        print(f'Codigo do curso: {chave}')
        dados=dic[chave]
        print(f'Nome do curso: {dados[0]}')
        print(f'Cidade: {dados[1]}')
        print(f'Numero de vagas: {dados[2]}')
        print(f'Período: {dados[3]}\n')

def gravaCurso(dic):
    arq=open('cursos.txt', 'w')

    for chave in dic:
        valor=dic[chave]
        cod=chave
        nome=valor[0] #nome composto
        cidade=valor[1] #nome composto
        vagas=valor[2]
        periodo=valor[3]

        #nomes compostos
        nome = nome.split() # cria uma lista
        nome = '-'.join(nome) #elementos da lista separados por - no arquivo

        cidade=cidade.split()
        cidade='-'.join(cidade)

        linha=cod+' \t '+nome+' \t '+cidade+' \t '+vagas+' \t '+periodo+'\n'
        arq.write(linha)
    arq.close()

def leCurso(dic):
    arq=open('cursos.txt', 'r')
    linha = arq.readline() # le a primeira linha
    while linha:
        chave = linha.split() #separa a linha em uma lista
        cod=chave[0]
        nome=chave[1] #nome composto
        cidade=chave[2] #nome composto
        curso=chave[3]
        periodo=chave[4]

        #nomes compostos
        nome=nome.split('-') # cria uma lista
        nome=' '.join(nome) #separa a lista com espaço

        cidade=cidade.split('-')
        cidade=' '.join(cidade)
      
        chave = cod
        dados = [nome,cidade,curso,periodo]

        dic[chave]=dados

        linha = arq.readline() #proxima linha
    arq.close()


#---------------------------------------------------ALUNOS-----------------------------------------------------------------------------------       

#dicAlunos == CPF : ( Nome, Endereço, DataNascimento, Sexo, [E-mails], [Telefones] )

def existeAluno(chave, dic):
    if chave in dic:
        return True
    else:
        return False

def cadastrarAluno(dic):
    cpf=input('CPF do aluno: ')
    chave=cpf
    if not existeAluno(chave,dic):
        nome=input('Nome: ')
        endereço=input('Endereço: ')
        data=input('Data de Nascimento (dd/mm/aaaa): ')
        sexo=input('sexo : ')

        email=input('Email: ')
        emails=[]
        while email!='': 
            emails.append(email)
            email=input('Proximo email: ')
        
        tel=input('Telefone: (sem espaço ou traços)')
        tels=[]
        while tel!='':
            tels.append(tel)
            tel=input('Proximo telefone: (sem espaço ou traços)')
        
        dados=(nome,endereço,data,sexo,emails,tels)
        dic[chave]=dados

        print('Cadastro realizado com sucesso!')
    else:
        print('Aluno já cadastrado!')

def alterarAluno(dic):
    cpf=input('CPF do aluno que deseja alterar: ')
    chave=cpf
    if existeAluno(chave,dic):
        nome=input('Nome: ')
        endereço=input('Endereço: ')
        data=input('Data de Nascimento (dd/mm/aaaa): ')
        sexo=input('sexo: ')

        email=input('Email: ')
        emails=[]
        while email!='': 
            emails.append(email)
            email=input('Proximo email: ')

        tel=input('Telefone: (sem espaço ou traços)')
        tels=[]
        while tel!='':
            tels.append(tel)
            tel=input('Proximo telefone: (sem espaço ou traços)')
        
        dados=(nome,endereço,data,sexo,emails,tels)
        dic[chave]=dados
        print('Aluno atualizado com sucesso!')
    else:
        print('Aluno não cadastrado!')

def excluirAluno(dic):
    cpf=input('CPF do aluno que deseja excluir: ')
    chave=cpf
    if existeAluno(chave,dic):
        del dic[chave]
        print('Aluno excluído com sucesso!')
    else:
        print('Aluno não cadastrado! ')

def listarAluno(dic):
    cpf=input('CPF do aluno que deseja listar dados: ')
    chave=cpf
    if existeAluno(chave,dic):
        dados=dic[chave]
        print(f'Nome do aluno: {dados[0]}')
        print(f'Endereço: {dados[1]}')
        print(f'Data de nascimento: {dados[2]}')
        print(f'Sexo: {dados[3]}')
        emails=', '.join(dados[4]) #separa os valores da lista com ,
        print(f'Emails: {emails}') 
        tels=', '.join(dados[5])
        print(f'Telefones: {tels}')

def listarAlunos(dic):
    for chave in dic:
        print(f'CPF do aluno: {chave}')
        dados=dic[chave]
        print(f'Nome do aluno: {dados[0]}')
        print(f'Endereço: {dados[1]}')
        print(f'Data de nascimento: {dados[2]}')
        print(f'Sexo: {dados[3]}')
        emails=', '.join(dados[4]) #separa os valores da lista com ,
        print(f'Emails: {emails}')
        tels=', '.join(dados[5])
        print(f'Telefones: {tels}')

def gravaAluno(dic):
    arq=open('alunos.txt', 'w')

    for chave in dic:
        valor=list(dic[chave]) 

        cpf=chave
        nome=valor[0] #nome composto
        endereço=valor[1] #nome composto
        data=valor[2]
        sexo=valor[3]
        email=valor[4] #lista
        tel=valor[5]  #lista

        #nomes compostos
        nome = nome.split() # cria uma lista
        nome = '-'.join(nome)  #elementos da lista separados por -

        endereço = endereço.split() # cria uma lista
        endereço = '-'.join(endereço)  #elementos da lista separados por - no arquivo
        
        #listas
        email=','.join(email)  #elementos da lista separados por , no arquivo
        tel=','.join(tel)  #elementos da lista separados por , no arquivo

        linha=cpf+' \t '+nome+' \t '+endereço+' \t '+data+' \t '+sexo+'\t '+email+' \t '+ tel+ '\n'
        arq.write(linha)
    arq.close()

def leAluno(dic):
    arq=open('alunos.txt', 'r')
    linha = arq.readline()
    while linha:
        chave = linha.split() #separa a linha em uma lista
        cpf=chave[0]
        nome=chave[1] #nome composto
        endereço=chave[2] #nomecomposto
        data=chave[3]
        sexo=chave[4]
        email=chave[5] #lista
        tel=chave[6] #lista
        
        #nomes compostos
        nome=nome.split('-') # cria uma lista
        nome=' '.join(nome) #separa a lista com espaço

        endereço=endereço.split('-') # cria uma lista
        endereço=' '.join(endereço) #separa a lista com espaço

        #listas
        email = email.split(',') #separa os elementos pela , e colocam em uma lista
        tel = tel.split(',') 

        chave = cpf
        dados = (nome,endereço, data,sexo,email,tel)

        dic[chave]=dados

        linha = arq.readline() #proxima linha
    arq.close()


#------------------------------------------------MATRICULAS------------------------------------------------------------------------------------

#dicmatriculas == (CodCurso, CPF) : [ Data_Matrícula, Bimestre, [Disciplina1, Disciplina2, ....,Disciplina3] ]

def existeMatricula(chave,dic):
    if chave in dic:
        return True
    else:
        return False

def cadastrarMatricula(dic):
    cpf=input('CPF do aluno:')
    cod=input('Codigo do curso: ')
    chave=(cpf,cod)

    if not existeMatricula(chave,dic):
        matricula=input('Data matricula (dd/mm/aaaa): ')
        bimestre=input('Bimestre (escreva por extenso): ')
        
        diciplina=input('Diciplina: ')
        diciplinas=[]
        while diciplina!='':
            diciplinas.append(diciplina)
            diciplina=input('Outra diciplina: ')

        dados=[matricula,bimestre,diciplinas]
        dic[chave]=dados
        print('Cadastrado com sucesso!')
    else:
        print('Dados já cadastrados!')

def alterarMatricula(dic):

    cpf=input('CPF do aluno:')
    cod=input('Codigo do curso: ')
    chave=(cpf,cod)
    if existeMatricula(chave,dic):
        matricula=input('Data matrícula (dd/mm/aaaa): ')
        bimestre=input('Bimestre (escreva por extenso): ')
        
        diciplina=input('Diciplina: ')
        diciplinas=[]
        while diciplina!='':
            diciplinas.append(diciplina)
            diciplina=input('Outra diciplina: ')

        dados=[matricula,bimestre,diciplinas]
        dic[chave]=dados
        print('Alteração realizada com sucesso!')
    else:
        print('Dados não cadastrados!')

def excluirMatricula(dic):
    cpf=input('CPF do aluno:')
    cod=input('Codigo do curso: ')
    chave=(cpf,cod)
    if existeMatricula(chave,dic):
        del dic[chave]
        print('Matrícula excluída com sucesso!')
    else:
        print('Dados não cadastrados! ')

def listarMatricula(dic):
    cpf=input('CPF do aluno:')
    cod=input('Codigo do curso: ')
    chave=(cpf,cod)
    if existeMatricula(chave,dic):
        dados=dic[chave]
        print(f'Data da matrícula: {dados[0]}')
        print(f'Bimestre: {dados[1]}')
        diciplinas=', '.join(dados[2]) #separa os valores da lista com ,
        print(f'Diciplinas: {diciplinas}')
    else:
        print('Matéria não cadastrada!')

def listarMatriculas(dic):
    for chave in dic:
        print(f'CPF do aluno: {chave[0]}')
        print(f'Codigo do curso: {chave[1]} ')
        dados=dic[chave]
        print(f'Data da matrícula: {dados[0]}')
        print(f'Bimestre: {dados[1]}')
        diciplinas=', '.join(dados[2]) #separa os valores da lista com ,
        print(f'Diciplinas: {diciplinas}\n')

def gravaMatricula(dic):
    arq=open('matriculas.txt', 'w')

    for chave in dic:
        valor=list(dic[chave]) 

        cpf=chave[0]
        cod=chave[1]
        data=valor[0]
        bimestre=valor[1]
        diciplinas=valor[2] #lista

        #listas
        diciplinas=','.join(diciplinas)  #elementos da lista separados por , no arquivo

        linha=cpf+' \t '+cod+' \t '+data+' \t '+bimestre+' \t '+diciplinas+ '\n'
        arq.write(linha)
    arq.close()

def leMatricula(dic):
    arq=open('matriculas.txt', 'r')
    linha = arq.readline()
    while linha:
        chave = linha.split() #separa a linha em uma lista

        cpf=chave[0]
        cod=chave[1]
        data=chave[2]
        bimestre=chave[3]
        diciplinas=chave[4] #lista

        #listas
        diciplinas = diciplinas.split(',') #separa os elementos pela , e colocam em uma lista
    
        chave = (cpf,cod)
        dados = [data,bimestre,diciplinas]

        dic[chave]=dados

        linha = arq.readline() #proxima linha
    arq.close()

#-----------------------------------------------RELATORIOS-------------------------------------------------------------

def relatorio1(dicAluno): #dicAluno
    x=input('Informe o nome do aluno desejado: \n')

    for chave in dicAluno:
        dados=dicAluno[chave]
        if (dados[0]).upper() == x.upper():
            print(f'Nome do aluno: {dados[0]}')
            print(f'Endereço: {dados[1]}')
            print(f'Data de nascimento: {dados[2]}')
            print(f'Sexo: {dados[3]}')
            emails=', '.join(dados[4]) #separa os valores da lista com ,
            print(f'Emails: {emails}')
            tels=', '.join(dados[5])
            print(f'Telefones: {tels}\n')

def relatorio2(dicCurso): #dicionario de cursos
    x=input('Periodo desejado: ')
    y=int(input('Quantidades de vagas desejadas: \n'))
    
    for chave in dicCurso: 
        dados=dicCurso[chave]
        if dados[3] == x and int(dados[2])>y: #se o numero de vagas (dados[2]) == y e o periodo desejado (dados[3]) == x
            print(f'CODIGO DO CURSO: {chave}')
            print(f'NOME: {dados[0]}')
            print(f'CIDADE: {dados[1]}')
            print(f'NUMERO DE VAGAS: {dados[2]}')
            print(f'PERÍODO: {dados[3]}\n')

def relatorio3(dicCurso,dicAluno,dicMatricula):
    x=input('Informe o nome do aluno desejado: ')   

    #Se o cpf do aluno estiver matriculado com algum curso no dicMatriculas informa os dados
    for chave in dicMatricula:
        #cpf do aluno
        cpfAluno=''
        for chaveAluno in dicAluno:
            dados=dicAluno[chaveAluno]
            for i in dados:
                if i == x:
                    cpfAluno=str(chaveAluno)


        #codigo do curso
        codCurso=''
        for chaveCurso in dicCurso: #para cadas chave do dic cursos
            if chaveCurso == chave[1] : #se a chave do curso == codigo do curso no dic matriculas
                codCurso=chave[1]

        if (cpfAluno,codCurso) == chave:

            if cpfAluno==chave[0]:
                print('\n------------------------------------')
                dados=dicAluno[chave[0]]
                print(f'Nome do aluno: {dados[0]}')
                print(f'Endereço: {dados[1]}')
                print(f'Data de nascimento: {dados[2]}')
                print(f'Sexo: {dados[3]}')
                emails=', '.join(dados[4]) #separa os valores da lista com ,
                print(f'Emails: {emails}')
                tels=', '.join(dados[5])
                print(f'Telefones: {tels}\n')

                dados=dicMatricula[chave]
                print(f'Data da matrícula: {dados[0]}')
                print(f'Bimestre: {dados[1]}')
                diciplinas=', '.join(dados[2]) #separa os valores da lista com ,
                print(f'Diciplinas: {diciplinas}\n')
                
                for chave in dicCurso:
                    if codCurso==chave:
                        dados=dicCurso[chave]
                        print(f'Nome do curso: {dados[0]}')
                        print(f'Cidade: {dados[1]}')
                        print(f'Numero de vagas: {dados[2]}')
                        print(f'Período: {dados[3]}\n')
    
    else:
        print('Matriculas não cadastradas para esse aluno')

def relatorio4(dicCurso,dicAluno,dicMatricula):

    maior=0
    for chave in dicMatricula:
        dados=dicMatricula[chave]
        if len(dados[2])>maior: 
            maior=len(dados[2])

    for chave in dicMatricula:
        dados=dicMatricula[chave]
        if len(dados[2])==maior:

            #cpf do aluno
            for chaveAluno in dicAluno:
                if chaveAluno == chave[0]:
                    print('---------------------------------------\n')
                    dados=dicAluno[chaveAluno]
                    print(f'Nome do aluno: {dados[0]}')
                    print(f'Endereço: {dados[1]}')
                    print(f'Data de nascimento: {dados[2]}')
                    print(f'Sexo: {dados[3]}')
                    emails=', '.join(dados[4]) #separa os valores da lista com ,
                    print(f'Emails: {emails}')
                    tels=', '.join(dados[5])
                    print(f'Telefones: {tels}\n')

            for chaveCurso in dicCurso:
                if chaveCurso==chave[1]:
                    dados=dicCurso[chaveCurso]
                    print(f'Nome do curso: {dados[0]}')
                    print(f'Cidade: {dados[1]}')
                    print(f'Numero de vagas: {dados[2]}')
                    print(f'Período: {dados[3]}\n')

#-----------------------------------------------MENU-------------------------------------------------------------------

def existeArquivo(arq):
    if os.path.exists(arq):
        return True
    else:
        return False

def menuRelatorio():
    print('1 - Mostrar os dados de um aluno a partir de um nome informado pelo usuário. ')
    print('2 - Mostrar os dados dos cursos que são oferecidos em determinado período (informado pelou suário) e que ofereçam uma quantidade de vagas maior do que informada uma quantidade informada pelo usuário. ')
    print('3 - Mostrar todas as matriculas já realizadas, todos os dados do curso e todos os dados do aluno, a partir do nome de um aluno informado pelo usuário.  ')
    print('4 - Mostrar na tela todos os dados do aluno e do respectivo curso para aqueles alunos que possuem maior quantidade de disciplinas em sua matrícula. ')

def menu():
    print('1 - Cursos')
    print('2 - Alunos')
    print('3 - Matrículas')
    print('4 - Relatórios')
    print('5 - Sair\n')

def submenu():
    print('1 - Cadastrar')
    print('2 - Alterar dados')
    print('3 - Excluir')
    print('4 - Listar Um')
    print('5 - Listar Todos\n')

def main():

    #declarar dicionarios
    dicCurso = {}
    dicAluno = {}
    dicMatricula = {}

    # Verificar arquivos
    if existeArquivo('cursos.txt'):
        leCurso(dicCurso)
    if existeArquivo('alunos.txt'):
        leAluno(dicAluno)
    if existeArquivo('matriculas.txt'):
        leMatricula(dicMatricula)
      
    roda = True
    while roda:
        menu()
        op1 = int(input('Escolha uma opção: '))

        #submenu de cursos
        if op1 == 1:
            submenu()
            op2 = int(input('Escolha uma opção: '))
            if op2 == 1:
                cadastrarCurso(dicCurso)
            elif op2 == 2:
                alterarCurso(dicCurso)
            elif op2 == 3:
                excluirCurso(dicCurso)
            elif op2 == 4:
                listarCurso(dicCurso)
            elif op2 == 5:
                listarCursos(dicCurso) 

        #submenu de alunos
        if op1 == 2:
            submenu()
            op2 = int(input('Escolha uma opção: '))
            if op2 == 1:
                cadastrarAluno(dicAluno)
            elif op2 == 2:
                alterarAluno(dicAluno)
            elif op2 == 3:
                excluirAluno(dicAluno)
            elif op2 == 4:
                listarAluno(dicAluno)
            elif op2 == 5:
                listarAlunos(dicAluno)
        
        #submenu de matriculas
        if op1 == 3:
            submenu()
            op2 = int(input('Escolha uma opção: '))
            if op2 == 1:
                cadastrarMatricula(dicMatricula)
            elif op2 == 2:
                alterarMatricula(dicMatricula)
            elif op2 == 3:
                excluirMatricula(dicMatricula)
            elif op2 == 4:
                listarMatricula(dicMatricula)
            elif op2 == 5:
                listarMatriculas(dicMatricula)

        #submenu de relatorios
        if op1 == 4:
            menuRelatorio()
            op2 = int(input('Escolha uma opção: '))
            if op2 == 1:
                relatorio1(dicAluno)
            if op2 == 2:
                relatorio2(dicCurso)
            if op2 == 3:
                relatorio3(dicCurso,dicAluno,dicMatricula)
            if op2 == 4:
                relatorio4(dicCurso,dicAluno,dicMatricula)
            
        if op1 == 5:
            gravaCurso(dicCurso)
            gravaAluno(dicAluno)
            gravaMatricula(dicMatricula)
            roda = False

main()