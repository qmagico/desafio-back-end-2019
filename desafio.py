# Checa se indice j está entre os caracteres que compoem a piramide
def between(n, j, cont):
    return n / 2 - 1 - cont <= j <= n / 2 + cont


# Pega o caractere correspondente ao indice j
def check_between(n, j, cont):
    if between(n * 2 - 1, j, cont):
        return "*"
    else:
        return "_"


# Retorna o desenho da piramide
def get_pyramid(n):
    cont = 0
    lines = []

    for i in range(n):
        string = ""
        for j in range(n * 2 - 1):
            string += check_between(n, j, cont)

        cont += 1
        lines.append(string)

    return lines


# Desenha a piramide
def draw_pyramid(n):
    print('\n'.join(get_pyramid(n)))


num_lines = int(input())

draw_pyramid(num_lines)
