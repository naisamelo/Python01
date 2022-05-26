frase = 'Curso em Vídeo Python'
#frase = frase.replace('Python','Android')
print(frase)
print('Curso' in frase)
print(frase.find('Vídeo')) #retorna a prosição da palavra
print(frase.lower().find('video'))
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])#retorna a palvra e depois a letra na posição indicada entre colchetes