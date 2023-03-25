# Mélange à queue d'aronde
 
Le programme est une fonction appelée "perfect_shuffle" qui prend une liste "deck" comme argument et retourne une nouvelle liste qui est un mélange parfait de la liste d'origine.

Le fonctionnement de la fonction est le suivant :

La longueur de la liste d'entrée est calculée et stockée dans la variable "n".

Les deux moitiés de la liste d'entrée sont créées et stockées dans les variables "a" et "b" en utilisant la notation de tranche. La première moitié est de 0 à n//2 
(division entière) et la seconde moitié est de n//2 à la fin.

Une liste vide "mix" est créée pour stocker le mélange parfait.

Une boucle for est utilisée pour ajouter alternativement chaque élément de "a" et de "b" à "mix", en commençant par le premier élément de "a".

Cela donne le mélange parfait de la liste d'entrée.

La liste mix est retournée.

En résumé, la fonction "perfect_shuffle" prend une liste et la divise en deux parties égales. Elle crée ensuite une nouvelle liste en alternant les éléments des deux parties dans un ordre spécifique pour obtenir un mélange parfait de la liste originale. La nouvelle liste est retournée en tant que sortie.
