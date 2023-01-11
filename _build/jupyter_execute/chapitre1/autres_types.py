#!/usr/bin/env python
# coding: utf-8

# # Autre types de variables

# ## Booléens

# Les variables bouléennes premettent de représenter les résultats des opérations dans l'algèbre de Boole (ou opérations logiques).
# Elles peuvent prendre les deux valeurs __True__ ou __False__.

# In[1]:


x = True
print (type (x))
print (f'La valeur de x est {x}')
print (f'La valeur de x considérée comme un entier est {x:d}')


# In[2]:


def bool2str (x):
    str = 'False'
    if x : str = 'True'
    return str


# ### Comparaisons

# In[3]:


proposition = 2 < 5
print ('2 < 5  ', proposition)

proposition = 5 < 2
print ('5 < 2  ', proposition)

proposition = 2 < 2
print ('2 < 2  ', proposition)

proposition = 2 <= 2
print ('2 ≤ 2  ', proposition)

proposition = 2 == 5
print ('2 == 5', proposition)

proposition = 2 != 5
print ('2 != 5', proposition)

proposition = not (2 == 5)
print ('not (2 == 5)', proposition)

x = 3
proposition = 2 < x < 4
print ('2 < x < 4', proposition)


# ### Opérateurs __and__ et __or__

# In[4]:


tabular_header = '|a|b|a and b|\n|:-:|:-:|:-:|'
print (tabular_header)

for a in [True, False]:
    for b in [True, False] :
        row = '|' + bool2str (a) + '|' + bool2str (b) + '|' + bool2str (a and b)
        print (row)


# |a|b|a and b|
# |:-:|:-:|:-:|
# |True|True|True
# |True|False|False
# |False|True|False
# |False|False|False

# In[5]:


tabular_header = '|a|b|a or b|\n|:-:|:-:|:-:|'
print (tabular_header)
for a in [True, False]:
    for b in [True, False] :
        expression = a or b
        row = '|' + bool2str (a) + '|' + bool2str (b) + '|' + bool2str (expression)
        print (row)


# |a|b|a or b|
# |:-:|:-:|:-:|
# |True|True|True
# |True|False|True
# |False|True|True
# |False|False|False

# ### Opérateur __not__

# In[6]:


tabular_header = '|a|b|a and b|not (a and b)|\n|:-:|:-:|:-:|:-:|'
print (tabular_header)
for a in [True, False]:
    for b in [True, False] :
        expression = a and b
        row = ('|' + bool2str (a) + '|' + bool2str (b) + '|' + bool2str (expression) 
               + '|' + bool2str (not expression) + '|' )
        print (row)


# |   a   |   b   |   a and b   |   not (a and b)   |
# |:-:|:-:|:-:|:-:|
# |True|True|True|False|
# |True|False|False|True|
# |False|True|False|True|
# |False|False|False|True|

# ### Fonction __all ()__ 

# In[7]:


tabular_header = '|a|b|c|all (a,b,c) |\n|:-:|:-:|:-:|:-:|'
print (tabular_header)
for a in [True, False]:
    for b in [True, False] :
        for c in [True, False] :
            expression = all ( [a, b, c] )
            row = '|' + bool2str (a) + '|' + bool2str (b) + '|' + bool2str (c) + '|' + bool2str (expression)
            print (row)


# |a|b|c|all (a,b) |
# |:-:|:-:|:-:|:-:|
# |True|True|True|True
# |True|True|False|False
# |True|False|True|False
# |True|False|False|False
# |False|True|True|False
# |False|True|False|False
# |False|False|True|False
# |False|False|False|False

# ### Fonction __any ()__

# In[8]:


tabular_header = '|a|b|c|any (a,b,c) |\n|:-:|:-:|:-:|:-:|'
print (tabular_header)
for a in [True, False]:
    for b in [True, False] :
        for c in [True, False] :
            expression = any ( [a, b, c] )
            row = '|' + bool2str (a) + '|' + bool2str (b) + '|' + bool2str (c) + '|' + bool2str (expression)
            print (row)
        


# |a|b|c|any (a,b,c) |
# |:-:|:-:|:-:|:-:|
# |True|True|True|True
# |True|True|False|True
# |True|False|True|True
# |True|False|False|True
# |False|True|True|True
# |False|True|False|True
# |False|False|True|True
# |False|False|False|False

# ### Récréation : prévoir le résultat des instructions suivantes

# In[9]:


5 / 2


# In[10]:


5 // 2


# In[11]:


5 % 2


# In[12]:


( (5 <= 2) - (2 < 5) ) ** (5 / 2 - 5 // 2)


# In[13]:


(5 / 2 - 5 // 2) / ( (5 <= 2) and (2 < 5) )


# In[ ]:


print (1 and 2)


# ## Chaînes de caractères (première partie)

# ### Introduction minimale
# Les variables figurant à l'intérieur d'une paire d'apostrophes (') ou de guillemets (") sont interprétées comme des _chaînes de caractères_.
# Le type d'une _chaîne de caractères_ est __str__.

# ### Formattage des nombres convertis d'une chaîne de caractère
#  A l'intérieur d'une chaîne de caractère, il est permis d'évaluer la valeur d'une variable numérique et de la convertir en _chaîne de caractère_.
#  La variable numérique doit figurer entre accolades et le format de représentation doit être indiqué derrière deux points (:).

# In[ ]:


s = 'Coucou'
print (s)
print ('le type de s est : ', type (s))


# Python permet la concaténation de _chaînes de caractères_ par simple utilisation des opérations __+__ et __*__ : 

# In[ ]:


s = 'Coucou'
s2 = s + s
print (s2)


# In[ ]:


s = 'Coucou'
s3 = s * 3
print (s3)


# In[ ]:


# formattage d'un entier
n = 2
print (f'la valeur de l\'entier n est {n:d}')

x = 23.456
print (f'la valeur du réel x est {x:f}, avec 6 décimales, par défaut')
print (f'la valeur du réel x est {x:.2f}, arrondis avec 2 décimales')
print (f'la valeur du réel x est {x:.2e}, en notation ingénieur')


# In[ ]:


s = 'Coucou'
print (s[0])


# Les chaînes de caractères sont __non modifiables__.

# In[ ]:


s = 'Coucou'
s [0] = 'D'


# Toute modification d'une variable de type __str__ nécessite d'écraser sa valeur précédente :
# 

# In[ ]:


s = 'Coucou'
print ('Avant modification, la chaîne s contient : ', s)
s = 'Doucou'
print ('Après modification, la chaîne s contient : ', s)


# ### Fonction len()
# La fonction __len__ permet de connaître la longueur d'une __chaîne de caractères__.

# In[ ]:


print (len ('Coucou '))

