#!/usr/bin/env python3

# Inicializando as variáveis
total = 0
contador_notas = 0

# Enquanto o contador de notas for menor que 10
while contador_notas < 10:
    try:
        # Solicita a entrada da nota
        nota = float(input(f"Digite a nota {contador_notas + 1}: "))
        
        # Verifica se a nota está dentro do intervalo esperado
        if 0 <= nota <= 10:
            total += nota
            contador_notas += 1
        else:
            print("Nota inválida! A nota deve ser entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

# Calculando a média
media = total / 10

# Exibindo o resultado
print(f"A média da disciplina é: {media}")

