def calcular_media():
    notas = []
    while True:
        try:
            nota = float(input("Digite a nota do aluno (ou -1 para encerrar): "))
            if nota == -1:
                break
            elif 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Por favor, insira uma nota válida entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Insira um número válido.")
    
    if notas:
        media = sum(notas) / len(notas)
        print(f"A média das notas é: {media:.2f}")
    else:
        print("Nenhuma nota foi inserida.")

# Executa o programa
calcular_media()
