def divisores():
    resultado = {}
    try:
        with open("numeros.txt", "r") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha.isdigit():
                    numero = int(linha)
                    divisores = [i for i in range(1, numero) if numero % i == 0]
                    resultado[numero] = divisores
    except FileNotFoundError:
        print("Arquivo 'numeros.txt' não encontrado.")
    return resultado
