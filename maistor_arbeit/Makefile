.PHONY: install test lint docker-build kind-up deploy-api deploy-db deploy-monitoring load-test build-push deploy-all terraform-apply experiments ci

install:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

test:
	pytest -q

docker-build:
	docker build -t cloud-native-api -f Dockerfile.api .

deploy-api:
	helm upgrade --install api infra/helm/api -n default

deploy-db:
	helm upgrade --install mongodb infra/helm/mongodb -n default

deploy-monitoring:
	helm upgrade --install monitoring infra/helm/monitoring -n observability --create-namespace

load-test:
	locust -f tests/load/locustfile.py --headless -u 500 -r 50 -t 10m -H $$HOST

build-push:
	./scripts/build_and_push.sh

deploy-all:
	./scripts/deploy_k8s.sh

terraform-apply:
	./scripts/terraform_apply.sh

experiments:
	./scripts/run_experiments.sh

ci:
	./scripts/run_ci_pipeline.sh
