def adicionar_aluno(alunos):

  nome = input("Digite o nome do aluno: ")
  matricula = input("Digite o número de matrícula do aluno: ")
  alunos[matricula] = nome
  print("Aluno adicionado com sucesso!")

def remover_aluno(alunos):

  matricula = input("Digite o número de matrícula do aluno a ser removido: ")
  if matricula in alunos:
    del alunos[matricula]
    print("Aluno removido com sucesso!")
  else:
    print("Número de matrícula não encontrado.")

def atualizar_aluno(alunos):

  matricula = input("Digite o número de matrícula do aluno a ser atualizado: ")
  if matricula in alunos:
    novo_nome = input("Digite o novo nome do aluno: ")
    alunos[matricula] = novo_nome
    print("Nome do aluno atualizado com sucesso!")
  else:
    print("Número de matrícula não encontrado.")

def ver_alunos(alunos):

  if alunos:
    print("Alunos cadastrados:")
    for matricula, nome in alunos.items():
      print(f"Matrícula: {matricula}, Nome: {nome}")
  else:
    print("Não há alunos cadastrados.")
