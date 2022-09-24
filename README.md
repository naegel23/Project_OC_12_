# Project_OC_12_Django_ORM
Installation et exécution de l'application :
1 - Cloner le dépôt du projet à l'aide de la commande :

$ git clone https://github.com/naegel23/Project_OC_12_Django_ORM (vous pouvez également télécharger le code en temps qu'archive zip)
2 - Rendez-vous depuis un terminal à la racine du répertoireavec la commande :

3 - Créer un environnement virtuel pour le projet avec la commande :

$ python -m venv env sous windows
ou $ python3 -m venv env sous macos ou linux
4 - Activez l'environnement virtuel avec la commande :

$ env\Scripts\activate sous windows
ou $ source env/bin/activate sous macos ou linux
5 - Installez les dépendances du projet avec la commande :

$ pip install -r requirements.txt
6 - Créez la base de données avec les commandes suivantes :

$ python manage.py makemigrations epic_events_db2
$ python manage.py makemigrations
$ python manage.py migrate epic_events_db2
$ python manage.py migrate
7 - Créer l'admin avec la commande suivante :

$ python manage.py createsuperuser
8 - Démarrer le serveur avec la commande :

$ python manage.py runserver
