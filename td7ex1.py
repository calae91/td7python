import colors;
import time;

taillef = input(colors.warning("taille de la fenetre ? :"))
nom = raw_input(colors.warning("nom du 1er fichier :"))
nom2 = raw_input(colors.warning("nom du 2eme fichier :"))

f = open(nom,"r")
f2 = open(nom2,"r")

nom_fic = time.strftime("%c").replace(" ","") + ".datas"
fw = open(nom_fic,"w")
ligne2 = f2.readline().rstrip("\n")
ligne = f.readline().rstrip("\n")
fw.write(" " + ligne + "\n")


concat = " " + ligne + "\n"
i=0

while i < len(ligne2):
	concat =ligne2[i]
	j=0
	while j < len(ligne):

		if (ligne[j:j+taillef] == ligne2[i:i+taillef]) :
			concat += "X"
		else:
			concat += " "
		j+=1
	i+=1
	fw.write(concat + "\n")

f.close()
fw.close()
