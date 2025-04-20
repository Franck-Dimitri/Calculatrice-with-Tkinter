from tkinter import * 


"""

numero = []

def bouton0():
    numero.append(0)
    Ecran_affichage.delete(0, END)
    # ensuite on insert le mif ot de genere :
    Ecran_affichage.insert(0, numero)

def bouton9():
    numero.append(9)
    Ecran_affichage.delete(0, END)
    # ensuite on insert le mif ot de genere :
    Ecran_affichage.insert(0, numero)

chiffre = numero
for i in numero:
    chiffre = chiffre + numero[i]

def addition():

    Ecran_affichage.delete(0, END)
    # ensuite on insert le mif ot de genere :
    Ecran_affichage.insert(0, numero)
    resultat = numero + chiffre2
            
def bouton_egale():
    Ecran_affichage.delete(0, END)
    # ensuite on insert le mif ot de genere :
    Ecran_affichage.insert(0, chiffre)
    numero.clear()

"""



calcul = ""

def ajout_calcul(symbol):
    global calcul 
    calcul += str(symbol)
    Ecran_affichage.delete(0, END)
    Ecran_affichage.insert(0, calcul)

    
def eval_calcul():
    global calcul
    try:
        calcul = str(eval(calcul))
        Ecran_affichage.delete(0, END)
        Ecran_affichage.insert(0, calcul)
    except:
        effacer_ecran()
        Ecran_affichage.insert(0, "Erreur")


def effacer_ecran():
    global calcul 
    calcul = ""
    Ecran_affichage.delete(0, END)

# creation de la fenetre
window = Tk()

#paramettre de la fenetre 
window.title("Calculatrice")
window.geometry("480x720")
window.minsize(420, 720)
window.maxsize(420, 720)
window.iconbitmap("") # chemin vers le logo de l'app
window.config(background = "#FFFDEE")


# creation de la frame principale
frame = Frame(window)
frame_ecran = Frame(frame, bg = "#FFFDEE")
frame_bouton = Frame(frame, bg = "#FFFDEE")


width = 3
height = 2

#creer le champ de notere app (input/entrer)
Ecran_affichage = Entry(frame_ecran, font=("Helvetica", 20), bg = "#FFFDEE", fg='black')
Ecran_affichage.pack()


frame_C = Frame(frame_bouton, bg = "#FFFDEE")
frame_racine = Frame(frame_bouton, bg = "#FFFDEE")
frame_mod= Frame(frame_bouton, bg = "#FFFDEE")
frame_mul = Frame(frame_bouton, bg = "#FFFDEE")
#-------------------------------------
frame_1 = Frame(frame_bouton, bg = "#FFFDEE")
frame_2 = Frame(frame_bouton, bg = "#FFFDEE")
frame_3 = Frame(frame_bouton, bg = "#FFFDEE")
frame_div = Frame(frame_bouton, bg = "#FFFDEE")
#---------------------------------------
frame_4 = Frame(frame_bouton, bg = "#FFFDEE")
frame_5 = Frame(frame_bouton, bg = "#FFFDEE")
frame_6 = Frame(frame_bouton, bg = "#FFFDEE")
frame_sous = Frame(frame_bouton, bg = "#FFFDEE")
#---------------------------------------
frame_7 = Frame(frame_bouton, bg = "#FFFDEE")
frame_8 = Frame(frame_bouton, bg = "#FFFDEE")
frame_9 = Frame(frame_bouton, bg = "#FFFDEE")
frame_add = Frame(frame_bouton, bg = "#FFFDEE")
#---------------------------------------
frame_0 = Frame(frame_bouton, bg = "#FFFDEE")
frame_open = Frame(frame_bouton, bg = "#FFFDEE")
frame_close = Frame(frame_bouton, bg = "#FFFDEE")
frame_egale = Frame(frame_bouton, bg = "#FFFDEE")



#bouton C : pour vider la calco
bouton_C = Button(frame_C, text="C", width=width, height=height,  font=("Helvetica", 25), bg = "#977DFF", fg = "white", command = effacer_ecran)
bouton_C.pack()

#bouton racine
bouton_rac = Button(frame_racine, text="ra", width=width, height=height, font=("Helvetica", 25), bg = "#977DFF", fg = "white")
bouton_rac.pack()
frame_C
#bouton modulo
bouton_mod = Button(frame_mod, text="mo", width=width, height=height, font=("Helvetica", 25), bg = "#977DFF", fg = "white", command = lambda:ajout_calcul("%"))
bouton_mod.pack()

#bouton puissance
bouton_mul = Button(frame_mul, text="x", width=width, height=height,  font=("Helvetica", 25), bg = "#977DFF", fg = "white", command = lambda:ajout_calcul("*"))
bouton_mul.pack()

frame_C.grid(padx = 3, pady = 3, row = 0, column = 0, sticky = W)
frame_racine.grid(padx = 3, pady = 3, row = 0, column = 1, sticky = W)
frame_mod.grid(padx = 3, pady = 3, row = 0, column = 2, sticky = W)
frame_mul.grid(padx = 3, pady = 3, row = 0, column = 3, sticky = W)

# -----------------------------------------------------------------------------------


#bouton 1
bouton_1 = Button(frame_1, text="1", width=width, height=height,  font=("Helvetica", 25), bg = "#0033FF", fg = "white", command = lambda:ajout_calcul(1))
bouton_1.pack()

#bouton 2, command = lamda:ajout_calcul(2)
bouton_2 = Button(frame_2, text="2", width=width, height=height, font=("Helvetica", 25), bg = "#0033FF", fg = "white", command = lambda:ajout_calcul(2))
bouton_2.pack()

#bouton 1
bouton_3 = Button(frame_3, text="3", width=width, height=height, font=("Helvetica", 25), bg = "#0033FF", fg = "white", command = lambda:ajout_calcul(3))
bouton_3.pack()

#bouton 1
bouton_div = Button(frame_div, text="/", width=width, height=height, font=("Helvetica", 25), bg = "#977DFF", fg = "white", command = lambda:ajout_calcul("/"))
bouton_div.pack()

frame_1.grid(padx = 3, pady = 3, row = 1, column = 0, sticky = W)
frame_2.grid(padx = 3, pady = 3, row = 1, column = 1, sticky = W)
frame_3.grid(padx = 3, pady = 3, row = 1, column = 2, sticky = W)
frame_div.grid(padx = 3, pady = 3, row = 1, column = 3, sticky = W)

# -----------------------------------------------------------------------------------

#bouton 4
bouton_4 = Button(frame_4, text="4", width=width, height=height,  font=("Helvetica", 25), bg = "#0033FF", fg = "white", command = lambda:ajout_calcul(4))
bouton_4.pack()

#bouton 5
bouton_5 = Button(frame_5, text="5", width=width, height=height, font=("Helvetica", 25), bg = "#0033FF", fg = "white", command = lambda:ajout_calcul(5))
bouton_5.pack()
#bouton 6
bouton_6 = Button(frame_6, text="6", width=width, height=height, font=("Helvetica", 25), bg = "#0033FF", fg = "white", command = lambda:ajout_calcul(6))
bouton_6.pack()

#bouton soustraction
bouton_sous = Button(frame_sous, text="-", width=width, height=height, font=("Helvetica", 25), bg = "#977DFF", fg = "white", command = lambda:ajout_calcul("-"))
bouton_sous.pack()

frame_4.grid(padx = 3, pady = 3, row = 2, column = 0, sticky = W)
frame_5.grid(padx = 3, pady = 3, row = 2, column = 1, sticky = W)
frame_6.grid(padx = 3, pady = 3, row = 2, column = 2, sticky = W)
frame_sous.grid(padx = 3, pady = 3, row = 2, column = 3, sticky = W)

# -----------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------

#bouton 7
bouton_7 = Button(frame_7, text="7", width=width, height=height,  font=("Helvetica", 25), bg = "#0033FF", fg = "white", command = lambda:ajout_calcul(7))
bouton_7.pack()

#bouton 8
bouton_8 = Button(frame_8, text="8", width=width, height=height, font=("Helvetica", 25), bg = "#0033FF", fg = "white", command = lambda:ajout_calcul(8))
bouton_8.pack()

#bouton 9
bouton_9 = Button(frame_9, text="9", width=width, height=height, font=("Helvetica", 25), bg = "#0033FF", fg = "white", command = lambda:ajout_calcul(9))
bouton_9.pack()

#bouton soustraction
bouton_add = Button(frame_add, text="+", width=width, height=height, font=("Helvetica", 25), bg = "#977DFF", fg = "white", command = lambda:ajout_calcul("+"))
bouton_add.pack()

frame_7.grid(padx = 3, pady = 3, row = 3, column = 0, sticky = W)
frame_8.grid(padx = 3, pady = 3, row = 3, column = 1, sticky = W)
frame_9.grid(padx = 3, pady = 3, row = 3, column = 2, sticky = W)
frame_add.grid(padx = 3, pady = 3, row = 3, column = 3, sticky = W)

# -----------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------

#bouton 0
bouton_0 = Button(frame_0, text="0", width=width, height=height,  font=("Helvetica", 25), bg = "#0033FF", fg = "white", command = lambda:ajout_calcul(0))
bouton_0.pack()

#bouton virgule
bouton_open = Button(frame_open, text="(", width=width, height=height, font=("Helvetica", 25), bg = "#0033FF", fg = "white", command = lambda:ajout_calcul("("))
bouton_open.pack()

#bouton multiplication
bouton_close = Button(frame_close, text=")", width=width, height=height, font=("Helvetica", 25), bg = "#977DFF", fg = "white", command = lambda:ajout_calcul(")"))
bouton_close.pack()

#bouton egale
bouton_egale = Button(frame_egale, text="=", width=width, height=height, font=("Helvetica", 25), bg = "#977DFF", fg = "white", command = eval_calcul)
bouton_egale.pack()

frame_0.grid(padx = 3, pady = 3, row = 4, column = 0, sticky = W)
frame_open.grid(padx = 3, pady = 3, row = 4, column = 1, sticky = W)
frame_close.grid(padx = 3, pady = 3, row = 4, column = 2, sticky = W)
frame_egale.grid(padx = 3, pady = 3, row = 4, column = 3, sticky = W)

# -----------------------------------------------------------------------------------

#
frame_ecran.grid(row = 0, column = 1, sticky = N)
frame_bouton.grid(row = 1, column = 1, sticky=S)
frame.pack(expand = YES)

# afficher la fenetre
window.mainloop()