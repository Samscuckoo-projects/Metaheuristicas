import pandas as pd

def recomendation(materiasFaltantes, path="../Dados/recomendacoes.csv"):
    """Exibe a lista de recomendações"""
    print(f"As matérias recomendadas para esse aluno são:")
    for materia, horas in materiasFaltantes:
        print(f"- {materia} {horas}")

"""Salva a lista de recomendacoes em um csv"""
    df = pd.DataFrame(materiasFaltantes, columns=["Sigla", "Horas"])
    df.to_csv(path, index=False)
    print(f"Resultados salvos em {path}")