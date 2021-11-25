from tkinter import *
import getpass

#função de imprimir dados:

def impDados():
    print("E-mail:%s" % vmail.get())
    print("Nome:%s" % vnome.get())
    print("Senha:%s" % vsenha.get())

root = Tk()
root.title("BoraVê.com")
root.geometry("600x500")
root.configure(background = "#dde")
#Campo de texto para marketing e/ou frase da empresa
txt1=Label(root, text="Melhore seu turismo" , background="#dde", foreground="#0000FF")
txt1.place(x= 20, y=20, width=120, height=40) 
#campo de texto para E-mail do usuario
Label(root,text="E-mail:", background="#ffffff", foreground="#009", anchor=W ).place(x=100,y=100,width=120,height=40)
vmail = Entry(root)
vmail.place(x=140, y=100, width=120, height=40)
#campo de texto para nome:
Label(root, text="Nome:", background="#ffffff", foreground="#009", anchor=W ).place(x=100,y=140, width=120, height=40)
vnome = Entry(root)
vnome.place(x=140,y=140, width=120, height=40)
#campo de texto para senha:
Label(root,text="Senha:", background="#ffffff", foreground="#009", anchor=W).place(x=100, y=180, width=120, height=40)
vsenha = Entry(root)
vsenha.place(x=140, y=180, width=120, height=40)

#abreviando variaveis
vtxt = "Entrada"
vbg = "#dde"
vfg = "#000"
#Butão de entrada
btn = Button(root, text=vtxt, command=impDados, bg=vbg, fg=vfg)
btn.pack(ipadx=20,ipady=20,padx=5,pady=5,side="top",fill=X,expand=True)


root.mainloop()
