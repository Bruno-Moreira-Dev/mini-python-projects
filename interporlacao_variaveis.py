nome = "Bruno"
idade = 29
profissao = "Programador"
linguagem = "Python"

pessoa = {
    "nome": nome,
    "idade": idade,
    "profissao": profissao,
    "linguagem": linguagem
}

print("Olá, me chamo %s.\nEu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))
print(f"Olá, me chamo {nome}. Eu tenho {idade} ano de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")
