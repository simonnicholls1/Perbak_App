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
  default = "westus2"
}
