# Experiment Playbook

## 1. Scalability
1. Deploy API + Mongo + monitoring via Helm.
2. Launch Locust job with stepped load (100 → 500 → 1,000 RPS every 5 minutes).
3. Capture metrics:
   - API latency percentiles (`flask_http_request_duration_seconds`)
   - Pod counts (HPA events)
   - Mongo CPU + replication lag (`mongodb_mongod_replset_oplog_total_lag`) if exporter installed
4. Document saturation point and scaling timelines.

## 2. Failure Recovery
- **API Pod Kill**: `kubectl delete pod -l app=cloud-native-api` during steady 500 RPS load. Measure request errors, recovery time.
- **Node Drain**: `kubectl drain <node>`; monitor rescheduling latency.
- **Mongo Primary Failure**: delete primary pod and measure election duration via `rs.status()`.

## 3. Replication Performance
1. Enable write-heavy Locust scenario (`/api/v1/messages` POST 90% of traffic).
2. Compare write concern `w=1` vs `w=majority` via environment variable `MONGO_WRITE_CONCERN` (see API).
3. Observe oplog lag and API latency deltas.

## 4. Auto-Scaling Behavior
- Configure HPA for CPU + custom RPS metric.
- Run CPU-bound endpoint load (`/api/v1/messages?heavy=true` if implemented) to trigger CPU scaling.
- For RPS-based scaling, ensure Prometheus Adapter exposes `requests_per_second` metric.
- Plot metric vs pod count to validate hysteresis & cooldown.

## 5. Latency under Different Loads
- Three Locust user classes: read-heavy, write-heavy, mixed.
- Run at 100, 500, 1,000 RPS; capture 50/95/99th percentile latencies and DB duration.
- Highlight thresholds where tail latency spikes.

## Reporting Guidelines
- Use Grafana dashboard snapshots per experiment.
- Store raw results in `docs/results/<timestamp>.md`.
- Summaries should include methodology, observations, bottlenecks, next actions.
