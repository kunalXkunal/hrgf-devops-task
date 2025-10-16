
# DevOps Project: Flask App Deployment on Azure AKS with CI/CD, Helm & Terraform

This project demonstrates a complete DevOps pipeline that builds, scans, and deploys a containerized Flask web application on Azure Kubernetes Service (AKS) using Terraform, Helm, GitHub Actions, and Trivy.


## Overview

Tools & Technologies Used:
- Docker – Containerization
- Azure Kubernetes Service (AKS) – Orchestration
- Terraform – Infrastructure as Code
- Azure Storage account - tfstate file
- Helm – Kubernetes Deployment
- GitHub Actions – CI/CD Automation
- Trivy – Image Vulnerability Scanning

## CI/CD Pipeline Flow

Each push to the main branch triggers the GitHub Actions workflow which performs:

Step	Action	Tool
1.	Checkout source code	GitHub Actions
2.	Log in to Azure	Azure Login Action
3.	Build Docker image	Docker
4.	Scan image for vulnerabilities	Trivy
5.	Push image to ACR	Azure 
6.	Get AKS credentials	Azure
7.	Deploy/Upgrade via Helm	Helm


## Security Integration

Trivy Image Scan — Detects vulnerabilities in Docker images during CI/CD.

Build Fails on Critical Vulnerabilities (configurable).

Helm ensures versioned, secure, and repeatable deployments.

No hard-coded secrets — uses GitHub Secrets & Kubernetes Secrets.






## How to Run this Project (Step-by-Step)

Step 1 — Prerequisites
- Azure Subscription
- Azure CLI, Terraform, kubectl, Helm, Git installed

Step 2 — Clone the Repository

```bash
  git clone https://github.com/kunalXkunal/hrgf-devops-task.git
```

Go to the project directory

```bash
  cd hrgf-devops-task
```

Step 3 — Deploy Infrastructure with Terraform

```bash
  cd terraform
  terraform init
  terraform plan
  terraform apply
```
Step 4 — Build & Push Docker Image to ACR

```bash
  az login
  az acr login --name <your-acr-name>
  docker build -t <your-acr-name>.azurecr.io/myapp:latest .
  docker push <your-acr-name>.azurecr.io/myapp:latest

```
Step 5 — Connect to AKS Cluster

```bash
  az aks get-credentials -g <resource-group> -n <aks-name> --admin
  kubectl get nodes
```
Step 6 — Deploy Application using Helm

```bash
  helm upgrade --install myapp-release ./myapp-chart   --set image.repository=<your-acr-name>.azurecr.io/myapp   --set image.tag=latest   --set replicaCount=2
```
Step 7 — Access the Application

```bash
  kubectl get svc
  http://<EXTERNAL-IP>
```
Step 8 — Run the CI/CD Pipeline (GitHub Actions)

```bash
  Go to your forked repo → Settings → Secrets and variables → Actions

  Add these secrets:

  AZURE_CREDENTIALS – output from az ad sp create-for-rbac

  ACR_USERNAME

  AKS_CLUSTER_NAME

  AKS_RESOURCE_GROUP

  ACR_LOGIN_SERVER

  ACR_PASSWORD

Push a code change → The GitHub Actions workflow (.github/workflows/deploy.yml) will:

  Build the Docker image

  Scan it using Trivy

  Push it to ACR

  Deploy to AKS using Helm
```



## Live Application

Deployed App URL:
http://172.193.201.220/

## Summary of Implementation
Stage                | Tool              | Description
---------------------|------------------|-----------------------------------------------
Infrastructure       | Terraform         | Creates Resource Group, AKS, and ACR
CI/CD                | GitHub Actions    | Automates build, scan, push, and deploy
Containerization     | Docker            | Packages Flask app into container image
Deployment           | Helm              | Deploys containerized app to AKS
Security             | Trivy             | Scans images for vulnerabilities
Cloud Platform       | Azure             | Hosts ACR and AKS services
State Management     | Azure Storage Account| Stores Terraform state

## Final Result
✅ Fully automated build → scan → push → deploy pipeline


✅ Flask app deployed on Azure AKS

✅ Secure, scalable, and production-ready setup


