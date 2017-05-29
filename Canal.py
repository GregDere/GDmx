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


class Canal:

    id_canal = 1

    def __init__(self):
        self.val_fader = 0
        self.val_bouton = 0
        self.val_canal = 0
        self.id_canal =  Canal.id_canal
        Canal.id_canal += 1

	#Methode pour recuperer la valeur globale du canal
    def get_val_canal(self):
        self.val_canal = int(self.val_fader) * int(self.val_bouton)
        return self.val_canal

	#Methode pour actualiser la valeur de l'atribut fader du canal
    def set_val_fader(self, nouvelle_val_fader):
        self.val_fader = nouvelle_val_fader

	#Methode pour actualiser la valeur de l'atribut bouton du canal		
    def set_val_bouton(self, nouvelle_val_bouton):
            self.val_bouton = nouvelle_val_bouton

    def __repr__(self):
        return "Canal"


class Page:

        id_page = 0

        def __init__(self):
                Page.id_page += 1
                self.canal = []
				
				#Creation de 32 objets "Canal"
                for i in range(32):
                        self.canal.append("")
                        self.canal[i] = Canal()
						
		#Methode pour actualiser la valeur de les atributs fader des canaux de la page	
        def set_val_faders_page(self,val_fader):
                for i in range(32):
                        id_canal = i
                        self.canal[id_canal].set_val_fader(val_fader[i].get())
						
		#Methode pour actualiser la valeur de les atributs bouton des canaux de la page	
        def set_val_boutons_page(self,val_bouton):
                for i in range(32):
                        id_canal = i
                        self.canal[id_canal].set_val_bouton(val_bouton[id_canal].get())
						
		#Methode pour recuperer les valeurs globales des canaux de la page
        def get_val_canaux_page(self,val_canal):
            for i in range(32):
                id_canal = i
                val_canal[i]= self.canal[id_canal].get_val_canal()
