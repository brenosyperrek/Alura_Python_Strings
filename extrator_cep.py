endereco = "Rua Jornalista Narbal Vilela 225, João Paulo, Florianópolis, SC, 88030-500"

import re

padrao = re.compile("[0-9]{5}[- ]?[0-9]{3}")
busca = padrao.search(endereco)
print(busca)

if busca:
    cep = busca.group()
    print (cep)
else:
    print ("CEP não encontrado")