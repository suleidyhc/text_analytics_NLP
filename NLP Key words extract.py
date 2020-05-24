#!/usr/bin/env python
# coding: utf-8

# In[36]:


get_ipython().system(' pip install nltk')

'''
NLTK is a powerful Python package that provide a set of diverse natural languages algoritms. 
It's free, opensource, easy to use, large community, and well documented. NLTK consists of the most commonb algoritms such as 
tokenizing, pat-of-speech tagging, setiment analysis, topic segmentation, and named entity recognition.
NLTK helps the computer to analysis, preprocess, and understand the written text. 

'''


# In[40]:


# Importando NLTK
import nltk

# Descargar todos los paquetes
nltk.download() # para instalar los paquetes de nltk


# In[22]:


get_ipython().system(' pip install docx2txt #  biblioteca python-docx2txt para leer texto de documentos de Microsoft Word')


# In[24]:


import docx2txt
documento = docx2txt.process("CV Suleidy.docx")


# In[25]:


print(documento)


# In[ ]:


# Para tokenizar este texto y que no estàa en inglès en oraciones, usaremos sent_tokenize():


# In[97]:


from nltk.tokenize import sent_tokenize
print(sent_tokenize(documento))


# In[ ]:


#  tokenizador de palabras 


# In[48]:


from nltk.tokenize import word_tokenize

tokens = word_tokenize(documento)
print(tokens)


# In[50]:


# Frecuencia de los tokens

from nltk.probability import FreqDist


# In[74]:


tokens = nltk.tokenize.word_tokenize(documento)
fdist = nltk.FreqDist(tokens)

for key,val in fdist.items():
    print (str(key)+ ':' + str(val))


# In[86]:


# Mostar en un gràafico la distribuciàon de los tokens

import matplotlib.pyplot as plt
fdist.plot(30, cumulative=False)
plt.show()


# In[90]:


# Quitar palabras de paradas (el, de, y, etc.)

from nltk.corpus import stopwords


# In[92]:


stop_words = set(stopwords.words("spanish"))
print(stop_words)


# In[100]:


# Hacemos copia de la lista

clean = tokens[:]
sr = stopwords.words('spanish')

for token in tokens:
    if token in sr:
        clean.remove(token)


# In[102]:


fdist.plot(30, cumulative=False)


# In[ ]:




