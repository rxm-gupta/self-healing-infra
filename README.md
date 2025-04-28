# 🛡️ Self-Healing Infrastructure with Prometheus, Alertmanager, Flask Webhook, Ansible & Docker

## 🚀 Project Overview
This repository demonstrates a complete **self-healing infrastructure** pattern:
- **Detect** service failures (NGINX down or sustained high CPU)  
- **Alert** via Prometheus & Alertmanager  
- **Automate** recovery with a Flask-based webhook and Ansible playbooks  
- **Containerize** all components with Docker & Docker Compose  

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

### Build & launch
```bash
docker compose up --build -d
```

### Verify services
```bash
NGINX: http://localhost:8080

Prometheus UI: http://localhost:9090

Alertmanager UI: http://localhost:9093
```

### Simulate NGINX failure
```bash
docker stop nginx
```

### Watch real-time logs:
```bash
docker logs -f webhook
```
➜ NGINX will auto-restart in ~30 s.

### Simulate High CPU
```bash
docker exec -d nginx sh -c "yes > /dev/null &"
```
Wait ~1 min, watch logs; NGINX auto-restarts if it’s the CPU hog.

### Clean up CPU load:
```bash
docker restart nginx
```

### Tear down
```bash
docker compose down
```

---

## Author: rxm-gupta
