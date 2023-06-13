import pandas as pd
import csv
from os import listdir, sep
from os.path import isfile, join

mypath = "C:\\Users\\Usuario\\OneDrive\\Documentos\\Teste_Origin"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]

for o in onlyfiles:
    path = print(mypath + '\\' + o)
    read_file = pd.read_excel (r'' + mypath + '\\' + o, 
    usecols= "A,H,I,J,N,O,P,Q,R", 
    header = 1)

    ##Adicionei essa linha - ela tira as quebras de linhas do texto
    read_file = read_file.replace(r'\n',' ', regex=True) 

    read_file.to_csv (r'' + 'C:\\Users\\Usuario\\OneDrive\\Documentos\\Teste_Destination' + '\\' + o +'.csv', sep=";",
    header= ["Data","EAN no fornecedor","ID do SKU na Lett","Titulo do SKU no fornecedor","Loja","SKU","Disponibilidade media 1P","Disponibilidade media 3P","Disponibilidade media Qualquer seller"], 
    index = False, 
    mode='w', 
    encoding='utf-8-sig', 
    float_format= None, 
    quoting = csv.QUOTE_NONE, 
    quotechar="",
    doublequote = False, escapechar="\n",decimal = '.')
         #["Data","ID da categoria Lett","Categoria Lett","ID do fornecedor","Fornecedor","ID da marca Lett","Marca Lett","EAN no fornecedor","ID do SKU na Lett","Titulo do SKU no fornecedor","Competitor SKUs IDs","Grupos de produtos do usuario","Organizacao","Loja","SKU","Disponibilidade media 1P","Disponibilidade media 3P","Disponibilidade media - Qualquer seller","Ultima data disponivel 1P","Ultimo status do dia"]
         
