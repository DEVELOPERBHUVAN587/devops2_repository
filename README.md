# Email Game DevOps Project 🎮🚀

This project demonstrates a complete DevOps lifecycle for a Pygame-based email quiz game, including CI/CD, infrastructure provisioning, configuration management, and monitoring using modern DevOps tools.

---

## 📁 Project Structure

```
devops2_repository/
├── deployment/
│   ├── ansible/
│   ├── puppet/
│   └── terraform/
├── docker/
├── monitoring/
│   ├── docker-compose.yml
│   └── prometheus/
│       └── prometheus.yml
├── src/
│   ├── main.py
│   └── requirements.txt
├── tests/
│   └── test_game.py
├── .github/workflows/
│   └── ci-cd.yml
└── README.md
```

---

## ⚙️ Setup Steps

1. **Clone the Repository**

```bash
git clone https://github.com/DEVELOPERBHUVAN587/devops2_repository.git
cd devops2_repository
```

2. **Install Requirements (on local host)**

```bash
pip install -r src/requirements.txt
```

3. **Run the Game (standalone)**

```bash
python3 src/main.py
```

---

## ✅ CI/CD Pipeline (GitHub Actions + Jenkins)

### 🔧 GitHub Actions (`.github/workflows/ci-cd.yml`)

- Python tests using `pytest`
- Build Docker image of the game

### 🧪 Jenkins (GUI + Sound via Docker)

Jenkinsfile runs the game in a playable form with GUI and sound.

---

## 🌐 Infrastructure Provisioning (Terraform)

Terraform + Libvirt is used to provision a local KVM VM:

- Creates VM with VNC display + audio support
- Uses `ubuntu-22.04.qcow2` disk image

```bash
cd deployment/terraform
terraform init
terraform apply
```

VM auto-starts the game on boot via cloud-init.

---

## 🤖 Configuration Management (Puppet Standalone)

```bash
cd deployment/puppet
sudo /opt/puppetlabs/bin/puppet apply   --modulepath=./   email_game/manifests/init.pp
```

This:

- Creates `/home/vishn_ubuntu/email_game/`
- Copies assets + code
- Installs dependencies

Then run manually:

```bash
python3 /home/vishn_ubuntu/email_game/main.py
```

---

## 📊 Monitoring (Grafana + Prometheus)

### 🔧 Setup

```bash
cd monitoring
docker compose up -d
```

### 🧠 Instrumentation

Prometheus client exposes game metrics on `:8000/metrics`:
- Games played
- Correct/Incorrect answers

Access Grafana at: [http://localhost:3000](http://localhost:3000)

- Default login: `admin/admin`
- Import JSON dashboard for metrics visualization

---

## 🖼️ Grafana Dashboard

Includes:
- Games played
- Correct answers
- Incorrect answers

All are collected in real-time from your game metrics endpoint.

---

## 🙌 You're Done!

A complete DevOps pipeline from code to monitoring. Enjoy hacking! 🎮🚀

---

Created with 💻 by **Vishnu Bhuvan**