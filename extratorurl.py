import re

class ExtratorURL:
    
    def __init__(self,url) -> None:
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""    

    def valida_url(self):
        if not self.url:
            raise ValueError("A url está vazia")
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.get_url_base())
        if not match:
            raise ValueError("A url não é válida")    

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_pametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1 :]
        return url_parametros

    def get_valor_parametro(self, nome_parametro):
        indice_parametro = self.get_url_pametros().find(nome_parametro)
        indice_valor = indice_parametro + len(nome_parametro) + 1
        indice_e_comercial = self.get_url_pametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_pametros()[indice_valor : ]
        else:
            valor = self.get_url_pametros()[indice_valor : indice_e_comercial]    
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return "Url: " + self.url +"\n" + "Parâmetros: " +self.get_url_pametros() + "\n" + "Base: " + self.get_url_base()