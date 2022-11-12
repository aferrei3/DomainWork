import os

domain_file = open('purchasable_domains.txt', 'r')
lines = domain_file.readlines()

o_file = open('available.txt', 'w')
for line in lines:

    os.system(f'gcloud domains registrations get-register-parameters {line}')



