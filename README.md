# Azure Gaming

## Contexte
Projet Azure qui a pour but de créer un Cloud Gaming sur Azure.

#### Consignes
Le déroulé du projet est le suivant:
* Le joueur s’identifie sur son portail web
* Une fois authentifié, si il n’est pas autorisé, il ne peut pas lancer le jeu
* Si il est autorisé, il a un bouton ou un lien pour lancer le jeu
* Le lancement du jeu va démarrer une VM sur Azure et y déployer le jeu
* L’utilisateur peut alors accéder au jeu via une interface.
* Une fois la partie terminée, ou une fois le joueur déconnecté, ou après un
timeout définit par avance, la VM est éteinte dans le cloud.

#### Livrable
Le délivrable est en deux parties:
* Le site du portail web, ainsi que deux identifiants et mots de passe pour
pouvoir tester le projet. Un des identifiants ne doit pas permettre l’accès au
jeu.
* Un accès au code source du projet, avec sa documentation pour l’installer.

---

## Projet

#### Technologies utilisés
* React => frontend
* Flask => API
* Azure cloud => gestion des VMs

#### Décomposition du projet
Le projet est decomposé en plusieurs parties :
* le frontend : qui contient l'application 
* le backend : qui contient l'api

---
## Project setup

Installation à faire pour démarrer le projet

### Get the project

```
git clone https://github.com/dylanbrudey/cloud-gaming-portal.git
```

### Project setup (Frontend) 

#### Installation
```
yarn install
```
##### Ajout du secret

Placer *data.js* dans le dossier *src*

#### Lancer le front
```
yarn start
```

### Project setup (Backend)

#### Installation

##### Création d'un environnement virtuel

###### Windows
```
python -m venv ./api/venv
```
###### Unix
```
python3 -m venv ./api/venv
```
##### Lancement de l'environnement virtuel

###### Windows
```
.\api\venv\Scripts\activate
```
###### Unix
```
source api/venv/bin/activate
```
##### Installation des dépendances
###### Windows
```
pip install .\api\requirements.txt
```
###### Unix
```
pip3 install ./api/requirements.txt
```

##### Ajout du secret

Placer *config.py* dans le dossier *api*

#### Lancement de l'api
```
yarn start-api
```

---

## Login credentials
 Les secrets seront communiqués via une autre plateforme.
 Vous trouverez les identifiants d'autentification aux jeux du portail dans *identifiants_portail.txt*

---

## FAQ

1 - Shutdown automatique 

Un shutdown automatique de la vm est realisé à 01:00 chaque jour. Merci de realisé les tests avant ou après cette heure ci.

2 - Que se passe t-il quand je clique sur play ?

Un premier message indiquant que la machine virtuelle s'allume s'affiche.
Puis un deuxième apparaitra lorsque celle-ci sera allumée.
Et enfin, un dernier message s'affichera avec les identifiants et l'ip de la vm pour se connecter a distance (avec le rdp)

3 - Que se passe t-il quand je clique sur stop ?

Un premier message indiquant que la machine virtuelle s'éteint s'affiche.
Puis un deuxième apparaitra lorsque celle-ci sera éteinte.

4 - Comment se connecter en RDP ?

Sur Windows, utiliser la connexion de bureau à distance.
Sur Mac, installer Microsoft Remote Desktop.
Afin de se connecter, , ajoutee à l'adresse IP de la VM le port *3389* de la manière suivante XX.XXX.XXX.XX:3389.
