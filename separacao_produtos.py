print("Digite os Id's dos produtos: \n")

id_produto = []
doces = []  # Produtos com ID's pares
amargos = []  # Produtos com ID's impares

while len(id_produto) != 10:  # Quando a quantidade de elementos em id_produtos for igual a 10, encerra
    # A cada repetição adiciona (append) o Id a lista (id_produtos)
    id_produto.append(int(input("Digite o ID: ")))

for i in id_produto:
    # Itera sobre todos elementos adicionados a lista id_produtos
    if i % 2 == 0:
        # Caso o resto da divisão por 2 seja 0, significa ser par.
        doces.append(i)
    else:
        amargos.append(i)

print("\n", "="*30, "\n")
print(f"{len(doces)} Produtos doces: {doces}")
print(f"{len(amargos)} Produtos amargos: {amargos}")
