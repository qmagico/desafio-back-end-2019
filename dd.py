def piramide(n):
    underscore, asterisco = '_,*'.split(",")
    ast = 1

    for i in range(n+1):
        print(underscore * int(n-i) + asterisco * (ast) + underscore * int(n-i))
        ast+=2


piramide(6)