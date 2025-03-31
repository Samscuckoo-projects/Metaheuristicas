import pandas as pd

def recomendation(siglas, path="../Dados/recomendacoes.csv"):
    """Salva a lista de recomendacoes em um csv"""
    df = pd.DataFrame({"Sigla": siglas})
    df.to_csv(path, index=False)
    print(f"Resultados salvos em {path}")

    """Exibe a lista de recomendações"""
    for sigla in siglas:
        print(f"{sigla} ")