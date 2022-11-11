import os

os.system('sudo apt install whois')
os.system('sudo apt install curl')
os.system('curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py')
os.system('python3 get-pip.py')
os.system('export PATH="$HOME/.local/bin:$PATH"')
os.system('rm get-pip.py')
os.system('pip install virtualenv')
os.system('git config --global user.email "aferrei3@binghamton.edu"')
os.system('git config --global user.name "aferrei3')


os.system('sudo apt-get install apt-transport-https ca-certificates gnupg')
os.system('echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list')
os.system('curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo tee /usr/share/keyrings/cloud.google.gpg')
os.system('sudo apt-get update && sudo apt-get install google-cloud-cli')
os.system('gcloud init')
