from azure.identity import ClientSecretCredential
from azure.mgmt.web import WebSiteManagementClient
from azure.mgmt.subscription import SubscriptionClient

# Substitua com suas credenciais e detalhes específicos
subscription_id = "bdfc5b78-7a9c-4d3e-a616-913a49e3e20c"
tenant_id = "8c974388-f2f1-4000-bd28-71fb59de657d"
client_id = "c5ca09ac-1156-473a-b647-73165c2e049d"
client_secret = "vEN8Q~_qB6idOJxrDfNVvB_HSPhaCnkVOIuO0cde"

# Autenticação usando credenciais de serviço principal
credentials = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)

# Cliente de gerenciamento de assinatura para obter detalhes da assinatura
subscription_client = SubscriptionClient(credentials)
subscription = next(subscription_client.subscriptions.list())

# Cliente de gerenciamento de Web App para buscar detalhes
web_client = WebSiteManagementClient(credentials, subscription_id)

# Nome da Web App que você deseja buscar
resource_group_name = 'WEB-APP-SERVICE'
web_app_name = 'nodejs-web-app-service'

# Buscar detalhes da Web App
web_app = web_client.web_apps.get(resource_group_name, web_app_name)

# Exibir o nome da Web App e o perfil do publicador

print(f"Web App Name: {web_app.name}")
print(f"Publisher Profile: {web_app.kind}")

# Se precisar de mais detalhes, pode explorar outros atributos disponíveis em 'web_app'