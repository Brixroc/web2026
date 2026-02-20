# 1
mkdir tpLinux
# 2 
tree
# 3 
cd /workspaces/web2026/tpLinux
touch fic1.txt 
touch fic2.txt
touch fichier.md
touch image.jpg
touch exos.md
touch exoos.txt
# 4
mkdir dosA
cd /workspaces/web2026/tpLinux/dosA
mkdir dosB
mkdir dosC
cd /workspaces/web2026/tpLinux
mkdir dosD
# 5
mv /workspaces/web2026/tpLinux/fic1.txt /workspaces/web2026/tpLinux/dosA/dosB/fic1.txt
mv /workspaces/web2026/tpLinux/fic2.txt /workspaces/web2026/tpLinux/dosA/dosB/fic2.txt
mv /workspaces/web2026/tpLinux/fichier.md /workspaces/web2026/tpLinux/dosA/dosB/fichier.md
# 6
cd /workspaces/web2026/tpLinux/dosB
mv /workspaces/web2026/tpLinux/fic1.txt /workspaces/web2026/tpLinux/dosA/fic1.txt
mv /workspaces/web2026/tpLinux/fic2.txt /workspaces/web2026/tpLinux/dosA/dosC/fic2.txt
mv /workspaces/web2026/tpLinux/fichier.md /workspaces/web2026/tpLinux/dosA/dosD/fichier.md


# 7
cd /workspaces/web2026/tpLinux
echo -e "bonjour tout le monde" > fic1.txt
ls -l fic1.txt
# 8

# 9
mv /workspaces/web2026/tpLinux/exoos.txt /workspaces/web2026/tpLinux/exos.txt

# 10
cd /workspaces/web2026
touch supprimer.sh
nano supprimer.sh
rm -r ./tpLinux
tree
controle x pour quitter
chmod 766 ./supprimer.sh
./supprimer.sh