# src/calculadora.py

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

if __name__ == "__main__":
    print("Bem-vindo à Calculadora!")
    print("1: Somar")
    print("2: Subtrair")
    print("3: Multiplicar")
    print("4: Dividir")
    
    operacao = input("Escolha a operação (1/2/3/4): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if operacao == '1':
        print(f"O resultado é: {somar(num1, num2)}")
    elif operacao == '2':
        print(f"O resultado é: {subtrair(num1, num2)}")
    elif operacao == '3':
        print(f"O resultado é: {multiplicar(num1, num2)}")
    elif operacao == '4':
        try:
            print(f"O resultado é: {dividir(num1, num2)}")
        except ValueError as e:
            print(e)
    else:
        print("Operação inválida.")
