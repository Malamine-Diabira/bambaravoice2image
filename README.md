# Bambara Voice to Image Generation

Ce projet vise à développer un système capable de convertir des descriptions vocales en langue Bamanankan en images correspondantes. Il utilise des modèles d'apprentissage automatique pour transcrire la parole, traduire le texte et générer des images à partir de descriptions.

# Fonctionnalités
Transcription vocale : Utilisation de l'API Kabakoo pour transcrire la parole Bamanankan en texte.
Traduction : Utilisation du modèle de traduction de Hugging Face pour traduire le texte Bamanankan en anglais.
Génération d'images : Utilisation de différents modèles, tels que Stable Diffusion, CLIP, et DALL-E pour générer des images à partir du texte.

# Comment essayer le projet ?

Cloner le dépôt : Clonez ce dépôt sur votre machine locale.

Copier le code :
git clone https://github.com/Malamine-Diabira/Bambaravoice2image.git
Installer les dépendances : Installez les dépendances Python nécessaires en utilisant pip.

Copier le code
pip install -r requirements.txt
Démarrer l'application : Lancez l'application Flask en exécutant le fichier app.py.

Copier le code :  python app.py
Accéder à l'interface utilisateur : Ouvrez votre navigateur et accédez à l'adresse http://127.0.0.1:5000.


Visualiser l'image générée : Une fois le fichier audio transcrit, traduit et l'image générée, vous pouvez visualiser l'image résultante sur l'interface utilisateur.

# Génération d'images avancée (pour les utilisateurs avec GPU)
Pour explorer des modèles de génération d'images avancés tels que Stable Diffusion, utilisez le notebook Colab fourni.

Ouvrez le notebook Colab  https://colab.research.google.com/drive/1DyAxZEVqtBXSRzGF58ZaJojDkpqnsuPG?usp=sharing dans Google Colab.

Exécutez les cellules du notebook pour tester différents modèles de génération d'images.

Explorez les résultats et comparez les performances des différents modèles.

# Améliorations potentielles
Utilisation de modèles plus précis : Intégrez des modèles plus précis comme DALL-E pour une génération d'images plus précise.
Interface utilisateur améliorée : Améliorez l'interface utilisateur en ajoutant des fonctionnalités telles que la visualisation de l'historique des résultats et la personnalisation des préférences.
Optimisation des performances : Optimisez les performances du système en réduisant les temps de traitement et en améliorant la précision des résultats.

# Contribution
Les contributions à ce projet sont les bienvenues ! N'hésitez pas à ouvrir une issue pour discuter de nouvelles fonctionnalités ou à soumettre une pull request avec des améliorations.



