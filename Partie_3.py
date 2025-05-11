# =================== EXPLORATION FACULTATIVE / BONUS ===================
import matplotlib.pyplot as plt
import Partie_1 as p1
import Partie_2 as p2
# =================== 7. Fonction résumé client : resume_client(nom) ===================

def resume_client(nom):
    from Partie_2 import criteres

    # Vérifier si le client existe
    for client in p1.clients:
        if client[0] == nom:
            investissements = client[1]
            taux = client[2]
            break
    else:
        print(f"Le client {nom} n'existe pas, sorry.")
        return

    # Calculs
    total_investi = sum(investissements)
    montant_moy = total_investi / len(investissements)
    capital_final = total_investi * (1 + taux / 100)

    # Récupérer classement déjà calculé
    for c in criteres:
        if c[0] == nom:
            critere = c[1]
            break
    else:
        critere = "Inconnu"

    # Affichage
    print(f"\n--- Résumé du client {nom} ---")
    print(f"Investissements : {investissements}")
    print(f"Total investi : {total_investi} FCFA")
    print(f"Montant moyen investi : {montant_moy} FCFA")
    print(f"Classement : {critere}")
    print(f"Capital projeté : {capital_final} FCFA")

# =================== 8. Diagramme en barres des capitalisations finales ===================

def diagramme_capitalisation():
    clients = p1.names_list
    capital_final = []

    for nom in clients:
        # Trouver le total investi dans p1.new_list
        for client in p1.new_list:
            if client[0] == nom:
                total = client[1]
                break
        else:
            print(f" Données non trouvées pour {nom}")
            continue
        taux = p2.get_taux(nom)
        capital_final_value = total * (1 + taux / 100)
        capital_final.append(capital_final_value)

    # Création du graphique
    plt.figure(figsize=(10, 8))
    plt.bar(clients, capital_final, color='orange')
    plt.xlabel('Clients')
    plt.ylabel('Capital Final (FCFA)')
    plt.title('Capitalisation Finale par Client')
    plt.xticks(rotation=45)

    plt.show()
# =================== 9. Fonction principale ===================
if __name__ == "__main__":
    #Possibilité de tester les autres noms if u want
    resume_client("Jean")
    diagramme_capitalisation()

