import re
import collections

def limpiar_string(str):
    regex = re.compile('[^a-zA-Z]')
    return  regex.sub('', str)


import collections
def isAnagram(str1,str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()
    if str1_list == str2_list:
        return True
    else:
        return False



#anagramas
i = 0
j = 1
lista_a_comprobar = ["car", "tree", "boy", "rlig", "girl", "arc", "yob", "teer"]

while i < len(lista_a_comprobar):

    while j < len(lista_a_comprobar):
        if isAnagram(lista_a_comprobar[i], lista_a_comprobar[j]):
            lista_a_comprobar.remove(lista_a_comprobar[j])
        j = j + 1
    i = i + 1
    j = i + 1
print(lista_a_comprobar)

# saber cual es la mas repetida
input = input("Ingrese una oracion y sepa cual es la letra mas repetida")
print()



