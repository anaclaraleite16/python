preco= float(input("digite o preco"))
codigo = int(input("digite 1,2,3 ou 4"))
if codigo == 1:
    valor_pago = preco - (preco * 0.10)
    print(valor_pago)
elif codigo == 2:
    valor_pago = preco - (preco * 0.15)
    print(valor_pago)
elif codigo == 3:
    valor_pago = preco 
    print(valor_pago)
elif codigo == 4:
    valor_pago = preco + (preco * 0.10)
    print(valor_pago)
else:
    print("codigo invalido, use 1,2,3 ou 4")

