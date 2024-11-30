#!/usr/bin/env python3

def contar_nos(arvore):
    """
    Função recursiva que conta o número total de nós na árvore filogenética.
    A árvore é representada como um dicionário de dicionários.

    Parâmetros:
    - arvore: dicionário que representa a árvore filogenética.

    Retorna:
    - O número total de nós na árvore, incluindo ramos internos e folhas.
    """

    try:
        # Inicializa a contagem com 0, pois não devemos contar o nó inicial (Filo1)
        total_nos = 0

        # Verifica se o nó tem filhos (subárvores) e percorre cada um dos filhos
        if isinstance(arvore, dict):  # Garante que estamos lidando com um dicionário
            for chave, subarvore in arvore.items():
                # A contagem é feita apenas nas subárvores (nós internos e folhas)
                total_nos += 1  # Conta o nó atual (classe, ordem, família, etc.)
                if isinstance(subarvore, dict):
                    total_nos += contar_nos(subarvore)  # Chama recursivamente para cada subárvore

        return total_nos

    except Exception as e:
        print(f"Erro inesperado: {e}")
        return 0


# Árvore filogenética fornecida
arvore = {
    "Filo1": {
        "Classe1": {
            "Ordem1": {
                "Familia1": {},
                "Familia2": {}
            },
            "Ordem2": {
                "Familia3": {
                    "Genero3": {},
                    "Genero4": {}
                }
            }
        },
        "Classe2": {
            "Ordem3": {},
            "Ordem4": {
                "Familia4": {},
                "Familia5": {
                    "Genero1": {},
                    "Genero2": {
                        "Especie1": {},
                        "Especie2": {}
                    }
                }
            }
        }
    }
}

# Chamada da função para contar os nós
total_nos = contar_nos(arvore)

# Exibe o total de nós
print(f'O total de nós na árvore filogenética é: {total_nos}')


