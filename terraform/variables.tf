variable "subscription_id" {
  description = "The Azure Subscription ID"
}

variable "tenant_id" {
  description = "The Azure Tenant ID"
}

variable "client_id" {
  description = "The Azure Client ID"

}

variable "client_secret" {
  description = "The Azure Client Secret"
}

variable "location" {
  description = "The location for the resources"
  default = "eastus"
}

variable "environment" {
  description="Target environment"
}

variable "registry_name" {
  description = "Registry for images"
}

variable "resource_group" {
  description="Resource Group"
}

variable "db_name" {
  description = "DB Name"
}

variable "cluster_name" {
  description = "K8 cluster name"
}

variable "key_vault_name" {
  description = "Name for key vault"
}
