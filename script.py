from azure.identity import ClientSecretCredential
from azure.mgmt.web import WebSiteManagementClient
from azure.mgmt.subscription import SubscriptionClient

# Substitua com suas credenciais e detalhes específicos
subscription_id = ${{ secrets.AZURE_SUBSCRIPTION_ID }}
tenant_id = ${{ secrets.AZURE_TENANT_ID }}
client_id = ${{ secrets.AZURE_CLIENT_ID }}
client_secret = ${{ secrets.AZURE_CLIENT_SECRET }}

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