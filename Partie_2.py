
# =================== CONTROLE ET DECISIONS ===================

import Partie_1 as p1
#Fonction de récupération du taux
def get_taux(nom):
    for client in p1.clients:
        if client[0] == nom:
            return client[2]
    return None  # au cas où le nom est introuvable


# =================== 4. Classement des clients par niveau d'investissement ===================
# - Faible, moyen, haut
# - Faible: total_investi < 30.000
# - Moyen: 30.000 < total_investi < 70.000
# - Haut: total_investi > 70.000

print("\n=== CLASSEMENT DES CLIENTS ===")
criteres = []
for client in p1.new_list:
    nom = client[0]
    total_investi = client[1]
    if total_investi < 30000:
        critere = "Faible"
    elif 30000 <= total_investi <= 70000:
        critere = "Moyen"
    else:
        critere = "Haut"
    print(f"Le client {nom} est classé comme {critere}.")
    criteres.append((nom, critere))

# =================== 5. Simulation de capital final ===================


for client in p1.new_list:
    nom = client[0]
    total = client[1]
    taux = get_taux(nom)
    capital_final = total * (1 + taux / 100)
    print(f"{nom} : Total = {total} FCFA | Taux = {taux} % | Capital final = {capital_final} FCFA")

# =================== 6. Classement par capital final décroissant ===================
capital_final_list = []
for client in p1.new_list:
    nom = client[0]
    total = client[1]
    taux = get_taux(nom)
  
    capital_final = total * (1 + taux / 100)
    capital_final_list.append((nom, capital_final))
     #Tri par capital final décroissant
capital_final_list.sort(key=lambda x: x[1], reverse=True)

  # Affichage
print("\n--- Classement par capital final décroissant ---")
for nom, capital in capital_final_list:
    print(f"{nom} : {capital} FCFA")