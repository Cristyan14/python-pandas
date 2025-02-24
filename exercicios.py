import pandas as pd

lista ={'Nome': [],
        'Notas': []

}

i = 1;
print('Digite a quantidade de alunos: ')
n = int(input(" "))
while i <= n:
  nome = input("Digite o nome: ")
  nota = float(input("Digite a nota: "))
  lista['Nome'].append(nome)
  lista['Notas'].append(nota)
  i = i + 1
  
  dtf = pd.DataFrame(lista);
  
  
  print(dtf)


Exercício 1: Carregar o arquivo Excel Carregue os dados de um arquivo Excel contendo informações de alunos e suas notas. Exiba o DataFrame.

display(dtf)


media = dtf['Notas'].mean()
print(media)

ordenacao = dtf.sort_values('Notas', ascending=False)
display(ordenacao)


maior = dtf.loc[dtf['Notas'] >= 7]
maior = maior.sort_values('Notas', ascending=False)
display(maior)

melhor_desempenho = dtf.loc[dtf['Notas'] == dtf['Notas'].max()]
display(melhor_desempenho)

display(dtf['Notas'].median())

dtf['Notas'] = pd.to_numeric(dtf['Notas'], errors='coerce')
aprovado = dtf.loc[dtf['Notas'] >=7 ].copy() 
aprovado.loc[:,'Situação'] = 'Aprovado'
reprovado = dtf.loc[dtf['Notas'] < 7].copy()
#reprovado.assign(Situação='Reprovado')

reprovado.loc[:,'Situação'] = 'Reprovado'
dtf = dt_atualizado = pd.concat([aprovado, reprovado])
dp = dtf.sort_values('Notas',ascending=False)
display(dp)

menor = dtf.loc[dtf['Notas'] == dtf['Notas'].min()];
print(menor)

segundo = dtf.nlargest(2,'Notas').iloc[1:]
display(segundo)

nmqc = dtf['Quantidade de Notas menores que 5'] = len(dtf[dtf['Notas'] <= 5])
display(dtf)
