import requests
#from clientes.models import Cliente,Produto

response = requests.get("http://challenge-api.luizalabs.com/api/product/?page=1")
products = response.json()

print(products)

for product in products['products']:
    #Produto.objects.create(title=product['title'])
    print(product['title'])