# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 23:29:44 2021

@author: Adriano Paul
"""

import requests as r
import json
import pandas as pd

class empenhos(object):
    def __init__(self, ano=2021, favorecido=30815452000192, fase=1, pag=''):
        self.ano = ano
        self.favorecido = favorecido
        self.fase = fase
        self.pag = pag
        
        self.dados = r.get('http://api.portaldatransparencia.gov.br/api-de-dados/despesas/documentos-por-favorecido', 
                    params={"ano":self.ano, "codigoPessoa":self.favorecido, "fase":self.fase, "pagina":self.pag}, 
                    headers={"chave-api-dados":''})
        self.dados = pd.DataFrame(self.dados.json())
        
        self.dados.valor = self.dados.valor.apply(lambda x: x.replace(",", "."))
        self.dados.valor = self.dados.valor.apply(lambda x: x.replace(".", "", x.count(".") -1))
        self.dados.valor = self.dados.valor.astype(float)
        
        print("{} recebeu um total de {} empenhos no valor total de R${} em {}.".format(
            self.dados.nomeFavorecido[0],len(self.dados), round(sum(self.dados.valor),2), self.ano))
        
        self.dados.to_html("{}-{}.html".format(self.dados.nomeFavorecido[0],self.ano),justify='center')
        

ano = 2020
favorecido = 30815452000192
fase = 1
pag = ''

a = empenhos(ano,favorecido,fase,pag)

docs = r.get('http://api.portaldatransparencia.gov.br/api-de-dados/despesas/documentos-por-favorecido', 
                    params={"ano":ano, "codigoPessoa":favorecido, "fase":fase, "pagina":pag}, 
                    headers={"chave-api-dados":'e17daebe3e3913ccc6575af267ff484e'})
df = pd.DataFrame(docs.json())





cols = list(docs_py.columns)
docs_py.valor = docs_py.valor.apply(lambda x: x.replace(",", "."))
docs_py.valor = docs_py.valor.apply(lambda x: x.replace(".", "", x.count(".") -1))
docs_py.valor = docs_py.valor.astype(float)



documento = '423034422072020NE800429'
fase = 1
rel = requests.get('http://api.portaldatransparencia.gov.br/api-de-dados/despesas/documentos-relacionados', 
                   params={"codigoDocumento":documento, "fase":fase},  
                   headers={"chave-api-dados":'e17daebe3e3913ccc6575af267ff484e'})
rel_py = rel.json()
print(json.dumps(rel_py, sort_keys=True, indent=4))
