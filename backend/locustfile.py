from locust import HttpUser, task


class LocustTest(HttpUser):
    @task
    def courses(self):
        self.client.get("/courses")
