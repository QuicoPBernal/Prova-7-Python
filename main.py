import alunos

def main():

  alunos_dict = {} 
  while True:
    print("\nMenu:")
    print("1. Adicionar aluno")
    print("2. Remover aluno")
    print("3. Atualizar aluno")
    print("4. Ver alunos")
    print("5. Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
      alunos.adicionar_aluno(alunos_dict)
    elif opcao == '2':
      alunos.remover_aluno(alunos_dict)
    elif opcao == '3':
      alunos.atualizar_aluno(alunos_dict)
    elif opcao == '4':
      alunos.ver_alunos(alunos_dict)
    elif opcao == '5':
      print("Saindo do programa...")
      break
    else:
      print("Opção inválida!")

if __name__ == "__main__":
  main()
