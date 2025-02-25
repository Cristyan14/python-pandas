# Aquivo Python referente ao arquivo Untiled 4.ipynb

# Importação do Pandas

import pandas as pd

clubes = {
    'Time': [],
    'Pontuação': []
}

# Solicita ao usuário a quantidade de times e sua pontuação 

i = 1
n = int(input('Digite a quantidade de clubes: '))
while i <= n:
  time = input('Nome clube: ')
  pontuacao = float(input('Pontuação: '))
  clubes['Time'].append(time)
  clubes['Pontuação'].append(pontuacao)
  i = i + 1

#Criação do DataFrame e exibição

dt = pd.DataFrame(clubes);
display(dt)

# Ordenação por meio da Pontuação

ordenado = dt.sort_values('Pontuação', ascending=False)
display(ordenado)

# Melhores 5 colocados

melhores_5 = ordenado.head(5)
display(melhores_5)

# Piores 5 colocados

piores_5 = ordenado.tail(5)
display(piores_5)

# Time com mais de 40 pontos

mais_de_40 = ordenado.loc[ordenado['Pontuação'] >= 40]
display(mais_de_40)


#Inserir quantidade de Vitórias/Empates e Derrotas de cada time

for index in range(len(ordenado)):
    time = ordenado.loc[index, 'Time']
    n_vitorias = int(input(f'Quantidade de vitórias do {time}:'))
    ordenado.at[index, 'Vitórias'] = n_vitorias
display(ordenado)

for index in range(len(ordenado)):
    time = ordenado.loc[index, 'Time']
    n_empates = int(input(f'Quantidade de empates do {time}:'))
    ordenado.at[index, 'Empates'] = n_empates
display(ordenado)

for index in range(len(ordenado)):
    time = ordenado.loc[index, 'Time']
    n_derrotas = int(input(f'Quantidade de derrotas do {time}:'))
    ordenado.at[index, 'Derrotas'] = n_derrotas
display(ordenado)


# Inserir quantidade de Gols Marcados/Sofridos e Saldo de Gols de cada time

for index in range(len(ordenado)):
    time = ordenado.loc[index, 'Time']
    n_gols_marcados = int(input(f'Quantidade de gols marcados do {time}:'))
    ordenado.at[index, 'GM'] = n_gols_marcados
display(ordenado)

for index in range(len(ordenado)):
    time = ordenado.loc[index, 'Time']
    n_contras = int(input(f'Quantidade de gols sofridos do {time}:'))
    ordenado.at[index, 'GC'] = n_contras
display(ordenado)

for index in range(len(ordenado)):
    time = ordenado.loc[index, 'Time']
    n_sg = int(input(f'Quantidade de saldo de gols do {time}:'))
    ordenado.at[index, 'SG'] = n_sg
display(ordenado)

# Exercício 1: Ordenação dos times pela maior pontuação. Ordene o DataFrame dt pela coluna "Pontuação" de forma decrescente e exiba o resultado.

ordenado_final = ordenado.sort_values(by=['Pontuação','Vitórias', 'SG', 'GM'], ascending=False)
display(ordenado_final)


# Exercício 2: Média de vitórias. Calcule a média de vitórias de todos os times.

media = ordenado_final['Vitórias'].mean()
display(media)

# Exercício 3: Time com maior número de vitórias. Encontre o time que obteve o maior número de vitórias.

maior = ordenado_final.loc[ordenado_final['Vitórias'] ==  ordenado_final['Vitórias'].max()]
display(maior)

# Exercício 4: Análise dos times rebaixados. Se considerarmos que os 4 últimos colocados são rebaixados, crie um DataFrame apenas com esses times. Exiba esses times com todas as suas informações.

rebaixados = ordenado_final.tail(4)
dt_rebaixados = pd.DataFrame(rebaixados)
display(dt_rebaixados,)

# Exercício 5: Time com pior saldo de gols. Encontre o time com o pior saldo de gols e exiba suas informações.

pior_saldo = ordenado_final.loc[ordenado_final['SG'] ==  ordenado_final['SG'].min()]
display(pior_saldo)

# Exercício 6: Análise de desempenho. Filtre os times que têm mais de 10 vitórias e menos de 15 derrotas. Exiba esses times com todas as suas informações.

analise = ordenado_final.loc[(ordenado_final['Vitórias'] > 10) & (ordenado_final['Derrotas'] < 15)]
display(analise)

# Exercício 7: Adicionando uma coluna de Situação. Crie uma coluna chamada "Situação" que contenha "Aprovado" para times com pontuação maior ou igual a 50 e "Rebaixado" para os times com pontuação menor que 50.

situacao = ordenado_final[['Time','Pontuação']].head(6)
ordenado_final.loc[ordenado_final.index[0:7], 'Situação'] = 'Libertadores'
ordenado_final.loc[ordenado_final.index[8:14], 'Situação'] = 'Sul-Americana'
ordenado_final.loc[ordenado_final.index[14:16], 'Situação'] = 'Nada'
ordenado_final.loc[ordenado_final.index[16:], 'Situação'] = 'Rebaixado'
ordenado_final.index = ordenado_final.index + 1
display(ordenado_final)


# Exercício 8: Melhor desempenho em gols. Encontre o time com maior número de gols feitos (GM) e exiba as informações.

desemepenho = ordenado_final.loc[ordenado_final['GM'] == ordenado_final['GM'].max()]
display(desemepenho)

# Exercício 9: Comparação entre vitórias e empates. Encontre a diferença entre o número de vitórias e empates de cada time e crie uma nova coluna chamada "Diferença de Vitória-empate". Exiba o DataFrame com essa nova coluna.

diferenca = ordenado_final['Diferença Vitória/Empate'] = ordenado_final['Vitórias'] - ordenado_final['Empates']
display(ordenado_final)

# Exercício 10: Times que têm mais de 20 vitórias. Crie um DataFrame com os times que conseguiram mais de 20 vitórias. Exiba esse DataFrame.

mais_de_vinte = ordenado_final.loc[ordenado_final['Vitórias'] > 20]
pd.DataFrame(mais_de_vinte)
display(mais_de_vinte)






