# 🛡️ Self-Healing Infrastructure with Prometheus, Alertmanager, Flask Webhook, Ansible & Docker

## 🚀 Project Overview
This repository demonstrates a complete **self-healing infrastructure**
- **Containerize** all components with Docker & Docker Compose
- **Detect** service failures (NGINX down or sustained high CPU)  
- **Alert** via Prometheus & Alertmanager  
- **Automate** recovery with a Flask-based webhook and Ansible playbooks    

---

## 📁 Repository Structure

```text
self-healing-infra/
├── docker-compose.yml
├── webhook/
│   └── Dockerfile
├── prometheus/
│   ├── prometheus.yml
│   ├── alerts.yml
│   └── blackbox.yml
├── alertmanager/
│   └── alertmanager.yml
├── ansible/
│   ├── ansible.cfg
│   ├── inventory/
│   │   └── hosts.ini
│   └── playbooks/
│       ├── restart_nginx.yml
│       └── cpu_investigate.yml
└── scripts/
    └── alertmanager_webhook.py
```

---

## 🔌 Ports to Open

When running on a public VM (e.g. EC2), make sure your security group or firewall allows inbound traffic on:

| Port  | Protocol | Service               | Purpose                                  | Source                   |
|-------|----------|-----------------------|------------------------------------------|--------------------------|
| 22    | TCP      | SSH                   | Remote server management                 | Your IP only             |
| 8080  | TCP      | NGINX                 | Demo web-service endpoint (HTTP)         | `0.0.0.0/0` (public)     |
| 9090  | TCP      | Prometheus UI         | Monitoring dashboard                     | Your IP or `0.0.0.0/0`   |
| 9093  | TCP      | Alertmanager UI       | Alerting dashboard                       | Your IP or `0.0.0.0/0`   |
| 9100  | TCP      | Node Exporter         | Host-metrics endpoint                    | Your IP only (optional)  |
| 9115  | TCP      | Blackbox Exporter     | HTTP probe endpoint for NGINX health     | Your IP only (optional)  |


---


## 🚀 Quick Start Guide

### Clone & cd
```bash
git clone https://github.com/rxm-gupta/self-healing-infra.git
cd self-healing-infra
```

### Install Docker Compose Plugin (if not already installed)
```bash
sudo apt-get update
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

### Install the Docker packages.
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Add current user to Docker group (to avoid using sudo always)
```bash
sudo usermod -aG docker $USER
```
✅ Important: After this, log out and log back in, or run:
```bash
newgrp docker
```

### Start the Docker daemon
```bash
sudo systemctl start docker
```
```bash
docker compose version
```

### Build & launch
```bash
docker compose build
docker compose up -d
```

### Verify services
```bash
NGINX: http://localhost:8080

Prometheus UI: http://localhost:9090

Alertmanager UI: http://localhost:9093
```


### Simulate High CPU
```bash
docker exec -d nginx sh -c "yes > /dev/null &"
```

### Watch real-time logs:
```bash
docker logs -f webhook
```
```bash
docker logs prometheus
```
Wait ~1 min, watch logs; On High CPU alert, NGINX container will be automatically restarted unconditionally.


### Tear down
```bash
docker compose down
```
---

![Image](https://github.com/user-attachments/assets/f08c376f-fad9-4058-8752-a44fa30322d2)

![Image](https://github.com/user-attachments/assets/d244d939-dd25-4fce-9b36-5c6a827f0621)

![Image](https://github.com/user-attachments/assets/91699e5c-3a46-4d0e-ad97-dc2e08588a5b)

![Image](https://github.com/user-attachments/assets/d26d45a0-db86-41a4-a815-c941ed523428)

![Image](https://github.com/user-attachments/assets/40f94911-cda3-4f63-809c-c60a348959d2)

![Image](https://github.com/user-attachments/assets/4a403fa7-129f-47a1-9af5-53ad5f5c0fe7)

---

## Author
- **GitHub** https://github.com/rxm-gupta/
- **LinkedIn** https://www.linkedin.com/in/ram-gupta-103169258/
- **Gmail** rxmgupta@gmail.com

