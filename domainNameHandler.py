file_name = input("ENTER NAME OF DOMAIN SUFFIX/PREFIX FILE\n")
domain_name = input("ENTER DOMAIN NAME\n")
o_file_name = input("ENTER NAME OF OUTPUT FILE\n")
o_file = open(o_file_name,'w')

extension_file = open("common_extensions.txt")
extensions = extension_file.readlines()


if '.com' in domain_name:
    domain_name = domain_name.rstrip('.com')

domain_words_file = open(file_name, 'r')

lines = domain_words_file.readlines()

for line in lines:
    if line[0] == '+':
       sufpref_string = line.lstrip('+')
       sufpref_string = sufpref_string.rstrip('\n')
       domain_string = domain_name + sufpref_string
    else:
        sufpref_string = line.rstrip('+\n')

        domain_string = sufpref_string + domain_name 

    for extension in extensions:
        o_file.write(domain_string + extension)






        
        
