import tkinter as tk
import random
import webbrowser
new=2
url="https://youtube.com/shorts/sJQHPymFBfU"

root = tk.Tk()
root.geometry('400x400')

def hover(event):
    x = random.randint(0,350)
    y = random.randint(0,350)
    nao.place(x=x, y=y)

def mensagem():
    message = tk.Label(root, text='Agora que vc aceitou, não tem mais volta')
    ra = tk.Button(root, text="Clique aqui para saber o que você aceitou...", command=raca_negra)
    message.place(x=70, y=120, relx=0, rely=0)
    ra.place(x=80, y=140, relx=0, rely=0)

def raca_negra():
    webbrowser.open(url)

pergunta = tk.Label(root, text='Temos um convite, você aceita sem saber o que é?')
pergunta.pack(anchor='n', padx=20)

nao = tk.Button(root, text='Não')
nao.place(x=140, y=80)
nao.bind('<Enter>', hover)

sim = tk.Button(root, text='Sim', command=mensagem)
sim.place(x=25, y=80, relx=0, rely=0)

root.mainloop()