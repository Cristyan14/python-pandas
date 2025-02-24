import pandas as pd

# Cadastrar dados na planilha
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


#Exercício 1: Carregar o arquivo Excel Carregue os dados de um arquivo Excel contendo informações de alunos e suas notas. Exiba o DataFrame.
print("\nExibindo o DataFrame dos alunos e suas notas:")
display(dtf)

# Exercício 2: Calcular a média das notas
print("\nExercício 2: Média das notas dos alunos")
media = dtf['Notas'].mean()
print(media)

# Exercício 3: Ordenar alunos pelas notas
print("\nExercício 3: Ordenação dos alunos pela nota (maior para menor)")
ordenacao = dtf.sort_values('Notas', ascending=False)
display(ordenacao)

# Exercício 4: Filtrar alunos com nota maior ou igual a 7
print("\nExercício 4: Alunos com nota maior ou igual a 7")
maior = dtf.loc[dtf['Notas'] >= 7]
maior = maior.sort_values('Notas', ascending=False)
display(maior)

# Exercício 5: Mostrar aluno com melhor desempenho
print("\nExercício 5: Aluno com o melhor desempenho")
melhor_desempenho = dtf.loc[dtf['Notas'] == dtf['Notas'].max()]
display(melhor_desempenho)

# Exercício 6: Calcular a mediana das notas
print("\nExercício 6: Mediana das notas")
display(dtf['Notas'].median())

# Exercício 7: Adicionar situação de aprovação e reprovação
print("\nExercício 7: Adicionar situação (Aprovado/ Reprovado)")
dtf['Notas'] = pd.to_numeric(dtf['Notas'], errors='coerce')
aprovado = dtf.loc[dtf['Notas'] >=7 ].copy() 
aprovado.loc[:,'Situação'] = 'Aprovado'
reprovado = dtf.loc[dtf['Notas'] < 7].copy()
#reprovado.assign(Situação='Reprovado')
reprovado.loc[:,'Situação'] = 'Reprovado'
dtf = dt_atualizado = pd.concat([aprovado, reprovado])
dp = dtf.sort_values('Notas',ascending=False)
display(dp)

# Exercício 8: Encontrar o aluno com a menor nota
print("\nExercício 8: Aluno com a menor nota")
menor = dtf.loc[dtf['Notas'] == dtf['Notas'].min()];
print(menor)

# Exercício 9: Encontrar o segundo melhor desempenho
print("\nExercício 9: Segundo melhor desempenho")
segundo = dtf.nlargest(2,'Notas').iloc[1:]
display(segundo)

# Exercício 10: Quantidade de alunos com nota menor que 5
print("\nExercício 10: Quantidade de alunos com nota menor que 5")
nmqc = dtf['Quantidade de Notas menores que 5'] = len(dtf[dtf['Notas'] <= 5])
display(dtf)
