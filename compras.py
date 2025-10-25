total = 0
dic = {
    input("Digite o nome do primeiro produto: "):float(input("Digite o valor do primeiro produto: ")),
    input("Digite o nome do segundo produto: "):float(input("Digite o valor do segundo produto: ")),
    input("Digite o nome do terceiro produto: "):float(input("Digite o valor do terceiro produto: ")),
    input("Digite o nome do quarto produto: "):float(input("Digite o valor do quarto produto: ")),
    input("Digite o nome do quinto produto: "):float(input("Digite o valor do quinto produto: "))
}
for item, preco in dic.items():
    total += preco
print(f"O valor total de sua compra foi de {total} reais.")