import subprocess
import sys

def get_domains_from_file(filename):
    with open(filename) as f:
        return f.readlines() 

def verify_domains(domains, lookup_command):
    valid_domains = []
    for domain in domains:
        domain_string = lookup_domain(domain.strip(), lookup_command) 
        if domain_string != '':
            valid_domains += [domain_string]
    return valid_domains
    


def lookup_domain(domain, lookup_command):

    if lookup_command == "whois":
        command = "whois {} | grep 'This query returned 0 objects'".format(domain)
    elif lookup_command == "nslookup":
        command = "nslookup {} | grep -i \"Can't find\"".format(domain)
    else:
        print("Invalid domain lookup command provided. Exiting...")
        sys.exit()

    command_output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    if command_output.returncode == 0:
        print("Domain {} does not exist".format(domain))
        return domain
    else:
        print("Domain {} exists".format(domain))
        return '' 





o_file = open("available_domains.txt")






        
domain_file = input('ENTER DOMAIN FILE NAME')
o_file_name = input('ENTER OUTPUT FILE')
o_file = open(o_file_name,'w')
domains = get_domains_from_file(domain_file)
valid_domains = verify_domains(domains,"nslookup")
for i in valid_domains:
    o_file.write(i)
    o_file.write('\n')

