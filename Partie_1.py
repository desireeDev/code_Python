# =================== TRAITEMENT DE LA STRUCTURE IMBRIQUÉE (LISTES ET TUPLES) ===================

# =================== 1. Création de la liste des noms des clients ===================

clients = [
    ("Jean", [10000, 12000, 8000], 3.5),
    ("Awa", [50000, 52000, 60000], 4.2),
    ("Paul", [25000], 3.8),
    ("Fatou", [75000, 70000], 5.0),
    ("Ali", [15000, 18000, 17000, 16000], 4.0),
]

names_list = []

for client in clients:
    nom = client[0]
    names_list.append(nom)

print("\n La liste de noms se présente comme suit :")
for nom in names_list:
    print(f" - {nom}")

# =================== 2. Calculs pour chaque client ===================

print("\n Détails des investissements :")
for client in clients:
    nom = client[0]
    investissements = client[1]
    total_investi = sum(investissements)
    montant_moy = total_investi / len(investissements)
    last_invest = investissements[-1]

    print(f"\nClient : {nom}")
    print(f"  ▸ Total investi              : {total_investi} FCFA")
    print(f"  ▸ Montant moyen investi      : {montant_moy:.2f} FCFA")
    print(f"  ▸ Dernier investissement     : {last_invest} FCFA")

# =================== 3. Affichage de la liste des tuples (nom, total, moyenne, dernier) ===================

new_list = []
print("\n La nouvelle liste de tuples (résumé) :")
for client in clients:
    nom = client[0]
    investissements = client[1]
    total_investi = sum(investissements)
    montant_moy = total_investi / len(investissements)
    last_invest = investissements[-1]
    tuple_data = (nom, total_investi, montant_moy, last_invest)
    new_list.append(tuple_data)
    print(f"  {tuple_data}")
