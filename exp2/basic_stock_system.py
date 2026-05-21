estoque = {
    "teclado":   {"quantidade": 15, "preco": 250.00},
    "mouse":     {"quantidade": 20, "preco": 120.00},
    "monitor":   {"quantidade": 8,  "preco": 1500.00},
    "headset":   {"quantidade": 12, "preco": 350.00},
    "webcam":    {"quantidade": 6,  "preco": 480.00},
    "pendrive":  {"quantidade": 25, "preco": 75.00}
}

while True:
    print("\n=== MENU ===")
    print("1. Ver estoque")
    print("2. Sair")
    print("3. Entrada de produto")
    print("4. Saída de produto")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("=== ESTOQUE ATUAL ===")
        for produto, dados in estoque.items():
            print(f"{produto} - Qtd: {dados['quantidade']} - R$ {dados['preco']:.2f}")
    elif opcao == "2":
        print("Encerrando...")
        break
    elif opcao == "3":
        novo_produto = input("Qual produto? ")
        nova_unidade = int(input("Quantas unidades? "))
        if novo_produto in estoque:
            estoque[novo_produto]['quantidade'] += nova_unidade
            print(f"Foi adicionado {nova_unidade} {novo_produto} ao banco de dados")
        else:
                print("Produto não encontrado!")
    elif opcao == "4":
        baixa_produto = input("Qual é o produto? ")
        baixa_unidade = int(input("Quantas unidades? "))
        if baixa_produto in estoque:
            if baixa_unidade <= estoque[baixa_produto]['quantidade']:
                    estoque[baixa_produto]['quantidade'] -= baixa_unidade
                    total = baixa_unidade * estoque[baixa_produto]['preco']
                    print(f"Retirada de {baixa_unidade} x {baixa_produto} - Total: R$ {total:.2f}")
            else:
                   print("Unidades insuficientes!")
        else:
            print("Produto não encontrado!")
    else:
        print("Opção inválida!")




