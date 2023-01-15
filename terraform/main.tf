provider "azurerm" {
  subscription_id = var.subscription_id
  tenant_id = var.tenant_id
  client_id = var.client_id
  client_secret = var.client_secret
  version = "=2.32.0"
  features {}
}

provider "azuread" {
  version = "=0.8.0"
}

resource "azurerm_resource_group" "perbak_rg" {
  name     = "perbak-rg"
  location = "westus2"
}

resource "azurerm_key_vault" "key_vault" {
  name                = "key-vault"
  location            = azurerm_resource_group.perbak_rg.location
  resource_group_name = azurerm_resource_group.perbak_rg.name
  sku_name            = "standard"
  tenant_id           = var.tenant_id
}

data "azurerm_key_vault_secret" "client_secret" {
  name         = "client-secret"
  key_vault_id = azurerm_key_vault.key_vault.id
}

data "azurerm_key_vault_secret" "postgres_user" {
  name         = "postgres-user"
  key_vault_id = azurerm_key_vault.key_vault.id
}

data "azurerm_key_vault_secret" "postgres_password" {
  name         = "postgres-password"
  key_vault_id = azurerm_key_vault.key_vault.id
}

resource "azurerm_kubernetes_cluster" "perbak_cluster" {
  name                = "perbak_cluster"
  location            = azurerm_resource_group.perbak_rg.location
  resource_group_name = azurerm_resource_group.perbak_rg.name
  dns_prefix          = "perbak-cluster"

  default_node_pool {
    name       = "default"
    node_count = 3
    vm_size    = ",standard_d12_v2"
  }

  service_principal {
    client_id     = var.client_id
    client_secret = var.client_secret
  }

  network_profile {
    network_plugin    = "kubenet"
    network_policy    = "calico"
    load_balancer_sku = "basic"
  }
}

resource "azurerm_postgresql_server" "perbak_postgres_server" {
  name                = "perbak-postgres-server"
  location            = azurerm_resource_group.perbak_rg.location
  resource_group_name = azurerm_resource_group.perbak_rg.name
  version             = "10.0"
  storage_mb = 51200
  backup_retention_days = 7


  administrator_login          = data.azurerm_key_vault_secret.postgres_user.value
  administrator_login_password = data.azurerm_key_vault_secret.postgres_password.value

  sku_name = "B_Gen5_1"
  ssl_enforcement_enabled = "true"
}

resource "azurerm_postgresql_database" "perbak_postgres_db" {
  name                = "perbak-db"
  resource_group_name = azurerm_resource_group.perbak_rg.name
  server_name         = azurerm_postgresql_server.perbak_postgres_server.name
  charset             = "UTF8"
  collation           = "English_United States.1252"
}