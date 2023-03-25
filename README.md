# Git_Linux
## Dashboard Project
http://127.0.0.1:8050/


## TDs
### TD1

#### Exercice 1

cd /

ls

pwd

mkdir test

cd /home

cd ~

cd /home

cd /

cd ~

mkdir test

cd test

pwd

#### Exercice 2: Créer, renommer, copier, supprimer


cd ~

pwd

mkdir linux_ex_1

cd linux_ex_1

touch [first_name]_[last_name].txt

mkdir notes

mv [first_name]_[last_name].txt notes/

mv notes/[first_name][last_name].txt notes/[first_name][last_name]_$(date +%Y).txt

cp -r notes notes_2022

rm -rv notes



#### Exercice 3: Créer et exécuter un script



cd ~/linux_ex_1

echo 'Script running please wait ... Done.' > script_1.sh

cat script_1.sh

sh script_1.sh



#### Exercice 4.1 : Modifier les droits pour accéder ou modifier un fichier



cd ~/linux_ex_1

a. echo "fake personal information" > credentials

b. cat credentials

c. ls -l credentials

chmod a=r credentials

a. ls -l credentials

b. nano credentials

c. cat credentials

chmod a=rw credentials

a. ls -l credentials

b. nano credentials

c. cat credentials

d. chmod u+x credentials

e. ls -l credentials

chmod o-r credentials

a. ls -l credentials

chmod a=rwx credentials

a. ls -l credentials



#### Exercice 4.2: Accéder aux fichiers root



cd /

sudo touch .private_file

a. echo "Some information" | sudo tee .private_file

b. cat .private_file

c. ls -a

echo "New information" > ~/.private_file

a. cat ~/.private_file

sudo echo "New information added by root" >> ~/.private_file

a. cat ~/.private_file

sudo chmod a=rwx ~/.private_file

a. echo "Even newer information" > ~/.private_file

b. cat ~/.private_file

#### Exercice 4.3: Changer le propriétaire d'un fichier




chmod a+rw ~/.private_file

sudo chown $USER ~/.private_file

chmod a+rw ~/.private_file



#### Exercice 4.4: Gérer les paquets (outils/fonctions)



sudo apt update

sudo apt upgrade

sudo apt install cmatrix

cmatrix

Ctrl+c

sudo apt install tmux

tmux

echo "Hello session 0"

tmux new-window cmatrix

Ctrl+b d

tmux new-session -s session1

echo "Hello session 1"

Ctrl+b d

tmux ls

tmux attach-session -t 0

Ctrl+b d

tmux attach-session -t 1

Ctrl+b d



### TD2 



#### Exercise 1: Access general computer informations



sudo apt-get update && sudo apt-get upgrade -y

uname -a

top

htop

lscpu

df -h

mount

lsusb

hostname



#### Exercise 2: Shell - Variables and scripts scope



x="piri pimpin"

echo $x

x+=" piri pimpon"

mkdir my_programs

cd my_programs

echo "pilou pilou" > pilou

./pilou

chmod +x pilou

pilou

echo $PATH

export PATH=$PATH:/path/to/current/location

export PATH

cd ~

pilou

echo 'export PATH=$PATH:/path/to/current/location' >> .profile

Open a new terminal and run pilou.



#### Exercise 3: Scheduling task - daemon



echo "echo date +%F-%T Hello >> hellos.txt" > say_hello.sh

chmod +x say_hello.sh

crontab -e

/path/to/say_hello.sh



#### Exercise 4: Hashing



mkdir hash_checksum

cd hash_checksum

touch .sensible_addresses .sensible_passwords

ls -la

echo "echo 'Have a good day'" > gentle_script.sh

chmod +x gentle_script.sh

sha256sum gentle_script.sh > log_sha

echo "rm -rf .sensible*" >> gentle_script.sh

sha256sum gentle_script.sh > log_sha

./gentle_script.sh

ls -la

cat log_sha



#### Exercise 5: Compressing



sudo apt-get install qpdf -y

mkdir compress

cd compress

echo "Hello" > hello

zlib-flate -1 < hello > hello.deflate

wc -c hello.deflate > log_compress

seq -f "Hello %g" 1000 > hello_multiple

for i in {1..100}; do echo "Hello $i" >> hello_multiple_i; done

zlib-flate -1 < hello_multiple_i > hello_multiple_i.deflate

wc -c hello_multiple_i.deflate >> log_compress

wc -c hello.deflate hello_multiple.deflate hello_multiple_i.deflate

awk '{printf "%d\n", 100*$1/664}' log_compress

The compression ratio decreases as the file size and the randomness of the content increase.



#### Exercise 6: ACLs : Access Control Lists



sudo useradd client_1 -p passwd-client_1

sudo useradd contributor_1 -p passwd-contributor_1

sudo useradd contributor_2 -p passwd-contributor_2

sudo groupadd clients

sudo groupadd contributors

sudo usermod -a -G clients client_1

sudo usermod -a -G contributors contributor_1

sudo usermod -a -G contributors contributor_2

getent group clients contributors

sudo mkdir lika_project

sudo chown root:clients lika_project

sudo chmod 750 lika_project

sudo setfacl -m g:contributors:rwX lika_project

ls -l

su - client_1

rm -r lika_project

su - contributor_1


