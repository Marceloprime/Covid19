from googlesearch import search


#Primeira verificacao
#Filtro fraco
print('epedemia:\n')
string = '"epedemia"'
google = 'google'
for resultado in search((string+google), num_results=10):
	print(resultado)

print('\nVírus:\n')
virus = '"vírus"'
google = 'google'
for resultado in search((virus+google), num_results=10):
	print(resultado)

print('\nWHO:\n')
whc = '"Emergencies"'
google = 'https://www.who.int'
for resultado in search((whc+google), num_results=10):
	print(resultado)


print('\nMinistério da Saúde:\n')
saude = '"grave"'
google = 'saude'
for resultado in search((saude+google), num_results=10):
	print(resultado)

