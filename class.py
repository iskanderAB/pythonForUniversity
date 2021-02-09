
# class compte:
# #gestion d'un compte bancaire
#     def crediter(self,x):
#         self.solde += x
#     def afficherSolde(self):
#         print("Le solde vaut :",self.solde)
# monCompte=compte()
# monCompte.nom = "comptePerso"
# monCompte.numero = 666
# monCompte.solde = 1000

# print(monCompte.numero)
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y


p = Point(1,2)
print(p.__x)
