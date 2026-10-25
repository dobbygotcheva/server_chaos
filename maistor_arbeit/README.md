# Cloud-Native Distributed Web System

This project demonstrates a cloud-native web application featuring a Python Flask API, MongoDB replica set backend, Kubernetes deployment with auto-scaling via Horizontal Pod Autoscaler (HPA), and an observability stack built on Prometheus and Grafana. Load testing scenarios (Locust) drive experiments on scalability, failure recovery, replication performance, auto-scaling behavior, and latency under varying workloads.

## Repository Layout

- `app/api` – Flask application source
- `infra/helm` – Helm charts for API, MongoDB, monitoring stack, and load testing tools
- `infra/terraform` – Terraform modules for Kubernetes cluster, networking, and database VMs
- `k8s` – Environment-specific overlays and raw manifests references
- `monitoring` – Prometheus rules and Grafana dashboards
- `tests/load` – Locust scenarios and experiment harness
- `docs` – Experiment procedures, runbooks, and architecture notes

## Getting Started

1. **Install dependencies**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run the API locally**
   ```bash
   export FLASK_ENV=development
   export MONGODB_URI="mongodb://localhost:27017,localhost:27018,localhost:27019/?replicaSet=rs0"
   flask --app app.api.main run --debug
   ```

3. **Docker**
   ```bash
   docker build -t cloud-native-api -f Dockerfile.api .
   docker run -p 8080:8080 -e MONGODB_URI=... cloud-native-api
   ```

4. **Kubernetes**
   ```bash
   helm upgrade --install api-server infra/helm/api
   helm upgrade --install mongodb infra/helm/mongodb
   helm upgrade --install monitoring infra/helm/monitoring
   ```

5. **Load Testing**
   ```bash
   locust -f tests/load/locustfile.py --headless -u 500 -r 50 -H http://localhost:8080
   ```


