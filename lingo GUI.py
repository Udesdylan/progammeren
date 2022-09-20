from tkinter import *
from lingo import Lingo

#lingo object
lingo = Lingo()

#lijst met invoervelden
entryvelden = {}

#valideer de invoer, event listener
def validate(event):
    print("beurt: " + str(lingo.beurt))
    print("woord: " + lingo.woord)
    
    invoer = entryvelden[lingo.beurt-1].get()
    print("ingevoerd:" + invoer)
    
    uitvoer = lingo.validate_input(invoer)
    print("resultaat:" + uitvoer)
    
    #uitvoer
    entryvelden[lingo.beurt-2].insert(END, ">" + uitvoer)
   
    #update de status
    status_label.config(text =uitvoer)
    
    #update beurten
    beurten_label.config(text = str(lingo.beurt) + "/5") 
    
#main
app = Tk()
app.title("Lingo")
app.geometry("400x400")
app.resizable(False, False)


#Main
title_label = Label(app, text="Welkom bij lingo", font=("Arial", 18, "bold" ))
title_label.pack()

#uitleg
status_label = Label(app, text="Raad het woord van 5 letters in 5 beurten", font=16, )
status_label.pack()

#Status
status_label = Label(app, text="succes", font=("Arial",14, "bold"), fg ="red")
status_label.pack()

#aantal beurten
beurten_label = Label(app, text="beurt 1/5",font=("Arial", 20, "bold" ))
beurten_label.pack()

for i in range(5):
    entry = Entry(app, bg="#3366cc", justify=LEFT ,font=("Arial", 24, "bold"))
    entry.pack()
    entryvelden[i]=entry
    entry.bind ('<Return>', validate)

app.mainloop()