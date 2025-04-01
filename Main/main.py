from Entrada.entrada import loadData
from Saida.saida import recomendation

#Definir o arquivo
"""file_path = ("../Dados/student.CSV")"""
file_path = input(f"Digite o caminho relativo do arquivo: ")

#Carregar os dados das siglas
materiasFaltantes = loadData(file_path)

#Exibir a recomendaçao feita
recomendation(materiasFaltantes)