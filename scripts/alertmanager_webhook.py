#!/usr/bin/env python3
import os
import logging
import subprocess
from flask import Flask, request

# ——— Configuration —————————————————————————————————————————
# Playbook and inventory locations baked into the image
PLAYBOOK_DIR = '/ansible/playbooks'
INVENTORY   = '/ansible/inventory/hosts.ini'

# Map Prometheus alert names to your Ansible playbooks
PLAYBOOK_MAP = {
    'NginxDown': os.path.join(PLAYBOOK_DIR, 'restart_nginx.yml'),
    'HighCPU':   os.path.join(PLAYBOOK_DIR, 'cpu_investigate.yml'),
}

# Flask & logging setup
app = Flask(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

# ——— Webhook endpoint —————————————————————————————————————————
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json(force=True)
    alerts = data.get('alerts', [])
    for alert in alerts:
        name   = alert['labels'].get('alertname')
        status = alert.get('status')
        logging.info(f"Received alert: {name} (status: {status})")

        playbook = PLAYBOOK_MAP.get(name)
        if not playbook:
            logging.warning(f"No playbook mapped for alert: {name}")
            continue

        # Construct and run the Ansible command
        cmd = ['ansible-playbook', playbook, '-i', INVENTORY]
        logging.info(f"Executing: {' '.join(cmd)}")
        proc = subprocess.run(cmd, capture_output=True, text=True)

        # Log both stdout and stderr for full visibility
        logging.info(f"Playbook stdout:\n{proc.stdout.strip()}")
        if proc.stderr:
            logging.error(f"Playbook stderr:\n{proc.stderr.strip()}")

    # Always return 200 so Alertmanager won’t retry
    return '', 200

# ——— Entrypoint ——————————————————————————————————————————————
if __name__ == '__main__':
    port = int(os.environ.get('WEBHOOK_PORT', '5001'))
    app.run(host='0.0.0.0', port=port)

