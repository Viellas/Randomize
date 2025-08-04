import random

print("Bem-vindo ao jogo da sorte do arthuzinho")
print("Regra: Se você escolher o mesmo número que o computador, você perde. Se for diferente, você ganha.")

# Computador randomiza um número
numero_computador = random.randint(1, 5)

# Usuário escolhe um número 
numero_usuario = int(input("Escolha um número entre 1 e 5: "))

# Verifica se o número é válido
if numero_usuario < 1 or numero_usuario > 5:
    print("Número inválido! Escolha entre 1 e 5.")
else:
    print(f"O computador escolheu: {numero_computador}")
    if numero_usuario == numero_computador:
        print("Perdeu bobão")
    else:
        print("Ganhar é mole, quero ver perder")
