# import pdb
# pdb.set_trace()

# filename = 'Data/Export Bateria 5.csv'
filename = 'Data/Export Bateria 7.csv'
arquivo = open(filename, 'r', encoding='utf-8')  #read mode and forced UTF-8
linhas = arquivo.readlines()
arquivo.close()

indices = [19, 20, 21, 22, 25]

tabela = [linha.split(',') for linha in linhas]
# tabela = []
# for linha in linhas:
    # aux = linha.split(',')
    # tabela.append(aux)

# tabelavoltas = [[line[id] for id in indices] for line in tabela if len(line)==len(tabela[0])]
tabelavoltas = []
for linhatabela in tabela:
    if len(linhatabela) != len(tabela[0]):
        continue
    
    temp = []
    for id in indices:
        temp.append(linhatabela[id])
    tabelavoltas.append(temp)

for volta in tabelavoltas:
    print( str(volta).replace('[' , '').replace(']', '') )