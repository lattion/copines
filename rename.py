import os

# Le dossier cible (à modifier si tu veux aussi le faire pour le dossier 'personnes')
dossier = "img"

print(f"Démarrage du renommage dans le dossier : {dossier}")

# On parcourt tous les fichiers du dossier
for fichier in os.listdir(dossier):
    # On sépare le nom et l'extension (ex: "1" et ".JPG" ou ".HEIC")
    nom, extension = os.path.splitext(fichier)
    
    # On cible uniquement les images
    if extension.lower() in ['.jpg', '.jpeg', '.png', '.heic']:
        
        # On ajoute "_2" pour éviter les conflits et on force l'extension en minuscule
        nouveau_nom = f"{nom}_2{extension.lower()}"
        
        ancien_chemin = os.path.join(dossier, fichier)
        nouveau_chemin = os.path.join(dossier, nouveau_nom)
        
        # Action de renommage
        os.rename(ancien_chemin, nouveau_chemin)
        print(f"✅ Renommé : {fichier}  ->  {nouveau_nom}")

print("\nOpération terminée ! Tu peux maintenant faire ton Commit et Push sur GitHub.")