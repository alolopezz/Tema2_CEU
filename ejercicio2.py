texto = 'un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las bandoleras ni elviento, lo que se mueve son nuestras mentes -dijo el maestro'
lineas = texto.split('#')
for i, linea in enumerate(lineas): 
    lineas[i] = linea.capitalize()
    if 1 == 0:
        lineas[i] = lineas[i] + '...'
    else:
        lineas[i] = '- ' + lineas[i] + '.'

for linea in lineas: 
    print(linea)
