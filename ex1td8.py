import colors

from Tkinter import *
import time

#but de l'exercice :
#faire le gc skew 

#debut
lis = raw_input(colors.warning("Fichier 1 a ouvrir : "))

#ouverture fichier
f = open(lis, "r")

#lecture premiere ligne
#on ne prend pas en compte la premiere ligne du fichier fasta
seq = f.readline().rstrip('\n')
#on commence a rentrer la sequence dans un string
ligne = f.readline().rstrip('\n')
while (ligne != "") :
	seq += ligne
	ligne = f.readline()
f.close()

#uniformisation chaine
i=0
seq = seq.lower()
taille = len(seq)
div = 100
stl = 0
C= 0.0
tm = int(taille/div)
Cmax = -1000
Cmin = 1000
fenetre = Tk()
fenetre.title('GC Skew')
cumu = 0

canvas = Canvas(fenetre, width=1000, height=600, background='white')

while(i < 100):
	cur = seq[i*tm:(i+1)*tm]
	nb_g = cur.count('g')
	nb_c = cur.count('c')
	print(cumu)
	ligne3 = canvas.create_line(i*10,300-cumu/10,i*10,300-(cumu+C)/10)
	cumu+=C
	
	X = C
	C = (float(nb_g - nb_c)/float(nb_g + nb_c))*1000
	if(Cmax < C):
		Cmax = C
	if(Cmin > C):
		Cmin = C
		
	print(i*100)
	ligne1 = canvas.create_line(i*10,300-X,(i+1)*10,300-C)
	i+=1

ligne = canvas.create_line(0,300,1000,300,fill="red")
txt = canvas.create_text(10,280, text="0", font="Arial 16 italic", fill="red")

ligne = canvas.create_line(0,300 - Cmax,1000,300 - Cmax,fill="blue")
txt = canvas.create_text(20,290 - Cmax, text=str(int(Cmax)), font="Arial 16 italic", fill="blue")
print(Cmin)
print(Cmax)
ligne = canvas.create_line(0,300-Cmin,1000,300-Cmin,fill="green")
txt = canvas.create_text(20,280-Cmin, text=str(int(Cmin)), font="Arial 16 italic", fill="green")
print(cumu)
canvas.pack()

fenetre.mainloop()
