import pandas as pd

def loadData(path):
   """Lê um arquivo CSV e retorna um DataFrame"""

   try:
       df = pd.read_csv(path)
       return df['Sigla'].tolist()
   except Exception as e:
       print(f"Erro ao carregar o histórico: {e}")
       return None