from locust import HttpUser, task, between


class ReadHeavyUser(HttpUser):
    wait_time = between(0.1, 1.0)

    @task(4)
    def list_messages(self):
        self.client.get("/api/v1/messages?limit=20")

    @task(1)
    def write_message(self):
        self.client.post("/api/v1/messages", json={"message": "hello", "author": "load"})


class WriteHeavyUser(HttpUser):
    wait_time = between(0.05, 0.2)

    @task(5)
    def write_message(self):
        self.client.post(
            "/api/v1/messages",
            json={"message": "stress", "author": "load", "metadata": {"type": "write"}},
        )

    @task(1)
    def list_messages(self):
        self.client.get("/api/v1/messages?limit=5")


class MixedUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task(3)
    def list_messages(self):
        self.client.get("/api/v1/messages?limit=10")

    @task(2)
    def write_message(self):
        self.client.post(
            "/api/v1/messages",
            json={"message": "mixed", "author": "load"},
        )
