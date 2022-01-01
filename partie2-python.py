class etudiant :
    def __init__(self, nom, prenom, age, cne, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne
 #list de type etudiant        
etudiant = [
{'nom' : 'hbibiali','prenom' : 'hajar', 'age': 20,'cne': 158623, 'moyenne': 8},
{'nom' : 'miyaz','prenom' : 'nozha', 'age': 24,'cne': 25551443, 'moyenne': 20},
{'nom': 'lotfi','prenom' : 'iyad', 'age': 18,'cne': 225548322, 'moyenne': 12},
{'nom' : 'chelle','prenom' : 'zakaria ', 'age': 40,'cne': 1334342223, 'moyenne': 19},
]

#trie par age
etudiant.sort(key=lambda x: x.get('age'))
print(etudiant)
#trie par moyenne
etudiant.sort(key=lambda x: x.get('moyenne'))
print(etudiant)

