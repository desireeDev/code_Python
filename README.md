

📁 Projet — Analyse d’investissements clients (Partie 1, 2, 3)

Ce projet contient trois fichiers Python (`Partie_1.py`, `Partie_2.py`, `Partie_3.py`) permettant de traiter, analyser, classer et visualiser les données d’investissement de différents clients.
### ▶️ Comment exécuter les fichiers

#### ✅ Partie_1.py

Ce fichier traite la structure de données initiale (clients, investissements) et :

Affiche la liste des noms des clients
Calcule pour chaque client :
   Le total investi
   La moyenne des investissements
   Le dernier investissement
   Génère une nouvelle liste résumée de tuples

#### ✅ Partie_2.py

Ce fichier utilise les données de `Partie_1.py` pour :

Classer les clients selon leur niveau d’investissement (`Faible`, `Moyen`, `Haut`)
Simuler un capital final à 1 an basé sur un taux propre à chaque client
 Trier et afficher les clients selon leur capital final décroissant

#### ✅ Partie_3.py (**option recommandée**)

Ce fichier est la version la plus complète. En l'exécutant, tu auras :

Accès à toutes les analyses résumées (`resume_client(nom)`)
Génération automatique d’un diagramme en barres des capitalisations finales
Un point d’entrée principal (`if __name__ == "__main__"`) qui centralise les résultats

### 📌 Recommandation

Même si vous pouvez exécuter `Partie_1.py` et `Partie_2.py` séparément pour voir les étapes intermédiaires, il est recommandé de  lancer directement `Partie_3.py` pour obtenir une vue complète et interactive du projet.


### 💡 Prérequis

Assurez-vous que les bibliothèques suivantes sont installées :

```bash
pip install matplotlib

### ✅ Exemple d’exécution

```bash
python Partie_3.py
```

Cela affichera :

* Un résumé complet d’un client (ex: Jean)
* Un graphique interactif représentant les capitalisations finales de tous les clients


![WhatsApp Image 2025-05-11 at 17 57 04](https://github.com/user-attachments/assets/d5774a1a-3df7-47a5-baed-2d12640c470d)

![WhatsApp Image 2025-05-11 at 17 57 05](https://github.com/user-attachments/assets/c3d64b84-9b17-4a7c-a84c-fdd92d1736ba)

