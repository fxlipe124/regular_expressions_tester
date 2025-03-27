import re

def teste_expressao():
    print("Digite a Expressão Regular (ex.: '1(0|1)*00' começam com 1 e terminam com 00 ou 'b*ab*ab*ab*' testa cadeias com exatamente 3 'a'):")
    entrada = input("Expressão: ")

    try:
        padrao = re.compile(f"^{entrada}$")
    except re.error as e:
        print(f"Erro na expressão regular: {e}")
        return

    print("Digite as cadeias para testar (uma por linha). Digite 'FIM' para encerrar:")
    teste_strings = []
    while True:
        string = input("Cadeia: ")
        if string.upper() == "FIM":
            break
        teste_strings.append(string)

    print("Resultados:")
    for s in teste_strings:
        if padrao.match(s):
            print(f"'{s}' -> ACEITA")
        else:
            print(f"'{s}' -> REJEITADA")

if __name__ == "__main__":
    print("Testador de Expressões Regulares")
    teste_expressao()