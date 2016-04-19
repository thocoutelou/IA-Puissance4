Puissance 4-----------
Url     : http://codes-sources.commentcamarche.net/source/28653-puissance-4Auteur  : cs_lepecheurDate    : 11/08/2013
Licence :
=========

Ce document intitulé « Puissance 4 » issu de CommentCaMarche
(codes-sources.commentcamarche.net) est mis à disposition sous les termes de
la licence Creative Commons. Vous pouvez copier, modifier des copies de cette
source, dans les conditions fixées par la licence, tant que cette note
apparaît clairement.

Description :
=============

Jeu de Puissance 4 pour 2 joueurs avec chute de la pi&egrave;ce dans la colonne 
et reconnaissance de partie gagn&eacute;e.
<br />
<br />+ Possibilit&eacute; d
e continuer la partie pour pouvoir aligner des pi&egrave;ces plusieurs fois
<br
 />
<br />Remarque: Quand on continue une partie d&eacute;j&agrave; gagn&eacute
;e, une pi&egrave;ce ne peut compter que pour une seule ligne de 4.
<br /><a na
me='source-exemple'></a><h2> Source / Exemple : </h2>
<br /><pre class='code' 
data-mode='basic'>
# -------------------------------------- Jeu de puissance 4 
---------------------------------- # 
#           Lepecheur                    
                                                      #
# ---------------------
----------------------------------------------------------------------- # 

  
  # Interface
    
from Tkinter import *

    # Classe du jeu

class Can(C
anvas):

    def __init__(self):
        
            #Variables
        

        self.cases      = [] # Cases déjà remplies
        self.listerouge = []
 # Liste des cases rouges
        self.listejaune = [] # Liste des cases jaunes

        self.dgagnantes = [] # Cases déjà gagnantes et donc ne peuvent plus l'
être à nouveau (cf &quot;Continuer&quot;)
        self.running    = 1  # Type d
e partie en cours
        self.couleur    = [&quot;Rouges&quot;, &quot;Jaunes&q
uot;]
        self.color      = [&quot;red&quot;, &quot;#EDEF3A&quot;]
       
 
            #Interface
        
        self.clair      = &quot;light blue&
quot;
        self.fonce      = &quot;navy blue&quot;
        self.police1    
= &quot;Times 17 normal&quot;
        self.police2    = &quot;Arial 10 normal&q
uot;
        self.police3    = &quot;Times 15 bold&quot;
        self.can     
   = Canvas.__init__(self, width =446, height = 430, bg=self.fonce, bd=0)
     
   
        self.grid(row = 1, columnspan = 5)

            # Joueur en cours

        
        self.joueur = 1
        self.create_rectangle(20,400,115,42
5,fill = self.clair)
        self.create_text(35, 405, text =&quot;Joueur :&quo
t;, anchor = NW, fill = self.fonce, font= self.police2)
        self.indiccoul 
= self.create_oval(85, 405, 100, 420, fill = self.color[1])
        
         
   #Bouton Nouveau Jeu
        
        self.create_rectangle(330,400,420,425,
fill=self.clair)
        self.create_text(340, 405, text =&quot;Nouveau jeu&quo
t;, anchor = NW, fill = self.fonce, font= self.police2)
        
            #
Création des cases
        
        self.ovals = []
        for y in range(10
, 390, 55):
            for x in range(10, 437, 63):
                self.oval
s.append(self.create_oval(x, y, x + 50, y + 50 , fill= &quot;white&quot;))
    
            
            #En cas de click
                
        self.bind(
&quot;&lt;Button-1&gt;&quot;, self.click)
        
            # Pour relier à
 la fin les coordonnées des centres des cases
        
        self.coordscent
res = []
        
            # Comptabilisation des suites de pièces
       
 
        self.rouges, self.jaunes = 0,0
        
            # Dictionnaire 
de reconnaissance
        
        self.dictionnaire = {}
        v = 0
    
    for y in range(10, 390, 55):
            for x in range(10, 437, 63):
    
            self.dictionnaire[(x, y, x + 50, y + 50)] = v
                v += 
1
                self.coordscentres.append((x + 25, y + 25))

    def click(
self,event): #En cas de click
        if 330 &lt; event.x and 400 &lt; event.y 
and event.x &lt; 420 and event.y &lt; 425:
            self.new()# =&gt;Nouveau
 jeu
            
            #Jeu en cours: reconnaissance de la case jouée

            
        else :
            if self.running != 0:
               
 for (w, x, y, z) in self.dictionnaire:
                    if event.x &gt; (w,
 x, y, z)[0] and event.y &gt;(w, x, y, z)[1] and event.x &lt; (w, x, y, z)[2] an
d event.y &lt; (w, x, y, z)[3]:
                        self.colorier(self.dict
ionnaire[(w, x, y, z)]) # =&gt; Jouer

                
    def colorier(self
, n, nb=0): #Gère la coloration des cases
        
        if n in self.cases 
: return # Une case coloriée ne peut plus changer de couleur
           
     
   if n + 7 not in self.cases and n + 7 &lt; 49: #Si la case en dessous est vide
 et existe, on essaie d'abord de colorier celle-là
            self.colorier(n+
7)
            
        else:
            
                #Sinon on colorie
 celle-ci
            
            self.itemconfigure(self.ovals[n], fill = se
lf.color[self.joueur])
            self.cases.append(n)
            self.color
[self.joueur] == 'red' and self.listerouge.append(n) or self.listejaune.append(n
)
            self.listejaune = [case for case in self.listejaune if case not i
n self.listerouge]
            self.verif(n)
            
                #Ch
angement de joueur
            
            self.joueur = [0,1][[0,1].index(se
lf.joueur)-1]
            self.itemconfigure(self.indiccoul, fill = self.color[
self.joueur])

                #On regarde toutes les cases sont remplies
   
         
            self.verificationFinale()        
        
        retu
rn

    
    def verif(self, n): # Vérifie si la pièce ajoutée s'aligne avec 
trois autres déjà placées
        
        if self.running == 0 : return
    
    
        if n in self.listerouge and n+7  in self.listerouge and n+14  in s
elf.listerouge and n+21 in self.listerouge: # D'abbord à la verticale,
        
                                                                                
    # séparément car proximité d'un bord inintéressante
            liste=[n, n
+7, n+14, n+21] # Pour gérér les parties &quot;plurigagnantes&quot;
           
 if self.gagnantes(liste) : self.win(&quot;rouges&quot;, liste[0],liste[3])
   
         return
        
            #idem pour jaunes
        
        if n
 in self.listejaune and n+7 in self.listejaune and n+14 in self.listejaune and n
+21 in self.listejaune:
            liste=[n, n+7, n+14, n+21]
            if 
self.gagnantes(liste) : self.win(&quot;jaunes&quot;, liste[0],liste[3])
       
     return
        
        for x in (1,-6,8):
            
            if 
n in self.listerouge: # en s'assurant qu'elles ne sont trop près des bords (pour
 ne pas arriver de l'autre coté du plateau)
                if n % 7 != 6 and n
+x in self.listerouge:
                    if n % 7 != 5 and n+ 2*x in self.lis
terouge:
                        if n % 7 != 4 and n + 3*x in self.listerouge:

                            liste = [n, n+x, n+2*x, n+3*x]
                   
         if self.gagnantes(liste) : self.win(&quot;rouges&quot;, liste[0],liste[
3])
                            return
                        if n%7 &gt; 0 a
nd (n-x) in self.listerouge:
                            liste = [n-x,n, n+x, n
+2*x]
                            if self.gagnantes(liste) : self.win(&quot;rou
ges&quot;, liste[0],liste[3])
                            return
             
       if n%7 &gt; 1 and (n-x) in self.listerouge:
                        if n
%7 &gt; 2 and n-(2*x) in self.listerouge:
                            liste = [
n-2*x, n-x,n, n+x]
                            if self.gagnantes(liste) : self.
win(&quot;rouges&quot;, liste[0],liste[3])
                            return

                        
                #Pareil pour les jaunes
             
           
            if n in self.listejaune:
                if n % 7 != 6
 and n+x in self.listejaune:
                    if n % 7 != 5 and n+ 2*x in se
lf.listejaune:
                        if n % 7 != 4 and n + 3*x in self.listej
aune:
                            liste = [n, n+x, n+2*x, n+3*x]
             
               if self.gagnantes(liste) : self.win(&quot;jaunes&quot;, liste[0],
liste[3])
                            return
                        if n%7 &g
t; 0 and (n-x) in self.listejaune:
                            liste = [n-x,n, 
n+x, n+2*x]
                            if self.gagnantes(liste) : self.win(&qu
ot;jaunes&quot;, liste[0],liste[3])
                            return
       
             if n%7 &gt; 1 and (n-x) in self.listejaune:
                      
  if n%7 &gt; 2 and n-(2*x) in self.listejaune:
                            lis
te = [n-2*x, n-x,n, n+x]
                            if self.gagnantes(liste) :
 self.win(&quot;jaunes&quot;, liste[0],liste[3])
                            re
turn
                        
        
        for x in (-1,6,-8):
         
   
            if n in self.listejaune:
                if n % 7 != 0 and (n+
x) in self.listejaune:
                    if n % 7 != 1 and n+(2*x) in self.li
stejaune:
                        if n % 7 != 2 and n + (3*x) in self.listejaun
e:
                            liste = [n, n+x, n+2*x, n+3*x]
                
            if self.gagnantes(liste) : self.win(&quot;jaunes&quot;, liste[0],lis
te[3])
                            return
                        if n%7 &lt;6
 and (n-x) in self.listejaune:
                            liste = [n-x,n, n+x,
 n+2*x]
                            if self.gagnantes(liste) : self.win(&quot;j
aunes&quot;, liste[0],liste[3])
                            return
           
         if n%7 &lt; 5 and (n-x) in self.listejaune:
                        if
 n%7 &lt; 4 and n-(2*x) in self.listejaune:
                            liste =
 [n-2*x, n-x,n, n+x]
                            if self.gagnantes(liste) : sel
f.win(&quot;jaunes&quot;, liste[0],liste[3])
                            return

                        
            if n in self.listerouge:
              
  if n % 7 != 0 and (n+x) in self.listerouge:
                    if n % 7 != 1
 and n+(2*x) in self.listerouge:
                        if n % 7 != 2 and n + 
(3*x) in self.listerouge:
                            liste = [n, n+x, n+2*x, n
+3*x]
                            if self.gagnantes(liste) : self.win(&quot;rou
ges&quot;, liste[0],liste[3])
                            return
             
           if n%7 &lt;6 and (n-x) in self.listerouge:
                         
   liste = [n-x,n, n+x, n+2*x]
                            if self.gagnantes(li
ste) : self.win(&quot;rouges&quot;, liste[0],liste[3])
                        
    return
                    if n%7 &lt; 5 and (n-x) in self.listerouge:
   
                     if n%7 &lt; 4 and n-(2*x) in self.listerouge:
            
                liste = [n-2*x, n-x,n, n+x]
                            if self
.gagnantes(liste) : self.win(&quot;rouges&quot;, liste[0],liste[3])
           
                 return

    def verificationFinale(self): # Lorsque toutes le
s cases sont remplies
        
        if len(self.cases)==49: # On comptabili
se les points
            typ =self.plus() # Type de partie gagnée
           
 if typ[1]==0:
                self.texte2 = Label(fen, text = &quot;Les &quot;
 + typ[0] + &quot; ont définitivement gagné !&quot;, bg= self.fonce,
          
                          fg=self.clair, font=self.police1)
                sel
f.texte2.grid()
            elif typ[1]==1:
                self.texte2 = Labe
l(fen, text = &quot;Les &quot; + typ[0] + &quot; ont gagné les premiers!&quot;, 
bg= self.fonce,
                                    fg=self.clair, font=self.po
lice1)
                self.texte2.grid()
            else:
                s
elf.texte2 = Label(fen, text = typ[0], bg= self.fonce, fg=self.clair, font=self.
police1)
                self.texte2.grid(padx=110)

                
    de
f win(self, qui, p, d): # Partie gagnée
        
            #Marquage des piè
ces gagnantes
        
        self.create_line(self.coordscentres[p][0], self
.coordscentres[p][1],
                         self.coordscentres[d][0], self.c
oordscentres[d][1],
                         fill=&quot;blue&quot;)

        
if qui==&quot;rouges&quot; : self.rouges += 1 #Comptabilisation des suites
    
    if qui==&quot;jaunes&quot; : self.jaunes += 1

        if self.running == 
3:
            self.pRouges.config(text = &quot;Rouges : &quot; + str(self.roug
es))
            self.pJaunes.config(text = &quot;Jaunes : &quot; + str(self.ja
unes))
            return

            #Affichage des scores
        
     
   self.qui = qui
        self.texte = Label(fen, text=&quot;Les %s ont gagné !
&quot; % (qui), bg= self.fonce, fg=self.clair, font=self.police1)
        self.
texte.grid()
        self.running = 0
        
            #Proposition de co
ntinuer
        
        self.BtnContinuer = Button(fen, text=&quot; Continuer
 cette partie&quot;, bd= 0, bg=self.fonce, fg=self.clair,
                     
              font=self.police3, command=self.continuer)
        self.BtnContin
uer.grid(padx=120)

        
    def continuer(self): # Si on choisi de pours
uivre la même partie (déjà gagnée par un joueur)
        
        self.running
 = 3
        
            # Affichage des scores
            
        self.p
Rouges = Label(fen, text = &quot;Rouges : %s&quot; %(str(self.rouges)),
       
                      font=self.police3, bg=self.fonce, fg=self.clair)
        
self.pJaunes = Label(fen, text = &quot;Jaunes : %s&quot; %( str(self.jaunes)),

                             font=self.police3, bg=self.fonce, fg=self.clair)


        self.BtnContinuer.destroy()
        self.texte.destroy()
        self
.pRouges.grid(padx=160)
        self.pJaunes.grid(padx=160)

        
    de
f gagnantes(self, liste=[]): # On vérifie que les pièces ne sont pas encore gagn
antes, et on les ajoute dans la liste si elles le deviennent

        for i in
 liste:
            if i in self.dgagnantes: return 0
        
        for n 
in liste:
            self.dgagnantes.append(n)
            
        return 1


    
    def plus(self): # Donner le résultat final
        
        if s
elf.rouges &gt; self.jaunes    : return &quot;Rouges&quot;,0
        if self.ja
unes &gt; self.rouges    : return &quot;Jaunes&quot;,0
        if self.rouges !
= 0             : return self.qui, 1 # En cas d'égalité, le premier à avoir alig
né ses pièces gagne

        return &quot;Personne n'a gagné&quot;, 2 #Sinon, 
tous deux ont perdu

    def new(self):# Nouveau Jeu
        
            # 
Opérations non certaines
        
        try:
            self.BtnContinuer.
destroy()
        except:
            pass
        try:
            self.tex
te.destroy()
        except:
            pass
        try:
            self.
texte2.destroy()
        except:
            pass
        try:
            s
elf.pRouges.destroy()
        except:	
            pass
        try:
       
     self.pJaunes.destroy()
        except:
            pass
            
  
          # Opérations qui le sont
            
        self.destroy()
      
  self.__init__()

	
if __name__ ==	&quot;__main__&quot; :
    fen = Tk()
 
   fen.title(&quot;Puissance 4&quot;)
    fen.config(bg=&quot;navy blue&quot;)

    lecan = Can()
    fen.mainloop()
</pre>
