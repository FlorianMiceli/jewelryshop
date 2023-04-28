# Requêtes INSERT INTO à partir d'un fichier XLSX :
+ Placer le .xlsx dans ce dossier
+ Placer le nom de la table dans laquelle vous voulez INSERT INTO vos valeurs dans la cellule A1
+ Placer vos valeurs et leur nom d'attribut comme dans l'exemple suivant : ![image](https://user-images.githubusercontent.com/103659071/235236974-44040124-6be7-4411-a8ac-a733af592777.png)
+ Utilisez la fonction insertIntoDBfromXLSX(XLSXfilename, conn) pour faire vos requetes
	+ XLSXfilename : nom du fichier 
	+ conn : voir requestExample.py

+ Utilisez la fonction insertIntoDBfromMultipleXLSX(to_insert, conn) pour faire vos requetes à partir de plusieurs fichiers
	+ to_insert : liste des noms des fichiers
	+ conn : voir requestExample.py