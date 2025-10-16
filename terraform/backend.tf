terraform {
  backend "azurerm" {
    resource_group_name   = "devopsaks-rg"
    storage_account_name  = "tfstate28643"          
    container_name        = "terraformstate"
    key                   = "devops-aks.terraform.tfstate"
  }
}
