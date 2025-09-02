#%%
arquivo = "comandos_secundarios.txt"

#%% 

conteudo = open(arquivo, mode='r')
print(type(conteudo))


# %%
texto = "Estudar a função dir()"

arquivo_novo = open('estudar_no_futuro.txt',mode='w')

arquivo_novo.write(texto)
arquivo_novo.close()
# %%

conteudo.flush()
# %%
