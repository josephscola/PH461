#!/usr/bin/env python
# coding: utf-8

# # Classes

# Les classes sont les structures sur lesquelles s'appuie la programmation par _objet_.
# Une classe rassemble:
# - des variables appelées _attributs_
# - des fonctions appelées _méthodes_ qui ont un accès direct aux _attributs_ de la classe.
# 
# Une variable dont le type est une classe est appelée une _instance_ de cette classe.

# ```python
# # Syntaxe Python de la définition d'une class
# class nom_de_la_classe :
#     def __init__ (self, var1, var2, var3, ...):  # constructeur de la classe
#         self.variable1 = var1 # variable1 = attribut de la classe; var1 = variable locale
#         self.variable2 = var2
#         self.variable3 = var3  
#         # pas d'instruction return
#       
#     def methode1 (self, arg1, arg2, ...): #définition des fonctions de la classe ou méthodes
#         ...
#         return resultat1
#     
# ```

# ### Exemple d'une classe COMPLEXE

# In[1]:


class COMPLEXE :
    mod = -1
    def __init__ (self, real, imag) :
        self.real = real
        self.imag = imag
            
    def conjugate (self):
        return COMPLEXE (self.real, -self.imag)
    
    def modulus (self):
        modulus = (self.real ** 2 + self.imag ** 2)**0.5
        self.mod = modulus
        return modulus


# In[2]:


z1 = COMPLEXE (1, 2)

z2 = z1.conjugate ()

print (z1.modulus())
print (z2.modulus())


# La commande **dir** appliquée à l'instance d'une classe renvoie la liste des attributs de la classe.

# In[3]:


dir (z1)


# In[4]:


z1.__sizeof__()


# In[5]:


z1.__ge__(z2)


# In[6]:


class COMPLEXE :
    mod = -1
    def __init__ (self, real, imag) :
        self.real = real
        self.imag = imag
            
    def conjugate (self):
        return COMPLEXE (self.real, -self.imag)
    
    def modulus (self):
        modulus = (self.real ** 2 + self.imag ** 2)**0.5
        self.mod = modulus
        return modulus
    
    def __str__ (self):
        # n nombre de chiffres décimaux
        if self.imag < 0:
            string = f'{self.real:.3f} - {-self.imag:.3f}i'
        else:
            string = f'{self.real:.3f} + {self.imag:.3f}i'
        return string
    
    def __ge__(self, other):
        return self.modulus() >= other.modulus()


# In[7]:


z1 = COMPLEXE (1, 2)
z2 = COMPLEXE (0,2)


# In[8]:


z1.__ge__(z2)


# In[9]:


z1 >= z2


# In[10]:


print(z1)

