"""
Sistema de Gestão de Estoque
Estrutura do estoque:
  - chave: nome do produto (str)
  - quantidade: número de unidades disponíveis (int)
  - preco: valor unitário do produto (float)
"""

estoque = {
    "teclado": {"quantidade": 15, "preco": 250.00},
    "mouse": {"quantidade": 20, "preco": 120.00},
    "monitor": {"quantidade": 8, "preco": 1500.00},
    "headset": {"quantidade": 12, "preco": 350.00},
    "webcam": {"quantidade": 6, "preco": 480.00},
    "pendrive": {"quantidade": 25, "preco": 75.00}
}

while True:
    print("\n=== MENU ===")
    print("1. Ver estoque")
    print("2. Entrada de produto")
    print("3. Saída de produto")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n=== ESTOQUE ATUAL ===")

        for produto, dados in estoque.items():
            print(f"{produto} - Qtd: {dados['quantidade']} - R$ {dados['preco']:.2f}")

    elif opcao == "2":
        nome_produto = input("Qual produto deseja adicionar? ")

        quantidade_produto = int(input("Quantas unidades deseja adicionar? "))
        
        if quantidade_produto > 0:
            if nome_produto in estoque:
                estoque[nome_produto]['quantidade'] += quantidade_produto

                print(f"Foram adicionadas {quantidade_produto} unidades de {nome_produto}.")
            else:
                print("Produto não encontrado.")
        else:
            print("Número inválido!")

    elif opcao == "3":
        baixa_produto = input("Qual produto deseja retirar? ")
        baixa_unidade = int(input("Quantas unidades deseja retirar? "))

        if baixa_unidade > 0:

            if baixa_produto in estoque:

                if baixa_unidade <= estoque[baixa_produto]['quantidade']:
                    estoque[baixa_produto]['quantidade'] -= baixa_unidade
                    total = baixa_unidade * estoque[baixa_produto]['preco']
                    print(f"Retirada de {baixa_unidade} x {baixa_produto} - Total: R$ {total:.2f}")
                else:
                    print("Estoque insuficiente")
            else:
                print("Produto não encontrado")
        else:
            print("Número inválido!")

    elif opcao == "4":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")