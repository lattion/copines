import os

# Le dossier cible
dossier = "img"

print(f"Démarrage de la restauration dans le dossier : {dossier}")

# On parcourt tous les fichiers du dossier
for fichier in os.listdir(dossier):
    # On sépare le nom et l'extension (ex: "1_2" et ".jpg")
    nom, extension = os.path.splitext(fichier)
    
    # On vérifie que le fichier a bien été modifié avec "_2"
    if nom.endswith("_2"):
        # On enlève les 2 derniers caractères du nom (le "_2")
        nouveau_nom = f"{nom[:-2]}{extension}"
        
        ancien_chemin = os.path.join(dossier, fichier)
        nouveau_chemin = os.path.join(dossier, nouveau_nom)
        
        # Action de renommage
        os.rename(ancien_chemin, nouveau_chemin)
        print(f"✅ Restauré : {fichier}  ->  {nouveau_nom}")

print("\nOpération inverse terminée ! Tu peux maintenant faire ton dernier Commit et Push sur GitHub.")