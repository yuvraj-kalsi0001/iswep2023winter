import pandas as pd
df=pd.read_csv("/home/streptomyces/Menus/core_genome/gene_presence_absence.csv")
df1 = pd.DataFrame()
df1 = df[df['No. isolates']==10]
df2 = df1[['Gene','venezuelae_ATCC_10595']]
df2.to_csv("venezuelae_ATCC_10595.csv")
df2 = df1[['Gene','venezuelae_ATCC_10712']]
df2.to_csv("venezuelae_ATCC_10712.csv")
df3 = df1[['Gene','venezuelae_ATCC_14583']]
df3.to_csv("venezuelae_ATCC_14583.csv")
df4 = df1[['Gene','venezuelae_ATCC_14584']]
df4.to_csv("venezuelae_ATCC_14584.csv")
df5 = df1[['Gene','venezuelae_ATCC_14585']]
df5.to_csv("venezuelae_ATCC_14585.csv")
df6 = df1[['Gene','venezuelae_ATCC_15068']]
df6.to_csv("venezuelae_ATCC_15068.csv")
df7 = df1[['Gene','venezuelae_ATCC_21018']]
df7.to_csv("venezuelae_ATCC_21018.csv")
df8 = df1[['Gene','venezuelae_ATCC_21113']]
df8.to_csv("venezuelae_ATCC_21113.csv")
df9 = df1[['Gene','venezuelae_ATCC_21782']]
df9.to_csv("venezuelae_ATCC_21782.csv")
df10 = df1[['Gene','venezuelae_NRRL_B-65442']]
df10.to_csv("venezuelae_NRRL_B-65442.csv")
