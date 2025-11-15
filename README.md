from model.upgrade_strategy import AutoClickStrategyfrom model.upgrade_strategy import MultiplierStrategy

# Cookie Clicker Python – README

## 📌 Description

Ce projet est une version personnalisée de **Cookie Clicker** réalisée en Python avec **Pygame**. Le joueur clique sur une arme (ou un cookie) pour gagner de l'argent, puis peut acheter des upgrades pour augmenter sa production.

Le code est organisé en plusieurs modules :

* **core/** → gestion des événements et logique interne
* **model/** → état du jeu (GameState)
* **screens/** → gestion des écrans (GameScreen, BaseScreen…)
* **view/** → composants UI (boutons, images, texte)

---

## 🚀 Fonctionnalités

* Cliquer sur une arme/cookie pour gagner de l’argent
* Système complet d’**upgrades** avec niveaux
* Mise à jour automatique de l’affichage
* Architecture modulaire : facile à étendre
* Interface graphique réalisée avec Pygame

---

## 🛠️ Installation

### 1. Installer Python

Assure-toi d’avoir **Python 3.10+** installé.

### 2. Installer les dépendances

Dans un terminal :

```bash
pip install pygame
```

### 3. Lancer le jeu

```bash
python main.py
```

---

## 📁 Structure du projet

```
python_cookie_clicker/
│
├── core/
│   ├── event_manager.py
│   └── game_manager.py
│
├── model/
│   └── game_state.py
│
├── screens/
│   ├── base_screen.py
│   └── game_screen.py
│
├── view/
│   ├── button_components.py
│   ├── image_components.py
│   └── text_component.py
│
├── assets/
│   └── weapon.png
│
└── main.py
```

---

## 🎮 Comment jouer ?

* Lors du lancement, si c'est votre première partie, celle-ci se crée automatiquement.
* **Clique** sur l’arme / cookie pour gagner des points.
* **Achète des upgrades** dans le panneau à droite.
* Chaque upgrade augmente ta production ou donne des bonus spécifiques.

---

## 🧩 Ajouter un nouvel upgrade

Dans `game_manager.py`, ajoute une entrée dans `upgrades_available` :

```python
Upgrade(name="Super Speed", cost=50, strategy=MultiplierStrategy / AutoClickStrategy)
```

---

## 🔧 Configuration

Tu peux modifier la vitesse du jeu, les valeurs d’upgrades ou les images dans les fichiers :

* `GameState` → argent, production
* `assets/` → images
* `GameScreen` → interface

---

## 🐞 Débogage

En cas d'erreur Pygame :

* Vérifier que les chemins vers `assets/` sont corrects
* Vérifier les dimensions de la fenêtre
* Lancer avec `python -u main.py` pour afficher les logs

---

## 📜 Licence

Projet libre d'utilisation et de modification.

---

## 🤝 Contribution

N’hésite pas à proposer des améliorations ou demander d’autres fonctionnalités !
