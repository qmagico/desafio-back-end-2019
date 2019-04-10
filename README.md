under,star,contStar = "_","*",1
n = int(input("Entre com um número mágico: "))
contUnder = n - 1
for k in range(n):
    print(under * contUnder + star * contStar + under * contUnder)
    contStar += 2
    contUnder -=1
