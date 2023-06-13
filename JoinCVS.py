import pandas as pd
import csv
import glob
import os


os.chdir("C:\\Users\\Usuario\\OneDrive\\Documentos\\dados")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f,on_bad_lines='skip', delimiter=",",header= None,encoding='utf-8-sig', skiprows = 1) for f in all_filenames ]) #low_memory = False

#export to csv
combined_csv.to_csv("C:\\Users\\Usuario\\OneDrive\\Documentos\\dadoscombined\\SEARA_combined_csv.csv",
                    index= False,
                    sep=";", 
                    header = ["AnoMes","AnoSemanaGregoriana","Categoria","SubCategoria","Tipodeinformacao","Ranking","Marca","Pedidos","Faturamento","SharePedidos","ShareFaturamento","Tiquete_Medio","Itens","QtdProduto","ValorProduto","PrecoMedio "],
                    encoding='utf-8-sig',
                    decimal = ','
                    )
