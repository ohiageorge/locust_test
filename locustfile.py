import time
from locust import HttpUser, TaskSet, between, task
# https://github.com/nseinlet/OdooLocust


def index(l):
    l.client.get("/")


def login_page(l):
    l.client.get("/web/login")


def re_registration_page(l):
    l.client.get("/re-registration")


def sdf_registration_page(l):
    l.client.get("/sdf-registration")


def org_registration_page(l):
    l.client.get("/nonlevy-registration")


def provider_accreditation_page(l):
    l.client.get("/provider-accreditation")


def assessor_registration_page(l):
    l.client.get("/assessor-registration")


def moderator_register_page(l):
    l.client.get("/moderator-register")


class UserTasks(TaskSet):
    tasks = [index, login_page, re_registration_page, sdf_registration_page, org_registration_page,
            provider_accreditation_page, assessor_registration_page, moderator_register_page]

    @task
    def page404(self):
        self.client.get("/does_not_exist")


class WebsiteUser(HttpUser):
    """
    User class that does requests to the locust web server running on localhost
    """

    host = "http://127.0.0.1:8089"
    wait_time = between(2, 5)
    tasks = [UserTasks]
    
    
# backend Tasks
# def login(l):
#         l.client.post(
#             "/web/login", json={"username": "admin", "password": "admin"})
    
# def view_contacts(l):
#     l.client.get(
#         "/web#action=129&model=res.partner&view_type=kanban&cids=1&menu_id=93")
    
# def view_settings(l):
#     l.client.get(
#         "/web#id=&action=86&model=res.config.settings&view_type=form&cids=&menu_id=4")

# def view_users(l):
#     l.client.get(
#         "/web#action=70&model=res.users&view_type=list&cids=&menu_id=4")
    

# def read_user(l):
#     for item_id in range(26358, 64334):
#         l.client.get(
#             f"/web#id={item_id}&action=70&model=res.users&view_type=form&cids=&menu_id=4", name="/users")
#         time.sleep(1)
        
        
# # def write_user(l):
# #     self.client.get(
# #         f"/web#id={item_id}&action=70&model=res.users&view_type=form&cids=&menu_id=4", name="/users")


# def view_sdfs(l):
#     l.client.get(
#         "/web#action=266&model=inseta.sdf&view_type=list&cids=&menu_id=179")

    
# class BackendUserTasks(TaskSet):
#     tasks = [login, view_contacts, view_settings, view_users, read_user, view_sdfs]


# class BackendUser(HttpUser):

#     host = "http://127.0.0.1:8089"
#     wait_time = between(2, 5)
#     tasks = [BackendUserTasks]

#     def on_start(self):
#         self.client.post(
#             "/web/login", json={"username": "admin", "password": "admin"})

