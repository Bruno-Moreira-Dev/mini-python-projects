curso = "pYtHon"
novo_curso = "    Python   "

print(curso.upper())
print(curso.lower())
print(curso.title())

print(novo_curso.lstrip())
print(novo_curso.rstrip())

novo_curso_sem_espacos = novo_curso.strip()

print(novo_curso_sem_espacos)
print(novo_curso_sem_espacos.center(10, "#"))
print(".".join(novo_curso_sem_espacos))

for letra in novo_curso_sem_espacos:
    print(letra, end="-")
else:
    print()
    