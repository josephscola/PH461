#!/usr/bin/env python
# coding: utf-8

# # Classes

# Les classes sont les structures sur lesquelles s'appuie la programmation par _objet_.
# Une classe rassemble:
# - des variables appelées _attributs_
# - des fonctions appelées _méthodes_ qui ont un accès direct aux _attributs_ de la classe.
# On appelle _instance_ une variable dont le type est une classe.

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
    def __init__ (self, real, imag) :
        self.real = real
        self.imag = imag
            
    def conjugate (self):
        return COMPLEXE (self.real, -self.imag)
    
    def modulus (self):
        return (self.real ** 2 + self.imag ** 2)**0.5
    
    def C2string (self):
        # n nombre de chiffres décimaux
        if self.imag < 0:
            string = f'{self.real:.3f} - {-self.imag:.3f}i'
        else:
            string = f'{self.real:.3f} + {self.imag:.3f}i'
        return string


# In[2]:


z1 = COMPLEXE (1, 2)
print ('z1 = ', z1.C2string ())

z2 = z1.conjugate ()
print ('z2 = conj (z1) = ' + z2.C2string ())


# ## Arguments des fonctions

# In[3]:


def ADD_NUMBERS (x1, x2) :
    x3 = x1 + x2
    x1 *= 2
    return x3


# In[4]:


x1 = 2
x2 = 3
x3 = ADD_NUMBERS (x1, x2)
print ('x3 = ', x3)
print ('x1 = ', x1)


# Le premier argument de la fonction se nomme __x1__ mais il est interprété comme une variable distincte de la variable __x1__ passée en argument lors de l'appel de la fonction.

# In[5]:


def ADD_COMPLEXES (arg1, arg2) :
    z3 = COMPLEXE (arg1.real + arg2.real, arg1.imag + arg2.imag)
    arg1.imag *= 2
    return z3


# In[6]:


z1 = COMPLEXE (1, 2)
print ('avant l\'appel de la fonction')
print ('z1 = ' + z1.C2string () )
z2 = z1.conjugate ()

print ('après l\'appel de la fonction')
z4 = ADD_COMPLEXES (z1, z2)
print ('z4 = ' + z4.C2string () )
print ('z1 = ' + z1.C2string () )


# Le premier argument de la fonction porte un nom différent de la variable passée en argument lors de l'appel de la fonction mais comme il s'agit d'une classe, la fonction a traité l'instance de la classe qui a été déclarée dans le script d'appel.
