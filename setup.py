import os

os.system('sudo apt-get update')
os.system('sudo apt install whois')
os.system('sudo apt install curl')

os.system('sudo apt-get install software-properties-common')
os.system('sudo apt-add-repository universe')
os.system('sudo apt-get update')
os.system('sudo apt-get install python3-pip')

os.system('pip install virtualenv')

os.system('git config --global user.email "aferrei3@binghamton.edu"')
os.system('git config --global user.name "aferrei3')

os.system('virtualenv googenv')
os.system('googenv/Scripts/activate')
os.system('googenv/Scripts/pip install google-cloud-domains')


os.system('sudo apt-get install apt-transport-https ca-certificates gnupg')
os.system('echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list')
os.system('curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo tee /usr/share/keyrings/cloud.google.gpg')
os.system('sudo apt-get update && sudo apt-get install google-cloud-cli')
os.system('gcloud init')
