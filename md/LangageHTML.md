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
  - dans un fichier `.CSS` en indiquant le chemin dans le fichier HTML grace a la balise `<link>`

  Pour écrire du CSS, il faut un sélecteur (nom d'une balise ou d'une clss),des accolades, des propriétés, des valeurs.

  ```CSS
  selecteur{
    propriete1 : valeur1;
    propriete2 : valeur2;
    ...
  }
  ```
  Il existe plus de 500 propriétés et encore d'avantage de valeu possible. Cependant, les valeurs sont souvent:
  - une couleur : un nom(blue,white), un code(rgb(0-255, 0-255, 0-255))
  - une taille : il existe de nombreuses unités, pixels(px), pourcentage(%), ...
  
  Remarque : On trouve toute les propriété sur le site des dévelopeur de Modzilla 

 Les propriétés CSS s'appliquent en cascade : des éléments les plus globaux (`body`,`div`) vers les éléments les plus internes (pour finir par les classes).

 Rem: Principe du modèle en boite 
 Les éléments d'une page sont contenus dans une boite entourée d'une bordure(invisible par déaut)
 L'éspace entre:
 - le contenue et la bordure s'appelle `padding`
 - la bordure et les éléments autour s'appelle `margue ou margin`

 La bordure `border` peut meme avoir un style.
 [https://www.w3schools.com/css/css_boxmodel.asp](https://www.w3schools.com/css/css_boxmodel.asp)

 Rem: les conteneurs universels `<div></div>` et `<span></span>`

 Il existe de nombreuses propriétes relative au texte:
 - `text-align` 
 - `font`

 3. Javascript(JS)

C'est le langage de programmation qui permet de gérer les éléments intéractifs d'une page HTML.

Historiquement, les éléments d'interactions étaient placés dans un formulaire `<form></form>` pour renvoyer des informations au serveur.

Dans le formulaire on place les éléments `input type="">`:
- type = "texte"
- type = "checkbox"
- type = "button"
- type = "range"

Remarque: Une balise `<button type="button"></button>` a ete spécifiquement créée pour les boutons

On peut écrire le JS directement: 
- dans le fichier HTML entre des balises `<script></script>`
- dans un fichier externe avec l'extention .js


On utilise la balise `script` pour lier le fichier js

JS est utilise pour réagir aux évenements : `clique` , `change`, `mouseover`, ... 
La syntaxe basique est : 
```js
elementHTML.addEventListener("evenement", function(){...});
```