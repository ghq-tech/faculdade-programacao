import random

# inicializa o jogo
def iniciar_jogo():
    """
    Inicializa o jogo da forca.

    Escolhe uma palavra aleatória, cria a palavra mascarada,
    define a quantidade inicial de vidas e inicia o conjunto
    de letras já tentadas.

    Returns:
        palavra_secreta, palavra_mascarada,
        vida_jogador e letras_tentadas.
    """
    
    lista_palavras = [
    "algoritmo",
    "python",
    "variavel",
    "computador",
    "backend",
    "interface"
    ]
    palavra_secreta = random.choice(lista_palavras)
    palavra_mascarada = ["_"] * len(palavra_secreta)

    # O Set foi escolhido porque não permite letras repetidas e possui busca rápida para verificar tentativas anteriores.
    letras_tentadas = set()

    vida_jogador = 6

    # Mensagem de boas-vindas e regras no início
    print("====================================================")
    print("      BEM-VINDO AO JOGO DA FORCA ACADÊMICO          ")
    print("====================================================")
    print("Regras: Digite uma letra por vez.")
    print("Dica: Todas as palavras são relacionadas à tecnologia e programação.")
    print(f"Você começa com {vida_jogador} tentativas disponíveis.")
    print("Boa sorte!\n----------------------------------------------------")

    return palavra_secreta, palavra_mascarada, vida_jogador, letras_tentadas

# processa uma tentativa do jogador
def processar_tentativa(letra, palavra_secreta, palavra_mascarada, vida_jogador, letras_tentadas):
    """
    Processa a tentativa do jogador.

    Verifica se a letra já foi utilizada, se pertence
    à palavra secreta e atualiza o estado do jogo.

    Args:
        letra (str): letra digitada pelo jogador.
        palavra_secreta (str): palavra correta do jogo.
        palavra_mascarada (list): estado atual da palavra.
        vida_jogador (int): quantidade de vidas restantes.
        letras_tentadas (set): conjunto com letras já utilizadas.

    Returns:
        tuple: palavra_mascarada atualizada,
        vida_jogador atualizado e letras_tentadas.
    """

    # letra repetida sem alterar vidas
    if letra in letras_tentadas:
        print("\nAtenção: Você já tentou essa letra anteriormente!")
    else:
        letras_tentadas.add(letra)

        # Letra correta digitada
        if letra in palavra_secreta:
            print(f"\nBoa! A letra '{letra}' faz parte da palavra.")
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    palavra_mascarada[i] = letra

        #Letra incorreta digitada
        else:
            print(f"\nOps! A letra '{letra}' NÃO faz parte da palavra.")
            vida_jogador -= 1
            print(f"Você perdeu uma vida. Restam {vida_jogador} tentativas.")
    return palavra_mascarada, vida_jogador, letras_tentadas

#código principal
palavra_secreta, palavra_mascarada, vida_jogador, letras_tentadas = iniciar_jogo()

while vida_jogador > 0:
    # Exibição do estado atual do jogo a cada rodada
    # O join() foi utilizado para exibir a lista da palavra mascarada
    # de forma organizada no terminal, separando cada caractere por espaço.
    # Exemplo: "_ _ _ a _" em vez de "['_', '_', '_', 'a', '_']"
    print(f"\nPalavra: {' '.join(palavra_mascarada)}")
    print(f"Letras tentadas: {letras_tentadas}")

    letra = input("Qual letra você quer tentar? ").lower()

    # Validação de Entrada Acadêmica: Garante que o usuário digitou apenas uma letra válida
    if not letra.isalpha() or len(letra) != 1:
        print("\n[ERRO] Entrada inválida! Digite apenas uma única letra do alfabeto (A-Z).")
        continue  # Pula o processamento desta rodada inválida e reinicia o turno no while

    palavra_mascarada, vida_jogador, letras_tentadas = processar_tentativa(
        letra, palavra_secreta, palavra_mascarada, vida_jogador, letras_tentadas
    )

    # Mensagem de vitória com a palavra completa
    if "_" not in palavra_mascarada:
        print("\n====================================================")
        print(f"PARABÉNS! Você descobriu a palavra: {palavra_secreta.upper()}")
        print("====================================================")
        break
# Mensagem de derrota revelando a palavra secreta
if vida_jogador == 0:
    print("\n====================================================")
    print(f"GAME OVER! Suas vidas acabaram. A palavra era: {palavra_secreta.upper()}")
    print("====================================================")