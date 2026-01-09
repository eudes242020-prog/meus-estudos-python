alunos=[]
def cadastrar_aluno(alunos):
    print('Cadastro de aluno!')
    aluno=input('Informe o nome do aluno: ').strip().capitalize()
    novo_aluno={"nome": aluno, "notas": []}
    alunos.append(novo_aluno)
def adicionar_nota(alunos):
    print('Adicionando nota para o aluno')
    aluno=input('Informe o aluno que deseja adiciona uma nota: ').strip().capitalize()
    encontrado = False
    try:
        nota=float(input('Informe a nota do aluno: '))
        if nota < 0 or nota > 10:
            print("Notas somente possíveis de 0 a 10")
            return
    except ValueError:
        print('Nota precisa ser um número') 
        return    
    for nome in alunos:
        if nome['nome'] == aluno:
            encontrado = True
            nome['notas'].append(nota) 
    if not encontrado:
        print("Aluno não cadastrado")
def media_aluno(alunos):
    aluno=input('Informe o nome do aluno: ')
    encontrado = False
    for nome in alunos:
        if aluno == nome['nome']:
            encontrado = True
        if len(nome['notas'])==0:
            print('Aluno não possui nota')
            return
        media=sum(nome['notas'])/len(nome['notas'])   
        print(f"A media do aluno é {media}")
        break
    if encontrado==False:
        print('Aluno não encontrado')
def aprovaos_reprovados(alunos):
    aprovados=[]
    reprovados=[]
    
    for aluno in alunos:
        if len(aluno['notas'])==0:
            continue
        media=sum(aluno['notas'])/len(aluno['notas'])
        aluno_com_media = aluno.copy()
        aluno_com_media['media'] = media
        if media >=7:
            aprovados.append(aluno_com_media)
        else:
            reprovados.append(aluno_com_media)
    print("\n--- Alunos Aprovados ---")
    for aprovado in aprovados:
        print(f"Nome do aluno:{aprovado['nome']} | média {aprovado['media']:.2f}")
    print("\n--- Alunos Reprovados ---")
    for reprovado in reprovados:
        print(f"Nome do aluno {reprovado['nome']} | média {reprovado['media']:.2f}")
