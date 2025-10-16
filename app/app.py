from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello HRGF,\nI am Kunal Phale.\nThis application was deployed on Azure Kubernetes Service (AKS) using Terraform, Helm, and GitHub Actions."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
