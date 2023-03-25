# Git_Linux
## Dashboard Project
http://127.0.0.1:8050/


## TDs
### TD1

#### Exercice 1

```
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
```
#### Exercice 2: Créer, renommer, copier, supprimer

```
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
```


#### Exercice 3: Créer et exécuter un script

```

cd ~/linux_ex_1

echo 'Script running please wait ... Done.' > script_1.sh

cat script_1.sh

sh script_1.sh

```

#### Exercice 4.1 : Modifier les droits pour accéder ou modifier un fichier

```

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


```
#### Exercice 4.2: Accéder aux fichiers root

```

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
```
#### Exercice 4.3: Changer le propriétaire d'un fichier

```


chmod a+rw ~/.private_file

sudo chown $USER ~/.private_file

chmod a+rw ~/.private_file
```


#### Exercice 4.4: Gérer les paquets (outils/fonctions)

```

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

```

### TD2 



#### Exercise 1: Access general computer informations

```

sudo apt-get update && sudo apt-get upgrade -y

uname -a

top

htop

lscpu

df -h

mount

lsusb

hostname


```
#### Exercise 2: Shell - Variables and scripts scope

```

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

```

#### Exercise 3: Scheduling task - daemon


```
echo "echo date +%F-%T Hello >> hellos.txt" > say_hello.sh

chmod +x say_hello.sh

crontab -e

/path/to/say_hello.sh
```


#### Exercise 4: Hashing


```
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
```


#### Exercise 5: Compressing


```
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
```


#### Exercise 6: ACLs : Access Control Lists


```
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
```

### TD3

#### Exercise 1: Grep and awk on tabular data
```
ls -l /

ls -l / | grep bin

ls -l / | grep bin | awk '{print $5}'

ls -l / | grep bin | awk '{print $6, $7, $8}'

ls -l / | grep bin | awk '{print $8 "-" $6 "-" $7}'
```
#### Exercise 2: Grep with Regex, and sed on unstructured data
```
curl https://en.wikipedia.org/wiki/List_of_cyberattacks > cyberattacks.txt

grep "meta" cyberattacks.txt

grep -o "meta \w+" cyberattacks.txt

grep -oP "(?<=meta )\w+" cyberattacks.txt

cat cyberattacks.txt | grep -A1 'mw-content-text' | grep -v 'mw-content-text'

grep -oP '(?<=<title>).*(?= - Wikipedia</title>)' cyberattacks.txt

cat cyberattacks.txt | grep "^=="

```
### TD4 

#### Exercice 1 
```
4 : #!/bin/bash
    REMOTE_SERVER="remote.server.com"
    PRIVATE_KEY_PATH="~/.ssh/my_private_key.pem"
    REMOTE_USERNAME="my_username"
    ssh -i $PRIVATE_KEY_PATH $REMOTE_USERNAME@$REMOTE_SERVER
5 : ./connect.sh
6 : mv key.pem .key.pem
    nano connect.sh
    ssh -i ~/.key.pem ec2-user@<your-instance-ip>
    ./connect.sh
  ```
#### Exercice 2
  ```
  1 : touch test_to_remote_instance.txt
2 : ssh username@remote_instance_ip_address
    touch test_from_remote_instance.txt
    exit
3 : scp test_to_remote_instance.txt username@remote_instance_ip_address:~
    scp username@remote_instance_ip_address:~/test_from_remote_instance.txt .
4 : if [ -z "$1" ]; then
        echo "Please provide the path of the file to send as an argument."
        exit 1
    fi

    if [ ! -f "$1" ]; then
      echo "The file $1 does not exist."
      exit 1
    fi
    scp "$1" username@remote_instance_ip_address:~

    if [ -z "$1" ]; then
        echo "Please provide the path of the file to receive as an argument."
        exit 1
    fi
    scp username@remote_instance_ip_address:"$1" .
5 : ./scp_to_remote_instance.sh /path/to/my_file.txt
    ./scp_from_remote_instance.sh ~/remote_file.txt
```

### TD7
  
#### Exercice 2
 ``` 
git checkout -b theo-morvillez
echo "Allez l'om" > theo-morvillez.txt
git add theo-morvillez.txt
git commit -m "Add theo-morvillez.txt"
git push origin theo-morvillez
  
```  
#### Exercice 3
```  
git checkout main #master ne marchait pas
git merge theo-morvillez
git push origin main
  
```
#### Exercice 4
```  
git checkout theo-morvillez
nano README.md
git add README.md
git commit -m "Edit lines 2-6 in README.md"
git checkout main
git pull origin main
git merge theo-morvillez
nano README.md
git add README.md
git commit -m "Resolve merge conflicts in README.md"
git push origin main
```  

#### Exercice 5
```  
git checkout main
git pull origin main
cat README.md
git checkout theo-morvillez
git merge main
git add README.md
git commit -m "Merge changes from main to theo-morvillez"
  
```
#### Exercice 6
 ``` 
git checkout main
git branch -d theo-morvillez
git push origin --delete theo-morvillez
```  

#### Exercice 7
 ``` 
git pull origin main
git checkout -b theo-morvillez
nano README.md
git add README.md
git commit -m "ce que l'on a fait"
git rebase -i HEAD~8
git push origin theo-morvillez
```
