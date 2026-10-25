# System Architecture specifics

## Components
- **Frontend**: static dashboard polling API, hosted via CDN or Kubernetes ingress.
- **API Service**: Flask app exposing CRUD endpoints, exposing Prometheus metrics.
- **Database**: MongoDB replica set with 3 members in StatefulSet, persistent volumes, keyfile auth.
- **Load Balancer**: Nginx Ingress Controller providing TLS termination and retry logic.
- **Auto-Scaling**: HPA driven by CPU and custom requests/sec metric from Prometheus Adapter.
- **Monitoring**: Prometheus + Grafana deployments, Alertmanager optional.
- **Load Testing**: Locust jobs triggered manually or via CronJob using Helm chart.

## Data Flow
Clients → Nginx Ingress → Service → API pods → MongoDB primary (writes) / secondary (reads). Metrics published to Prometheus; Grafana dashboards visualize performance; HPA queries metrics API for scaling decisions.

## Reliability
- Pod disruption budgets and anti-affinity (to add) keep API replicas distributed.
- MongoDB replica set ensures automatic elections.
- CI/CD pushes versioned images, Helm releases with canary strategy (set `replicaCount` / `maxSurge`).

## Security Considerations
- Secrets managed through Kubernetes Secrets / ExternalSecret.
- NetworkPolicies restrict DB access to API namespace.
- TLS termination at ingress; mTLS optional for service mesh.
