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
----------------------------
Pour éditer un fichier plusieurs commandes/éditeurs sont possibles : 
- `nano`(dans ce cour)
- `vi`
- `emacs`