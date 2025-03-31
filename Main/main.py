from Entrada.entrada import loadData
from Saida.saida import recomendation

#Definir o arquivo
file_path = ("../Dados/student.CSV")

#Carregar os dados das siglas
siglas = loadData(file_path)

#Exibir a recomendaçao feita
recomendation(siglas)