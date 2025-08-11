Current Work In Progress



# This tutorial is based off a DEFCON 33 lab from the Packet Hacking Village (2025)
### ***https://github.com/malwaredllc/byob***
**This lab consisted of familization of bot nets and building your own bot.**
**This will have the botnet setup, with quick reference how to use the bot net and how it can be weaponized for educational purpose and understanding.**

# Setup
***https://www.youtube.com/watch?v=uVyniPrTzuk***
The following is a step by step guide of the provided video from the creator. 

### Linux Setup
* **Install a VM of Linux**
* **Ensure that you have python and docker installed**
* *The script will not run unless you have python and docker installed*
* **Install docker using**
```
sudo apt-get install docker.io -y
```
* **Install python using**
```
sudo apt install python
```
* **Ensure that you have *git* installed as well
```
sudo apt install git
```
* **Install *pipenv*
```
sudo apt install pipenv
```
-------------------------------------
**Because Linux has messed up the python library so bad in its system. It is encouraged to use a pipenv shell when running the byob. The reason is for easier to download needed library that will be required.**
* You will need the following from a fresh install from the pipenv shell
```
pip install flask
pip install flask_bcrypt
pip install flask_login
pip install colorama
pip install requests
pip install flask_sqlalchemy

```
-------------------------------------
**Now that we have all the needed resources installed, we can move to the next section

### Download the GitHub

**To download the GitHub, we will use the following command**
```
git clone https://github.com/malwaredllc/byob
```

### Changing directory

**Make sure you open a terminal and are in the home by using this command**
```
cd ~
```

**Now that the new directory is created, we will have to change to it.**
```
cd byob
cd web-gui
```
**We just entered the byob directory and used the command *cd web-gui* to go into the new folder. This is where the build starts**

### Setting up Docker

**We will have to have Docker started before we begin building the *byob* system.**
You must have docker running before you begin building

**Use the following command to start your Docker**
```
sudo systemctl start docker
```

**Double check it is running with this command**
```
sudo service docker status
```

**You should have a return that looks like this**
```
● docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; preset: enabled)
     Active: active (running) since Mon 2025-08-11 13:53:35 EDT; 1min 7s ago
 Invocation: 9f3d260a91c34d40bb81d4fa2e1aee47
TriggeredBy: ● docker.socket
```
*This shows that the docker is active and running*

### Running *startup bash script*

**Now that Docker is started and running, we can run the *startup.sh* with the following command**
*Double check you are still in the directory of the web-gui to start the bash script*

```
sudo ./startup.sh
```
Now we wait for the complete build. This will take some time as the docker needs to build and download the entire environment.

### Pyrex fail - How to fix
**Sometimes the pyrex will fail. This is a common error for some systems but not always. If you run into this error do the following**

* Open the directory path back to the *web-gui*
* Once there, use the command to edit the requirements.txt from the directory
```
sudo nano requirements.txt
```
* Go to the *pirexx*
```
git+https://github.com/jtgrassie/pyrex.git#egg-pyrex
```
***Note this is not in newer versions of byob but if you are running an older version here is the documented fix by the creator***
***If you run into this problem and fix the *requirements.txt* rerun the startup bash again***


