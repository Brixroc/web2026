## 1. Système d'éxploitation

> Un système d’exploitation (SE) est un programme (ou un ensemble de programmes) qui assure la communication
entre le matériel (hardware) et les logiciels (software)

=> operating systeme(os)
!!! note Principaux OS
Les principauxos sont : 
- **Windows** Microsoft
- **MacOs** Apple
- **Unix** Solaris
- **ChromeOs** Google
- **Android** Google
- **Ios** Apple
- **FreeBSD**
- **Gnu/Linux**

Les 6 premiers sont des logiciels propriétaires tandis que les deux derniers sont **libres**.

A l'exception de **Windows**, tous ces OS appartiennent à la famille *Unix-Like* : les commandes sont standardisées.
!!!

rem:
> « First, the freedom to copy a program and redistribute it to your neighbours, so that they can use
it as well as you. Second, the freedom to change a program, so that you can control it instead of it
controlling you ; for this, the source code must be made available to you » (Richard Stallman, Free Software Fundation)

Quelques exemples de logiciels libres : Linux, Python, FireFox, LibreOffice, Gimp, OBS Studios,...


## 2. Le père de tous les os : UNIX

Il est développé en 1971/1972 par K.thompson et D.Ritchie. Ils ont inventé **le langage C** pour écrire leur OS appelé UNIX.
Cet OS est célebre pour son interprete de commande appelé *Terminal* ou *Shell*

En 1991, un étudiant finlandais **Linus Torvald** envoie un mail avec une piece jointe contenant le noyau d'un système d'exploitation libre inspiré d'UNIX : **Linux**.


## 3. Quelques commandes dans le shell (bash)

Une commande s'écrit après le prompt qui se termine par le symbole `$`
Une commande possède toujours une syntaxe:
- le `nom` de la commande 
- des `options` facultatives
- des `arguments` facultatifs

Il existe une commande qui affiche l manuel/la documentation d'une autre commande passé en argument : `man`

Syntaxe générale: `nom --option argument` ou `nom -option argument`

|nom|rôle|exemple|
|---------|---------|-------|
|`whoami`|affiche le nom de l'utilisateur|`$ whoami`|
|`man`|affiche le manuel d'une autre commande|`$ man whoami`|
|`touch`|créer un fichier *vide*|`$ touch monfichier`|
|`ls`|le contenu d'un dossier|`$ ls -l`|
|`mkdir`|créer un dossier *vide*|`$ mkdir mondossier`|
|`nano`|éditer un fichier|`$ nano monfichier`|
|`cat`|affiche le contenu des fichiers|`$ cat monfichier`|
|`tree`|affiche l'arborescence du dossier courant`./`|`$ tree`|
|`pwd`|affiche le nom du dossier courant|`$ pwd`|
|`cd`|changer de répertoire courant|`$ cd./mondossier   `|
|`cp`|copie une source vers une direction|`$ cp ./monfichier ./mondossier`|
|`rm`|supprimer des fichiers ou des dossiers|`$ rm -r./mondossier `|
|`mv`|couper/renommer des fichiers|`$ mv ./monfichier ./nouveaunom `|
|`chmod`|modifie les permissions|`$ chmod 777 ./monfichier `|
----------------------------
Pour éditer un fichier plusieurs commandes/éditeurs sont possibles : 
- `nano`(dans ce cour)
- `vi`
- `emacs`
-------------------------------------------------------------------------------------
La commande `cd` (*change directory*) permet de se déplacer dans l'arborescence des dossiers.Sur Linux, le dossier **racine** (*root*) se note `/`.

On peut donner le chemin vers un dossier (un fichier) de magnère:
- relative (on commence par `./` ou `../`)
- absolue (on commence par `/`)

Linux rend facultatif l'utilisation de `./` 
Si on tape la commande `cd` sans arguments, on se déplace dans le répertoire "home".
=> `/home/utilisateur`

--------------------------------
La commande `cp` permet de copier une source vers une destination en la renommant éventuellement

```bash
$ cp cheminFichierSource cheminDossierDestination
```
en renomment
```bash
$ cp cheminFichierSource cheminDossierDestination/nouveaunom
```

----------------------
La commande `rm-r` permet de supprimer un dossier et tout se qu'il contient
--------------------

Il est possible d'écrire dans un fichier portant l'extantion `.sh` par défaut .Pour éxecuter ce fichier 
```bash
./monfichier.sh
```
Par défaut, les fichiers linux ne sont pas exécutable.Quand un fichier(dossier) est crée, il possède des **permissions** qui peuvent etre différentes pour : 
- `user` c'est le propriétaire du fichier
- `group` groupe d'utilisateur défini par `user`
- `other` le reste du monde

Les permissions sur un fichier(dossier) sont:
- *read* : `r` valeur = 4
- *write* : `w` valeur = 2
- *execute* : `x` valeur = 1

La commande `chmod nnn` permet de modifier les permissions ; il existe une autre syntaxe avec les lettres `u,g,o` (usre, groupe, other) et les symboles `+,-` pour ajouter ou retirer des droits.
```bash
chmod 754 ./monfichier.sh #rwx pour user, rx pour groupe et r pour other
```
```bash
chmod u-x,g-x,o+x ./monfichier.sh #retire x pour user et groupe, ajoute w pour other
```