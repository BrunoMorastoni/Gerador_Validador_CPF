

def gerar_cpf():
    pass 


def validar_ultimos_digitos(nove_primeiros_digitos,segundo_digito=False,primeiro_digito=0) -> int:
    
    lista_valores_multiplicados = []
    
    if segundo_digito:
        nove_primeiros_digitos.append(primeiro_digito)

    indice_numeros = 0
    numero_multiplicador = 11 if not segundo_digito else 12
    for x in reversed(range(2,numero_multiplicador)):
        lista_valores_multiplicados.append(x * nove_primeiros_digitos[indice_numeros])

        indice_numeros += 1
    
    soma_valores_resultado = sum(lista_valores_multiplicados) * 10 % 11


    if soma_valores_resultado > 9:
        soma_valores_resultado = 0
    
    
    return soma_valores_resultado


def validar_cpf(cpf):
    if cpf:
        cpf_dividido = cpf.split("-")

        nove_primeiros_digitos = [int(n) for n in cpf_dividido[0] if n != "."]
        numeros_validadores = cpf_dividido[1]

        
        primeiro_digito_validado = validar_ultimos_digitos(nove_primeiros_digitos)
        segundo_digito_validado = validar_ultimos_digitos(nove_primeiros_digitos,True,primeiro_digito_validado)

        NUMEROS_VALIDADOS_IGUAL_NUMEROS_CPF = primeiro_digito_validado == int(numeros_validadores[0]) and segundo_digito_validado == int(numeros_validadores[1])


        if NUMEROS_VALIDADOS_IGUAL_NUMEROS_CPF:
            return f"{cpf} | VALIDO!"
        
        return f"{cpf} | NÃO é VALIDO!!"
    else:
        return "CPF INVALIDO!"

def main():
    print(validar_cpf("")) # 720.812.670-47


if __name__ == "__main__":
    main()

"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""


