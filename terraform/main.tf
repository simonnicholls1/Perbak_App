provider "azurerm" {
  subscription_id = var.subscription_id
  tenant_id = var.tenant_id
  client_id = var.client_id
  client_secret = var.client_secret
  features {}
}

provider "azuread" {

}

data "azurerm_resource_group" "perbak_rg" {
  name     = var.resource_group
}

data "azurerm_key_vault" "key_vault" {
  name                = var.key_vault_name
  resource_group_name = data.azurerm_resource_group.perbak_rg.name
}

data "azurerm_key_vault_secret" "client_secret" {
  name         = "client-secret"
  key_vault_id = data.azurerm_key_vault.key_vault.id
}

data "azurerm_key_vault_secret" "postgres_user" {
  name         = "postgres-user"
  key_vault_id = data.azurerm_key_vault.key_vault.id
}

data "azurerm_key_vault_secret" "postgres_password" {
  name         = "postgres-password"
  key_vault_id = data.azurerm_key_vault.key_vault.id
}

resource "azurerm_container_registry" "perbak_registry" {
  name                = var.registry_name
  resource_group_name = data.azurerm_resource_group.perbak_rg.name
  location            = data.azurerm_resource_group.perbak_rg.location
  sku                 = "Standard"
}

resource "azurerm_kubernetes_cluster" "perbak_cluster" {
  name                = var.cluster_name
  location            = data.azurerm_resource_group.perbak_rg.location
  resource_group_name = data.azurerm_resource_group.perbak_rg.name
  dns_prefix          = "perbak-cluster"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "standard_B4ms"
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

  tags = {
    Environment = var.environment
  }
}

provider "kubernetes" {
  host                   = azurerm_kubernetes_cluster.perbak_cluster.kube_config.0.host
  username               = azurerm_kubernetes_cluster.perbak_cluster.kube_config.0.username
  password               = azurerm_kubernetes_cluster.perbak_cluster.kube_config.0.password
  client_certificate     = base64decode(azurerm_kubernetes_cluster.perbak_cluster.kube_config.0.client_certificate)
  client_key             = base64decode(azurerm_kubernetes_cluster.perbak_cluster.kube_config.0.client_key)
  cluster_ca_certificate = base64decode(azurerm_kubernetes_cluster.perbak_cluster.kube_config.0.cluster_ca_certificate)
}


resource "kubernetes_namespace" "perbak-api" {
  metadata {
    name = "perbak-api"
  }
}

resource "azurerm_postgresql_server" "perbak_postgres_server" {
  name                = "perbak-postgres-server"
  location            = data.azurerm_resource_group.perbak_rg.location
  resource_group_name = data.azurerm_resource_group.perbak_rg.name
  version             = "10.0"
  storage_mb = 51200
  backup_retention_days = 7


  administrator_login          = data.azurerm_key_vault_secret.postgres_user.value
  administrator_login_password = data.azurerm_key_vault_secret.postgres_password.value

  sku_name = "B_Gen5_1"
  ssl_enforcement_enabled = "false"
  ssl_minimal_tls_version_enforced ="TLSEnforcementDisabled"
}

resource "azurerm_postgresql_database" "perbak_postgres_db" {
  name                = var.db_name
  resource_group_name = data.azurerm_resource_group.perbak_rg.name
  server_name         = azurerm_postgresql_server.perbak_postgres_server.name
  charset             = "UTF8"
  collation           = "English_United States.1252"
}