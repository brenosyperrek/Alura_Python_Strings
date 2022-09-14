from extratorurl import ExtratorURL 

url = "https://bytebank.com/cambio?moedaDestino=Dolar&moedaOrigem=real&quantidade=100"

extrator_url = ExtratorURL(url)
print(extrator_url)
print(len(extrator_url))

parametro = extrator_url.get_valor_parametro("quantidade")
print (parametro)

