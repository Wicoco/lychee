## 🚦 Pipeline CI/CD

**Vérification des liens (`lychee_check`)**  
   Passe Lychee sur le site généré pour détecter tout lien mort (internes, externes, mailto ignorés).  
   - **Si des liens morts sont trouvés, le pipeline échoue.**
   - Le rapport associé `lychee-report.txt`.
   - Vous pouvez ajouter des exclusions dans le script CI si besoin (`lychee --exclude ...`).

## 👩‍💻 Usage et contribution

- **Tout commit/MR déclenche build + vérification des liens**
- **Corrigez les liens morts avant de demander une merge request**
- Le rapport détaillé est consultable dans l’onglet _CI/CD > Pipelines_ puis via "Artifacts" sur `lychee/lychee-report.txt`
- L’exclusion de liens spécifiques se fait dans la commande Lychee du CI ou via un fichier d’exclusion (voir [docs Lychee](https://lycheetweaker.readthedocs.io/en/docs-1.20/))