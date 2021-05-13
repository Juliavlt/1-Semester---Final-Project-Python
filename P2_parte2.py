#dicCursos == CodCurso : [NomeCurso, Cidade, Nro_Vagas, Período ]
#dicAlunos == CPF : ( Nome, Endereço, DataNascimento, Sexo, [E-mails], [Telefones] )
#dicmatriculas == (CodCurso, CPF) : [ Data_Matrícula, Bimestre, [Disciplina1, Disciplina2, ....,Disciplina3] ]

# Mostrar na tela todos os dados do aluno e do respectivo curso para aqueles alunos que
#possuem maior quantidade de disciplinas em sua matrícula. 

dicCurso={'1':['ads', 'são-carlos', '40', 'noturno'], '2':['agronomia', 'barretos', '35', 'matutino'], '3':['letras', 'limeira', '30', 'noturno']}
dicAluno={'12': ('julia', 'rua-antonio-de-almeida-leite', '10/05/2001', 'feminino', ['julia@hotmail.com,valente@hotamil.com'], ['996161005']), '23': ('pedro', 'rua-visconde-dos-santos', '10/04/2001', 'masculino', ['pedrolucas@hotmail.com'], ['996129987,88877776']), '34': ('leo', 'rua-laranjeiras-dos-pinhais', '21/03/1999', 'masculino', ['leonardo@hotmail.com'], ['123456789,987654321'])}
dicMatricula={('12', '1'): ['01/06/2018', 'segundo', ['ap1,adm']], ('23', '2'): ['01/01/2017', 'terceiro', ['bio,mat']], ('34', '3'): ['01/06/2018', 'segundo', ['adm,mat']]}

def relatorio4(dicCurso,dicAluno,dicMatricula):
    #cpf do aluno
    cpfAluno=''
    for chave in dicAluno:
        dados=dicAluno[chave]
        for i in dados:
            cpfAluno=str(chave)

    #Se o cpf do aluno estiver matriculado com algum curso no dicMatriculas informa os dados
    for chave in dicMatricula:
        codCurso=''
        for chaveCurso in dicCurso: #para cadas chave do dic cursos
            if chaveCurso == chave[1] : #se a chave do curso == codigo do curso no dic matriculas
                codCurso=chave[1]
                if (cpfAluno,codCurso) == chave: #se o cod curso e cpf do aluno == chave do dic matricula
                    for chave in dicMatricula:
                        dados=dicMatricula[chave] #pego os dados da matricula
                        maior=0
                        cont=1 
                        for dado in dados[2]:
                            for i in dado:
                                if i == ',':
                                    cont+=1 #como o cont começa com 1, o cont vai contar a quantidade de materias
                        print(cont)




relatorio4(dicCurso,dicAluno,dicMatricula)