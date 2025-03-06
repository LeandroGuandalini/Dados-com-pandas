#%% 4 Carregue adequadamente o dataset Adult Income (disponível para download) e exiba as primeiras 3 linhas.
import pandas as pd
df = pd.read_csv('adult.csv')

print(df.head(3))

# %% 5 Quantas linhas e colunas existem no dataset?
print(df.shape)

# %% 6 Quais colunas possuem valores ausentes? Qual a porcentagem de valores ausentes em cada uma?
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100
print(missing_percentage)

# %% 7 Quantas categorias diferentes existem na coluna "workclass"?
print(df['workclass'].nunique())

# %% 8 Quantas pessoas do dataset possuem nível de educação "Bachelors"?
print(df[df['education'] == 'Bachelors'].shape[0])

# %% 9 Qual é a média de horas trabalhadas por semana ("hours-per-week") para quem ganha mais de $50K e para quem ganha menos?
mean_hours_high_income = df[df['income'] == '>50K']['hours-per-week'].mean()
mean_hours_low_income = df[df['income'] == '<=50K']['hours-per-week'].mean()

print(f"Média de horas para >50K: {mean_hours_high_income}")
print(f"Média de horas para <=50K: {mean_hours_low_income}")

# %% 10 Quais são as 3 ocupações ("occupation") mais comuns entre pessoas que ganham mais de $50K?

top_occupations = df[df['income'] == '>50K']['occupation'].value_counts().head(3)
print(top_occupations)

# %% 11 Extraia apenas a primeira palavra da coluna "education", criando uma nova coluna "education_first_word".

df['education_first_word'] = df['education'].apply(lambda x: x.split()[0])
print(df[['education', 'education_first_word']])

# %% 12 Filtre apenas os dados de mulheres que trabalham mais de 40 horas por semana.

filtered_df = df[(df['gender'] == 'Female') & (df['hours-per-week'] > 40)]
print(filtered_df)

# %% 13 Ordene o DataFrame pelo salário ("income") e depois pela idade ("age"), do maior para o menor.
sorted_df = df.sort_values(by=['income', 'age'], ascending=[False, False])
print(sorted_df)

# %% 14 Crie uma nova coluna "capital_difference", que é a diferença entre "capital-loss" e "capital-gain".
df['capital_difference'] = df['capital-loss'] - df['capital-gain']
print(df[['capital-loss', 'capital-gain', 'capital_difference']])

# %% 15 Crie uma nova coluna "age_decade" que indica em qual década a pessoa nasceu (Exemplo: se a idade é 37, então "age_decade"="30s").
df['age_decade'] = (df['age'] // 10) * 10
df['age_decade'] = df['age_decade'].astype(str) + 's'
print(df[['age', 'age_decade']])

# %% 16 Crie uma nova coluna "marital_status_code" que converte "marital-status" em variáveis numéricas (0, 1, 2, … para cada classe diferente)
df['marital_status_code'] = df['marital-status'].astype('category').cat.codes
print(df[['marital-status', 'marital_status_code']])

# %%
