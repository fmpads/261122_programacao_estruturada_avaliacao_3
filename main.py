# SISTEMA SIMPLES DE COMPRA PARA UMA FLORICULTURA

# CADA ITEM GUARDARÁ APENAS O NOME DA FLOR E SEU VALOR
flores = [
    ["MARGARIDA", 10.0],
    ["ROSA", 15.0],
    ["VIOLETA", 5.0],
    ["ORQUÍDEA", 50.0]
]

carrinho = []

# CAIXA (BORDA)
def mostrar_caixa(textos):
    largura = max(len(texto) for texto in textos)

    print("╔" + "═" * (largura + 2) + "╗")

    for texto in textos:
        espacos = largura - len(texto)
        print("║ " + texto + (" " * espacos) + " ║")

    print("╚" + "═" * (largura + 2) + "╝")


# MENU PRINCIPAL DO SISTEMA
while True:
    mostrar_caixa(["MENU", "C - COMPRAR", "R - REMOVER", "L - LISTAR", "F - FINALIZAR"])

    opcao = input("ESCOLHA UMA OPÇÃO: ")

    if opcao == "C" or opcao == "c":
        continuar_compra = True

        # LAÇO QUE MANTÉM O USUÁRIO NA COMPRA DE FLORES
        while continuar_compra:
            linhas_flores = ["FLORICULTURA"]

            # FOR PERCORRE A LISTA PARA MOSTRAR TODAS AS FLORES DISPONÍVEIS
            for indice in range(len(flores)):
                linhas_flores.append(f"{indice + 1} - {flores[indice][0]}: R$ {flores[indice][1]:.2f}")

            mostrar_caixa(linhas_flores)

            # O BLOCO IF/ELIF/ELSE VALIDA A OPÇÃO INFORMADA
            try:
                escolha = int(input("INFORME A FLOR DESEJADA: "))

                if 1 <= escolha <= len(flores):
                    flor_escolhida = flores[escolha - 1]
                    carrinho.append(flor_escolhida)
                    mostrar_caixa([f"{flor_escolhida[0]} ADICIONADA AO CARRINHO."])
                elif escolha == 0:
                    mostrar_caixa(["OPÇÃO INVÁLIDA."])
                else:
                    mostrar_caixa(["OPÇÃO INVÁLIDA."])
            except ValueError:
                mostrar_caixa(["DIGITE APENAS O NÚMERO."])

            resposta = input("DESEJA COMPRAR MAIS FLORES? (S/N): ")

            if resposta == "S" or resposta == "s":
                continuar_compra = True
            elif resposta == "N" or resposta == "n":
                continuar_compra = False
            else:
                mostrar_caixa(["RESPOSTA INVÁLIDA. VOLTANDO AO MENU."])
                continuar_compra = False

    elif opcao == "R" or opcao == "r":
        if len(carrinho) == 0:
            mostrar_caixa(["O CARRINHO ESTÁ VAZIO."])
        else:
            linhas_carrinho = ["ITENS NO CARRINHO:"]

            # FOR PERCORRE O CARRINHO PARA EXIBIR OS ITENS NUMERADOS
            for indice in range(len(carrinho)):
                linhas_carrinho.append(f"{indice + 1} - {carrinho[indice][0]}: R$ {carrinho[indice][1]:.2f}")

            mostrar_caixa(linhas_carrinho)

            try:
                item_remover = int(input("INFORME A OPÇÃO PARA REMOVER: "))

                if 1 <= item_remover <= len(carrinho):
                    removido = carrinho.pop(item_remover - 1)
                    mostrar_caixa([f"{removido[0]} REMOVIDA DO CARRINHO."])
                else:
                    mostrar_caixa(["OPÇÃO INVÁLIDA."])
            except ValueError:
                mostrar_caixa(["DIGITE APENAS UM NÚMERO."])

    elif opcao == "L" or opcao == "l":
        if len(carrinho) == 0:
            mostrar_caixa(["O CARRINHO ESTÁ VAZIO."])
        else:
            linhas_carrinho = ["ITENS NO CARRINHO:"]

            # FOR PERCORRE A LISTA E MOSTRA TODOS OS ITENS SELECIONADOS
            for indice in range(len(carrinho)):
                linhas_carrinho.append(f"{indice + 1} - {carrinho[indice][0]}: R$ {carrinho[indice][1]:.2f}")

            mostrar_caixa(linhas_carrinho)

    elif opcao == "F" or opcao == "f":
        linhas_resumo = ["RESUMO DA COMPRA:"]
        total = 0.0

        for item in carrinho:
            linhas_resumo.append(f"- {item[0]}: R$ {item[1]:.2f}")
            total = total + item[1]

        linhas_resumo.append(f"VALOR TOTAL: R$ {total:.2f}")
        mostrar_caixa(linhas_resumo)

        mostrar_caixa(["FINALIZANDO A COMPRA..."])
        break

    else:
        mostrar_caixa(["OPÇÃO INVÁLIDA.", "TENTE NOVAMENTE."])
