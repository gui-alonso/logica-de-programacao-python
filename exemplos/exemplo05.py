"""
Escreva um programa que receba uma letra do alfabeto e determine se é uma vogal ou uma consoante.
"""
letra = input("Digite uma letra: ").lower()

if letra in 'aeiou':
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")
