#definicion de constantes

#importacion de funciones
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#BLOQUE PRINCIPAL
###########################pregunta 1
datos = pd.read_csv("mushrooms.csv")
df= pd.DataFrame(datos)
#print(df)
print(f"La cantidad de registros es: {int(df.size/len(df.columns))}")
df_p= df[df['class']=='p']
df_e= df[df['class']=='e']
df_a_lshape=(df[df['odor']=='a'].shape[0])+(df[df['odor']=='l'].shape[0])
print(f"La cantidad de hongos venenosos es: {(df_p).shape[0]}")
print(f"La cantidad de hongos comestibles es: {(df_e).shape[0]}")
print(f"La cantidad de hongos con olor a almendra o anis es: {df_a_lshape}")
numero_p= ((df_p[df_p['odor']=='a'].size)+(df_p[df_p['odor']=='l'].size))/df_e.shape[1]
numero_e= ((df_e[df_e['odor']=='a'].size)+(df_e[df_e['odor']=='l'].size))/df_e.shape[1]
print(f"De los cuales {int(numero_p)} ({(numero_p/df_a_lshape)*100}%) son venenosos y {int(numero_e)} ({(numero_e/df_a_lshape)*100}%) son comestibles")

#############################pregunta 2

print("")
print("     GRAFICO DE BARRA APILADAS     ")
# Contar ocurrencias de 'n', 'o' y 't' en la columna 'e'
conteo_e = df[df['class'] == 'e']['ring-number'].value_counts()
#print(conteo_e)

# Contar ocurrencias de 'n', 'o' y 't' en la columna 'p'
conteo_p = df[df['class'] == 'p']['ring-number'].value_counts()
#print(conteo_p)

valor_eje = ['none', 'one', 'two']
cantidad_barras = 3
indices = np.arange(cantidad_barras)
ancho_barra = 0.35

clase_e = [conteo_e.loc['n'] if 'n' in conteo_e.index else 0,
           conteo_e.loc['o'] if 'o' in conteo_e.index else 0,
           conteo_e.loc['t'] if 't' in conteo_e.index else 0]

clase_p = [conteo_p.loc['n'] if 'n' in conteo_p.index else 0,
           conteo_p.loc['o'] if 'o' in conteo_p.index else 0,
           conteo_p.loc['t'] if 't' in conteo_p.index else 0]

rects_2 = plt.bar(indices, clase_p, width=ancho_barra, color='pink', label='Poisonous')
rects_1 = plt.bar(indices, clase_e, width=ancho_barra, color='red', label='Edible')

plt.xlabel('Rings')
plt.ylabel('Registros')
plt.title('Setas por cantidad de anillo y clase')
plt.xticks(indices, valor_eje)

plt.legend()
plt.show()


###################################
print("")
print("     GRAFICO DE TORTA      ")
lista_setas = []
for setas in df["habitat"]:
    if setas not in lista_setas:
        lista_setas.append(setas)

nombres_setas = []
for codigo in lista_setas:
    if codigo == 'g':
        nombres_setas.append('grasses')
    elif codigo == 'l':
        nombres_setas.append('leaves')
    elif codigo == 'm':
        nombres_setas.append('meadows')
    elif codigo == 'p':
        nombres_setas.append('paths')
    elif codigo == 'u':
        nombres_setas.append('urban')
    elif codigo == 'w':
        nombres_setas.append('waste')
    elif codigo == 'd':
        nombres_setas.append('woods')
#print(nombres_setas)

lista_cant = []
for setas in lista_setas:
  #print(setas)
  df2 = df[df["habitat"] == setas ]
  lista_cant.append(df2.shape[0])
#print(lista_cant)

pos_max = lista_cant.index(max(lista_cant))
explode = [0] * len(lista_cant)
explode[pos_max] = 0.05

plt.pie(lista_cant, explode=explode, labels=nombres_setas,autopct='%1.1f%%', startangle=90)
plt.title('setas por habitat')
plt.show()

##################################
print("")
print("     GRAFICO DE BARRAS POR CLASE      ")

poblacion_disponible = ['Several', 'Solitary', 'Scattered', 'Numerous', 'Abundant', 'Clustered']

print("Población disponible:")
for i in range(len(poblacion_disponible)):
    print(f"{i + 1} {poblacion_disponible[i]}")

# Solicitar al usuario
opcion = int(input("Ingrese el número de la población que desea: ")) - 1

if opcion < 0 or opcion >= len(poblacion_disponible):
    print("Opción inválida. Por favor, elija un número válido.")
else:
    poblacion_elegida = poblacion_disponible[opcion]

#### ocurrencias
datos_filtrados_e = df[df['class'] == 'e']['population'].value_counts()
#print("ssss", datos_filtrados_e)

datos_filtrados_p = df[df['class'] == 'p']['population'].value_counts()
#print("ssss", datos_filtrados_p)

lista_population = []
for popu in df["population"]:
    if popu not in lista_population:
        lista_population.append(popu)

datos_e = [datos_filtrados_e.loc['a'] if 'a' in datos_filtrados_e.index else 0,
           datos_filtrados_e.loc['c'] if 'c' in datos_filtrados_e.index else 0,
           datos_filtrados_e.loc['n'] if 'n' in datos_filtrados_e.index else 0,
           datos_filtrados_e.loc['s'] if 's' in datos_filtrados_e.index else 0,
           datos_filtrados_e.loc['v'] if 'v' in datos_filtrados_e.index else 0,
           datos_filtrados_e.loc['y'] if 'y' in datos_filtrados_e.index else 0]
#print("e", datos_e)

datos_p = [datos_filtrados_p.loc['a'] if 'a' in datos_filtrados_p.index else 0,
           datos_filtrados_p.loc['c'] if 'c' in datos_filtrados_p.index else 0,
           datos_filtrados_p.loc['n'] if 'n' in datos_filtrados_p.index else 0,
           datos_filtrados_p.loc['s'] if 's' in datos_filtrados_p.index else 0,
           datos_filtrados_p.loc['v'] if 'v' in datos_filtrados_p.index else 0,
           datos_filtrados_p.loc['y'] if 'y' in datos_filtrados_p.index else 0]
#print("p", datos_p)

valores_graficar = [datos_e[poblacion_disponible.index(poblacion_elegida)],
                    datos_p[poblacion_disponible.index(poblacion_elegida)]]

etiquetas = ['Edible', 'Poisonous']
posiciones = np.arange(len(valores_graficar))
ancho_barra = 0.1

plt.barh(posiciones, valores_graficar, align='center')

plt.yticks(posiciones, etiquetas)
plt.xlabel('Registros')
plt.ylabel('Clases')
plt.title('Cantidad de registro por clase con la Poblacion: ' + str(poblacion_elegida))

plt.show()

#parte 3
lista_setas = []
for setas in df["class"]:
    if setas not in lista_setas:
        lista_setas.append(setas)

clases = []
for codigo in lista_setas:
    if codigo == 'e':
        clases.append('comestible')
    elif codigo == 'p':
        clases.append('venenoso')

lista_setas = []
for setas in df["cap-color"]:
    if setas not in lista_setas:
        lista_setas.append(setas)

color_sombrero = []
for codigo in lista_setas:
    if codigo == 'n':
        color_sombrero.append('brown')
    elif codigo == 'b':
        color_sombrero.append('buff')
    elif codigo == 'c':
        color_sombrero.append('cinnamon')
    elif codigo == 'g':
        color_sombrero.append('grey')
    elif codigo == 'r':
        color_sombrero.append('green')
    elif codigo == 'p':
        color_sombrero.append('pink')
    elif codigo == 'u':
        color_sombrero.append('purple')
    elif codigo == 'e':
        color_sombrero.append('red')
    elif codigo == 'w':
        color_sombrero.append('white')
    elif codigo == 'y':
        color_sombrero.append('yellow')


# Lista de nombres personalizados para las clases
nombres_clases = {'e': 'comestible', 'p': 'venenoso'}
colores = {'n': 'brown', 'b': 'buff','c': 'cinnamon', 'g': 'grey', 
           'r': 'green', 'p': 'pink', 'u': 'purple','e': 'red',
           'w' : 'white','y' : 'yellow' }

# Gráfico personalizado 1
grupo_clase_capColor = df.groupby(['cap-color', 'class']).size().unstack()
grupo_clase_capColor.index = color_sombrero  # Cambio de las iniciales a los nombres de colores personalizados
grupo_clase_capColor.columns = [nombres_clases.get(clase, clase) for clase in grupo_clase_capColor.columns]
grafico_barras_apiladas = grupo_clase_capColor.plot(kind='bar', stacked=True)
plt.legend(title='Clases', bbox_to_anchor=(1, 1))
plt.xlabel('Color de sombrero')
plt.ylabel('Registros')
plt.title('Cantidad de setas con mismo color de sombrero')
plt.show()

# Gráfico personalizado 2
grupo_clase_capColor = df.groupby(['class', 'cap-color']).size().unstack()
grupo_clase_capColor.index = clases
grupo_clase_capColor.columns = [colores.get(clase, clase) for clase in grupo_clase_capColor.columns]
grafico_barras_apiladas = grupo_clase_capColor.plot(kind='bar', stacked=True)
plt.legend(title='Color de sombrero', bbox_to_anchor=(1, 1))
plt.xlabel('Clases')
plt.ylabel('Registros')
plt.title('Cantidad de setas con mismo color de sombrero')
plt.show()