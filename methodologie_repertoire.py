import pickle
from datetime import date
from tkinter import*

repertoryPath='rep'

###================================================================================================================================================================================================================
###===============================================================================PARTIE MODIFICATION DU FICHIER TXT===============================================================================================
###================================================================================================================================================================================================================

def ajoutRepertoire(chemin):###Fonction modifiant et preparant les ajouts a faire pour la fonction save / demande les nouvelles donnees a l'utilisateur
    repertoire=importer(chemin)
    dico_ajout={}
    list_infos=("nom","prenom","date de naissance","numero de telephone","adresse de rue/avenue","ville","code postal","mail")
    list_doubles_possible=('prenom','numero de telephone','mail')
    for i in range(len(list_infos)):
        texte=("Veuillez entrez votre "+list_infos[i]+"(0 =stop) : ")
        entree=input(texte)
        while (i==2)and not((len(entree)==10)and(entree[2]==entree[5]=='/')and(type(entree[0])==int)and(type(entree[1])==int)and(type(entree[3])==int)and(type(entree[4])==int)and(type(entree[6])==int)and(type(entree[7])==int)):
            entree=input(texte+'valide (jj/ mm/aaaa)')
        while (i==3) and not((len(entree)==10)and(type(entree)==int)):
            entree=input(texte+'valide (0xxxxxxxxx)')
        if entree!='0':
            dico_ajout[list_infos[i]]=entree
        while (entree!='0' and list_infos[i]in list_doubles_possible):
            entree=input(texte)
            ###if entree!='0':
                ###dico_ajout[list_infos[i]].append(entree)
    print(dico_ajout)
    repertoire.append(dict(dico_ajout))
    return repertoire

def save(chemin,data):###Fonction modifiant le fichier repertoire
    repertoire=open(chemin+".martin","wb")
    rep2=pickle.Pickler(repertoire)
    rep2.dump(data)
    repertoire.close()

def importer(chemin):###Fonction important le fichier repertoire
    repertoire=open(chemin+".martin","rb")
    rep2=pickle.Unpickler(repertoire)
    rep3=rep2.load()
    repertoire.close()
    return(rep3)

def delete(chemin):
    repertoire=open(chemin+".martin","rb")
    chemin.remove(path)
    chemin.rmdir(path)

##def Del():
##    print()
##    ligne = int(input("Choisir l'entree que vous voulez effacer(1 etant le premier element): "))
##    nb_lignes = sum(1 for line in open('repertoire.txt'))
##                
##    while ligne<=0 or ligne>nb_lignes or ligne>nb_lignes and ligne>=0 :
##        print("\n","Entrez une valeur valide.","\n")
##        ligne = int(input("Choisir l'entree que vous voulez effacer(1 etant le premier element): "))
##
##    if os.stat("repertoire.txt").st_size == 0:
##        print("\n","Il n'y a plus d'elements dans la liste.","\n")
##        
##    with open("repertoire.txt","r") as rep:
##        liste = list(rep)
##                        
##    del liste[ligne-1]
##                    
##    with open("repertoire.txt","w") as rep:
##        for n in liste:
##            rep.write(n)
###================================================================================================================================================================================================================
###==================================================================================PARTIE INTERFACE/CALCUL PRINCIPAUX DU PROGRAMME===============================================================================
###================================================================================================================================================================================================================

def idle():                                                                     ###Fonction de menu.
    choix=input('Que voulez vous faire ? add(a)/search(s)/quit(q) ')            ###Demande a l'utilisateur ce qu'il souhaite faire.
    if (choix=='add' or choix=='a'):                                            
        save(repertoryPath,ajoutRepertoire(repertoryPath))                      ###Lance la fonction save avec le nom du fichier situé dans la variable globale repertoryPath, avec
        idle()                                                                  ###le data crée dans la fonction ajoutRepertoire elle meme ayant le nom de fichier de stockage des données pour pouvoir l'ouvrir.
    elif (choix=='search' or choix=='s'):                                      
        recherche()                                                             ###Lance la fonction recherche (voir fonction en question).
        
    elif (choix=='quit' or choix=='q'):
        print('merci d utiliser notre interface de repertoire')                 ###Quitte l'application (affiche un message puis termine la fonction idle)

###================================================================================================================================================================================================================

def recherche():

    today=date.today()
    print(today.strftime("%m"))
    
    choix=input('Que voulez vous chercher ? Nom(n) Prenom(p) Date de naissance(d) Numero de telephone(n) Adresse(a) Mail(m) ')
    if (choix=='Nom' or choix=='n'):
        rech='nom'
    elif (choix=='Prenom' or choix=='p'):
        rech='prenom'
    elif (choix =='mois naissance' or choix =='d'):
        rech='date de naissance'
    elif (choix =='Numero de telephone' or choix =='n'):
        rech='numero de telephone'
    elif (choix =='Adresse' or choix =='a'):
        choixA=input('voulez vous l adresse(a) la ville(v) ou le code postal(c) ? ')
        if (choixA=='adresse' or choixA=='a'):
            rech='adresse de rue/avenue'
        elif(choixA=='ville' or choixA=='v'):
            rech='ville'
        elif(choixA=='code postal' or choixA=='c'):
            rech='code postal'
    elif (choix =='Mail' or choix =='m'):
        rech='mail'

    if rech=='date de naissance':
        moisActuel=input('si vous souhaitez utiliser le mois actuel ecrivez "now" ')
        if moisActuel=='now':
            cle=today.strftime("%m")
        else:
            cle=int(moisActuel)
    else:
        cle=input('veuillez entrer la recherche : ')
    
    repertoire=importer(repertoryPath)
    print()
    for i in range(len(repertoire)):
        print(str(i)+' '+str(repertoire[i]))
    for i in range(len(repertoire)):
        ###print('personne en cours '+str(i)+', nom : '+str(repertoire[i][nom]+', prenom '+repertoire[i][prenom]))
        if rech=='date de naissance':
            moisEnCours=(10*int(repertoire[i][rech][3]))+(int(repertoire[i][rech][4]))
            ###print('mois en cours'+str(moisEnCours))
            if moisEnCours==int(cle):
                for y in repertoire[i]:
                    print(y+" "+repertoire[i][y],end=" | ")
                print()
                print()
        elif str(repertoire[i][rech])==str(cle):
            for y in repertoire[i]:
                print(y+" "+repertoire[i][y],end=" | ")
            print()
            print()
    print('End')

    idle()

###================================================================================================================================================================================================================


###penser a ajouter la gestion de plusieurs values

###================================================================================================================================================================================================================
###===============================================================================PARTIE TKINTER INTERFACE GRAPHIQUE===============================================================================================
###================================================================================================================================================================================================================

#Widget
dessin=Tk()
dessin.title("Repertoire Jacqueline Martin Gondet Loïc")

#First cadre
can= Canvas(dessin,height=600,width=500,bg="white")
can.pack(side=LEFT)

# entrée
value=StringVar() 
value.set("Nom")
entree=Entry(can,textvariable=str(value),width=30)
entree.pack(side=TOP)

value=StringVar() 
value.set("Prenom")
entree=Entry(can,textvariable=str(value),width=30)
entree.pack(side=TOP)

value=StringVar() 
value.set("Date de naissance")
entree=Entry(can,textvariable=str(value),width=30)
entree.pack(side=TOP)

value=StringVar() 
value.set("Numero de telephone")
entree=Entry(can,textvariable=str(value),width=30)
entree.pack(side=TOP)

value=StringVar() 
value.set("Adresse")
entree=Entry(can,textvariable=str(value),width=30)
entree.pack(side=TOP)

value=StringVar() 
value.set("Mail")
entree=Entry(can,textvariable=str(value),width=30)
entree.pack(side=TOP)



#second cadre 
can2=Canvas(dessin,height=400,width=400,bg="white")
can2.pack(side=TOP)

#last cadre
bdem=Button(dessin,text="Rechercher",command=recherche,font=("Ubuntu",20,"bold"))
bdem.pack(side=TOP)

cadre=Frame(dessin, pady=50, width=160)

ba=Button(dessin,text="Ajouter",command=ajoutRepertoire,font=("Ubuntu",20,"bold"))
ba.pack(side=LEFT)  
br=Button(dessin,text="Retirer",command=delete,font=("Ubuntu",20,"bold"))
br.pack(side=RIGHT) 
cadreScore=Frame(dessin, pady=50, padx=20)

texto=Text(dessin,height=4,width=20,font=("Ubuntu",20,"bold"))

dessin.mainloop()
#idle()
