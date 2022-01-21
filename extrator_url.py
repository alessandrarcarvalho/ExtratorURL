import re
class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        padrao = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao.match(self.url)
        if not match:
            raise ValueError("A url é inválida")


        if not self.url:
            raise ValueError("A URL está vazia.")


    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indices_interrogation = self.url.find('?')
        url_parametros = self.url[indices_interrogation + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):

        indice_valor = self.get_url_parametros().find(parametro_busca) + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor


url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=105"
extrator_url = ExtratorURL(url)

#extrator_url = ExtratorURL("    ")
valor_quantidade = extrator_url.get_valor_parametro("moedaDestino")
print(valor_quantidade)
