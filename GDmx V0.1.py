#	 Copyright 2017 Gregoire DEREVIANCKINE
#
#	 This file is part of GDmx.
#		
#    GDmx is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    GDmx is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with GDmx.  If not, see <http://www.gnu.org/licenses/>.



from Tkinter import*
from Canal import*

# Initialisation des variables
fader = []
faderVar = []           
toggle = []
toggleVar = []
canalVal= []


# Init de l'affichage de la fenetre
fenetre = Tk()
fenetre.config(bg = "black")

#declaration d'un objet "Page"
page_1 = Page()

# Remplissage vide des variables
for i in range(32):
    fader.append("")
    toggle.append("")
    faderVar.append(IntVar())
    toggleVar.append(IntVar())
    canalVal.append("")


imgON = PhotoImage(file="ON.gif")		
imgOFF = PhotoImage(file="OFF.gif")

# Fonction actualisant la valeur des attributs boutons de la page et stocke les valeurs global des canaux
def toggleFunc():
    page_1.set_val_boutons_page(toggleVar)
    page_1.get_val_canaux_page(canalVal)
    
    #Affichages des valeurs des canaux dans la console
    print canalVal[0],"",canalVal[1],"",canalVal[2],"",canalVal[3],"",canalVal[4],"",canalVal[5],"",canalVal[6],"",canalVal[7],"",canalVal[8],"",canalVal[9],"",canalVal[10],"",canalVal[11],"",canalVal[12],"",canalVal[13],"",canalVal[14],"",canalVal[15],"",canalVal[16],"",canalVal[17],"",canalVal[18],"",canalVal[19],"",canalVal[20],"",canalVal[21],"",canalVal[22],"",canalVal[23],"",canalVal[24],"",canalVal[25],"",canalVal[26],"",canalVal[27],"",canalVal[28],"",canalVal[29],"",canalVal[30],"",canalVal[31]

# Fonction actualisant la valeur des attributs fader de la page et stocke les valeurs global des canaux
def faderFunc(self):
    page_1.set_val_faders_page(faderVar)     
    page_1.get_val_canaux_page(canalVal)
    
    #Affichages des valeurs des canaux dans la console
    print canalVal[0],"",canalVal[1],"",canalVal[2],"",canalVal[3],"",canalVal[4],"",canalVal[5],"",canalVal[6],"",canalVal[7],"",canalVal[8],"",canalVal[9],"",canalVal[10],"",canalVal[11],"",canalVal[12],"",canalVal[13],"",canalVal[14],"",canalVal[15],"",canalVal[16],"",canalVal[17],"",canalVal[18],"",canalVal[19],"",canalVal[20],"",canalVal[21],"",canalVal[22],"",canalVal[23],"",canalVal[24],"",canalVal[25],"",canalVal[26],"",canalVal[27],"",canalVal[28],"",canalVal[29],"",canalVal[30],"",canalVal[31]

for i in range(32):				
    #Affichage des widgets pour les curseurs et les boutons
    fader[i] = Scale(fenetre, variable = faderVar[i], command = faderFunc, label = "   ", orient = 'v',width=30,length = 200, bg = "black",fg = "orange", from_ = 255, to = 0,highlightthickness=4,highlightbackground="black",troughcolor= "orange")
    toggle[i] = Checkbutton(fenetre, variable= toggleVar[i], command = toggleFunc, indicatoron = 0, image = imgOFF, selectimage = imgON, relief = SOLID, offrelief = SOLID)
    toggle[i].toggle()
	
    #Placement des widgets
    if i<=15:
        toggle[i].grid(row=2,column=i, ipadx=0, ipady=0)
        fader[i].grid(row=1,column=i)
    else:
        toggle[i].grid(row=4,column=i-16, ipadx=0, ipady=0)
        fader[i].grid(row=3,column=i-16)

fenetre.mainloop()




