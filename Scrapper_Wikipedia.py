#!/usr/bin/env python
# coding: utf-8

# ## Scrapper de Tablas de congresistas en Wikipedia
# #### Ejemplo Chile

# In[ ]:


#Importar paquetes
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


# In[ ]:


#Cambie abajo la url de wikipedia para otros paises
Link = "https://es.wikipedia.org/wiki/Anexo:Senadores_actuales_de_la_República_de_Chile"
pagina = requests.get(Link)


# In[ ]:


#Hacer un Soup
soup = BeautifulSoup(pagina.content, 'html.parser')


# In[ ]:


Tabla = soup.find_all('table')[1] #la página puede tener más de una tabla, acá se escogió la primera (0)


# In[ ]:


#En wikipedia las entradas de una tabla empiezan con un td, no debe cambiar nada acá
valores_lista = []
for i in range(len(Tabla.find_all('td'))):
    valor_fila = megaTable.find_all('td')[i].get_text()
    valores_lista.append(valor_fila)


# In[ ]:


valores_lista


# In[ ]:


#Hago una lista para cada columna, me interesan solo la columna 0,2,5,6,7,8,9. El número total de columnas es 9, modifico el 9 si hay mas o menos columnas.
nombre = []
for i in range(4, len(valores_lista), 10):
    nombre.append(valores_lista[i])
    
#bancada = []
#for i in range(2, len(rowValList), 9):
   # bancada.append(rowValList[i])
    
partido = []
for i in range(5, len(valores_lista), 10):
    partido.append(valores_lista[i])

circuscripcion = []
for i in range(1, len(valores_lista), 10):
    circuscripcion.append(valores_lista[i])

fecha_inicio = []
for i in range(8, len(valores_lista), 10):
    fecha_inicio.append(valores_lista[i])
    
fecha_fin = []
for i in range(9, len(valores_lista), 10):
    fecha_fin.append(valores_lista[i])


# In[ ]:


#Creo una base de datos con las columnas deseadas
import pandas as pd

senado_chile= pd.DataFrame()
senado_chile['nombre'] = nombre
#megaDf['bancada'] = bancada
senado_chile['partido'] = partido
senado_chile['circuscripcion'] = circuscripcion
senado_chile['fecha_inicio'] = fecha_inicio
senado_chile['fecha_fin'] = fecha_fin


# In[ ]:


senado_chile


# In[ ]:


#Elimino los \n de toda la base, si es necesario
senado_chile = senado_chile.replace(r'\n',' ', regex=True)


# In[ ]:


#Elimino los [] con numeros adentro
senado_chile = senado_chile.replace(r'\[.*]','', regex=True)


# In[ ]:


senado_chile


# In[ ]:


#Separo los apellidos y nombres que estan juntos
senado_chile['nombre'] = senado_chile['nombre'].str.replace( r"([A-Z])", r" \1").str.strip()


# In[ ]:


#Guardo la base de datos
senado_chile.to_excel("Senadores_Chile.xlsx")

