

class Pizza:
    def __init__(self, nom: str, prix: float, ingrediants, vegetarienne = False):
        self.nom = nom
        self.prix = prix
        self.ingrediants = ingrediants
        self.vegetarienne = vegetarienne
    def Afficher(self):
        type = ""
        if self.vegetarienne:
            type = "- Végétarienne"
        print("Pizza", self.nom, ":", self.prix, "€", type)
        print("Ingrédiants: ", ", ".join(self.ingrediants))
        print()


class PizzaPersonalisee(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    dernier_numero = 0
    def __init__(self):
        PizzaPersonalisee.dernier_numero += 1
        self.numero = PizzaPersonalisee.dernier_numero
        super().__init__("Personalisée", 0, [])


        self.nom = "Personalisée " + str(self.numero)

        self.demander_ingredients_utilisateur()
        self.calsuler_prix()
    def demander_ingredients_utilisateur(self):
        print()
        print(f"Pizza personalisée {self.numero}")
        while True:
            ingredient = input("Entrer ingrédient ou tappez Entrer pour terminer: ")
            if ingredient == "":
                return
            self.ingrediants.append(ingredient)
            print("Vous avez choisi", len(self.ingrediants), "ingrédients:", ", ".join(self.ingrediants))
    def calsuler_prix(self):
        self.prix = self.PRIX_DE_BASE + len(self.ingrediants)*self.PRIX_PAR_INGREDIENT




pizza1 = Pizza("4 fromages", 8.5, ("Mozzarella", "Emental", "Parmesan", "Brie"))
# pizza1.Afficher()

pizzas = [Pizza("4 fromages", 8.5, ("Mozzarella", "Emental", "Parmesan", "Brie"), True),
          Pizza("Fruits de mer", 10, ("Crevettes", "Calamar", "Thon", "Mozzarella")),
          Pizza("Saumon", 11.5, ("Saumon fumé", "Parmesan", "sauce tomate")),
          Pizza("Kebab", 7.99, ("Kebab", "Champignon", "Mozzarella", "Poivrons")),
          Pizza("Végétarienne", 10.7, ("Mozzarella", "Tomates", "Oingons", "Poivrons"), True),
          PizzaPersonalisee(),
          PizzaPersonalisee()
          ]

def tri(e):
    return len(e.ingrediants)
#pizzas.sort(key= tri)

for pizza in pizzas:
    pizza.Afficher()