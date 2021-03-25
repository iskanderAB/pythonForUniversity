class event:
    def __init__(self,titre,type,auteur,context,anime_par,date):
        self.titre = titre
        self.type = type
        self.auteur = auteur
        self.context = context
        self.anime_par = anime_par
        self.date = date

    def get_titre(self):
        return self.titre

    def get_type(self):
            return self.type

    def get_auteur(self):
        return self.auteur
    def get_context(self):
        return self.context
    def get_anime_par(self):
        return self.anime_par
    def get_date(self):
        return self.date

    def set_titre(self,titre):
        if(titre !=''):
            self.titre=titre
        return self

    def set_type(self,type):
        if(type !=''):
            self.type=type
        return self

    def set_auteur(self,auteur):
        if (auteur != ''):
            self.auteur=auteur
        return self

    def set_context(self,context):
        if(context !=''):
            self.context=context
        return self

    def set_anime_par(self,anime_par):
        if(anime_par !=''):        
            self.anime_par=anime_par
        return self

    def set_date(self,date):
        if(date !=''):        
            self.date=date
        return self

    def afficher(self):
        print("titre : ", self.titre , "type : " ,  self.type , "contexte : " , self.context , "animateur : " ,self.anime_par ,"auteur : " , self.auteur ,"date" ,  self.date)    

class user:
    def __init__(self,pseudo,password):
        self.pseudo = pseudo
        self.password = password

    def get_pseudo(self):
        return self.pseudo

    def get_password(self):
        return self.password

##programme principal
listeEvente = []
userliste = []
def addevent():
    global listeEvente
    E=event(input("titre : "),input("type  : "),input("auteur : "),input("context : "),input("anime_par : "),input("date : "))
    listeEvente.append(E);
    with open("evenement.txt","a+") as file:
     file.write(E.titre +" "+E.type +" "+E.auteur +" "+ E.context +" "+ E.anime_par +" "+E.date+ "\n")
     file.close()

def deletevent():
    global listeEvente
    titre=input("entre le titre d'evement a supprimer ")
    for ev in listeEvente:
        if  titre == ev.titre :
            print("deleted => ",ev.titre)
            listeEvente.remove(ev)
            with open("evenement.txt", "r") as f:
                lines = f.readlines()
            with open("evenement.txt", "w") as f:
                for line in lines:
                    print(line.split())
                    if line.split()[0] != titre:
                        f.write(line)
            break

def modifierevent():
    global listeEvente
    titre=input("entre le titre d'evement a modifier ")
    for ev in listeEvente:
        if  titre == ev.titre :
            ev.set_titre(input("modifier  titre : ")).set_type(input("modifier type : ")).set_auteur(input("modifier auter : ")).set_context(input("modifier context : ")).set_anime_par(input("modifier anime_par : ")).set_date(input("modifier date : "))
            with open("evenement.txt", "r") as f:
                lines = f.readlines()
            with open("evenement.txt", "w") as f:
                for line in lines:
                    if line.split()[0] == titre:
                        f.write(ev.titre +" "+ev.type +" "+ev.auteur +" "+ ev.context +" "+ ev.anime_par +" "+ev.date+ "\n")
            break






# def consultevent():
#     global listeEvente
#     for ev in listeEvente:
#         print(ev)


addevent()
listeEvente[0].afficher()
modifierevent()
listeEvente[0].afficher()
deletevent()




