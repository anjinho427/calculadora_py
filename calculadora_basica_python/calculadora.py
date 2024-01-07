def calculadora():
    print("Calculadora ")
   

    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            operacao = input("Digite a operação (+, -, *, /): ")
            num2 = float(input("Digite o segundo número: "))

            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                resultado = num1 / num2
            else:
                print("Operação inválida. Tente novamente.")
                continue

            print("Resultado: ", resultado)

            continuar = input("Deseja fazer outra operação? (s/n): ")
            if continuar.lower() != 's':
                break

        except ValueError:
            print("Entrada inválida. Certifique-se de inserir números corretamente.")

if __name__ == "__main__":
    calculadora()
1