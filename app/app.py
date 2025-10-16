from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """👋 Hello HRGF!
🤖 I am <b>Kunal Phale</b>.
🚀 This application was deployed on <b>Azure Kubernetes Service (AKS)</b>.
🧱 Tools used: Terraform, Helm, and GitHub Actions.
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
