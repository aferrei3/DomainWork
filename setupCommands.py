#base installs
sudo apt-get update
sudo apt install whois
sudo apt install curl

#installing pip
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python3-pip

#git config
git config --global user.email "aferrei3@binghamton.edu"
git config --global user.name "aferrei3"

#virtualenv install
pip install virtualenv
virtualenv googenv
googenv/Scripts/activate
googenv/Scripts/pip install google-cloud-domains

#google cloud install & init
sudo apt-get install apt-transport-https ca-certificates gnupg
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo tee /usr/share/keyrings/cloud.google.gpg
sudo apt-get update && sudo apt-get install google-cloud-cli
gcloud init


#npm initialization and install
sudo apt install npm
npm init -y
npm i body-parser mongoose express

#install robo 3t
sudo snap install robo3t-snap

