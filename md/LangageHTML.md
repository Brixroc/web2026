### Des notions de HTML 
 
 1 . HTML
 HyperText Markup Language ( langage de balise hypertexte)

 => un fichier `.html` c'est d'abord du texte
 => il est écrit par un `développeur` (exemple écrit avec VSCode)
 => il est vu par un utilisateur ( avec Firefox par exemple)


  Une balise html s'écrit : `<mBalise></mBalise>`

  **Exemple**: `<h1></h1>`

  Le texte s'écrit **entre les balises**

  **Exemple** : `<h1>Mon texte</h1>`

  Il existe aussi des balises orphelines : `<!DOCTYPE html>`,`<br>`,`<img>`...

  Référence : Mozilla [https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements)

  Une balise ouvrante peut contenir un attribut nottamment `class=""`:

  `<h1 class="maClasse"></h1>`

  Quelques balises importantes:
  - `<h1></h1>`  : pour faire des titres
  - `<p></p>`    : pour faire des paragraphes
  - `<a href=""></a>`  : pour faire des liens
  - `<ul></ul>`      : pour faire des listes sans ordre
  - `<ol></ol>`       : pour faire des listes avec ordre
  - `<li></li>`       : pour faire des iteme de liste
  - `<img src=""></img>`  : pour ajouter une image

  Pour trouver le chemin vers un fichier, on peut regarder:
  - dans le dossier courant avec `./`
  - dans un dossier exterieur avec `../`

  2. CSS 
  Cascading Style Sheet : page de style en cascade
  On peut ecrire du CSS : 
  - directement dans le fichier HTML entre les balises `<style></style>`
  - dans un fichier `CSS`

  Pour écrire du CSS, il faut un sélecteur (nom d'une balise ou d'une clss),des accolades, des propriétés, des valeurs.

  ```CSS
  selecteur{
    propriete1 : valeur1;
    propriete2 : valeur2;
    ...
  }
  ```
  (modification pour le garder)