import time
from locust import HttpUser, TaskSet, between, task
from OdooLocust.OdooLocustUser import OdooLocustUser
from OdooLocust import OdooTaskSet
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


class WebsiteUserTasks(TaskSet):
    tasks = [index, login_page, re_registration_page, sdf_registration_page, org_registration_page,
            provider_accreditation_page, assessor_registration_page, moderator_register_page]

    @task
    def page404(self):
        self.client.get("/does_not_exist")


# class WebsiteUser(HttpUser):
#     """
#     User class that does requests to the locust web server running on localhost
#     """

#     host = "http://127.0.0.1:8089"
#     wait_time = between(2, 5)
#     tasks = [UserTasks]
    
    
# backend Tasks
def login(l):
        l.client.post(
            "/web/login", json={"username": "ohiageorge@gmail.com", "password": "ohiageorge#001"})
    
def view_contacts(l):
    l.client.get(
        "/web#action=129&model=res.partner&view_type=kanban&cids=1&menu_id=93", name="/contacts")
    
def view_settings(l):
    l.client.get(
        "/web#id=&action=86&model=res.config.settings&view_type=form&cids=&menu_id=4", name="/settings")

def view_users(l):
    l.client.get(
        "/web#action=70&model=res.users&view_type=list&cids=&menu_id=4", name="/ist_users")
    

def read_user(l):
    for item_id in range(57864, 72806):
        l.client.get(
            f"/web#id={item_id}&action=70&model=res.users&view_type=form&cids=&menu_id=4", name="/users")
        time.sleep(1)
        
        
# def write_user(l):
#     self.client.get(
#         f"/web#id={item_id}&action=70&model=res.users&view_type=form&cids=&menu_id=4", name="/users")


def view_sdfs(l):
    l.client.get(
        "/web#action=266&model=inseta.sdf&view_type=list&cids=&menu_id=179", name="/sdfs")

    
class BackendUserTasks(TaskSet):
    tasks = [login, view_contacts, view_settings, view_users, read_user, view_sdfs]


class BackendUser(HttpUser):

    host = "http://127.0.0.1:8089"
    wait_time = between(2, 5)
    tasks = [BackendUserTasks, WebsiteUserTasks]

    def on_start(self):
        self.client.post(
            "/web/login", json={"username": "ohiageorge@gmail.com", "password": "ohiageorge#001"})


# class AdminOdooUser(OdooLocustUser):
#     # host = "www.aims-online.co.za"
#     # database = "live"
#     # login = "ohiageorge@gmail.com"
#     # password = "@UrK5sSXU@3Tup"
#     # port = 443
#     # wait_time = between(0.1, 10)  # Simulates waiting time between tasks
#     host = "localhost"
#     database = "etdp_live2"
#     login = "admin"
#     password = "@UrK5sSXU@3Tup"
#     port = 8016
#     wait_time = between(0.1, 10)  # Simulates waiting time between tasks
    
    
#     @task(50)
#     def fetch_odoo_users(self):
#         cust_model = self.client.get_model('res.users')
#         cust_ids = cust_model.search([], limit=80)
#         prtns = cust_model.read(cust_ids, ['login'])
    

#     @task(48)
#     def write_odoo_users(self):
#         cust_model = self.client.get_model('res.users')
#         user = cust_model.search([('id','=', 2)])
#         prtns = cust_model.read(user, ['login'])
#         # user.write({'id_no': 'perf test'})
    
#     @task(45)
#     def fetch_odoo_partners(self):
#         cust_model = self.client.get_model('res.partner')
#         cust_ids = cust_model.search([], limit=80)
#         prtns = cust_model.read(cust_ids, ['name'])
        
        
#     @task(40)
#     def fetch_sdfs(self):
#         cust_model = self.client.get_model('inseta.sdf')
#         cust_ids = cust_model.search([], limit=80)
#         prtns = cust_model.read(cust_ids, ['name'])


#     @task(35)
#     def fetch_organizations(self):
#         cust_model = self.client.get_model('inseta.organisation')
#         cust_ids = cust_model.search([], limit=80)
#         prtns = cust_model.read(cust_ids, ['name'])
        
        
#     @task(30)
#     def fetch_wspatrs(self):
#         cust_model = self.client.get_model('inseta.wspatr')
#         cust_ids = cust_model.search([], limit=80)
#         prtns = cust_model.read(cust_ids, ['name'])
        
        
#     @task(25)
#     def fetch_wspatrs_eval(self):
#         cust_model = self.client.get_model('mis.wspatr.evaluation')
#         cust_ids = cust_model.search([], limit=80)
#         prtns = cust_model.read(cust_ids, ['legal_name','financial_year_id'])
        
        
#     @task(100)
#     def fetch_providers(self):
#         cust_model = self.client.get_model('inseta.provider')
#         cust_ids = cust_model.search([], limit=80)
#         prtns = cust_model.read(cust_ids, ['name'])
        
#     @task(90)
#     def fetch_assessors(self):
#         cust_model = self.client.get_model('inseta.assessor')
#         cust_ids = cust_model.search([], limit=80)
#         prtns = cust_model.read(cust_ids, ['first_name'])
        
#     @task(80)
#     def fetch_moderators(self):
#         cust_model = self.client.get_model('inseta.moderator')
#         cust_ids = cust_model.search([], limit=80)
#         prtns = cust_model.read(cust_ids, ['first_name'])
        
#     @task(200)
#     def fetch_learners(self):
#         cust_model = self.client.get_model('inseta.learner')
#         cust_ids = cust_model.search([], limit=80)
#         prtns = cust_model.read(cust_ids, ['first_name','middle_name','last_name'])
    
#     @task(10)
#     def fetch_interventions(self):
#         cust_model = self.client.get_model('learner.batch.upload.wizard')
#         cust_ids = cust_model.search([], limit=80)
#         prtns = cust_model.read(cust_ids, ['download_number','funding_type'])
        
#     @task(210)
#     def fetch_allocate_assessment(self):
#         cust_model = self.client.get_model('allocate.assessment')
#         cust_ids = cust_model.search([], limit=80)
#         prtns = cust_model.read(cust_ids, ['name','provider_id','learner_total_count','learner_approved_count'])
    
    
#     @task(210)
#     def write_allocate_assessment(self):
#         cust_model = self.client.get_model('allocate.assessment')
#         rec = cust_model.search([('id','=', 30)])
#         original_learner_count = cust_model.read(rec, ['learner_total_count'])
        # rec.write({'learner_total_count': 100})
        # sleep(1)
        # rec.write({'learner_total_count': original_learner_count})
    
    
# class AdminOdooUserGeneric(OdooLocustUser):
#     host = "www.aims-online.co.za"
#     database = "live"
#     login = "ohiageorge@gmail.com"
#     password = "@UrK5sSXU@3Tup"
#     port = 443
#     wait_time = between(0.1, 10)  # Simulates waiting time between tasks
    
#     @task(10)
#     def fetch_odoo_partners(self):
#         cust_model = self.client.get_model('res.partner')
#         cust_ids = cust_model.search([], limit=80)
#         prtns = cust_model.read(cust_ids, ['name'])

        
#     tasks = [OdooTaskSet.OdooGenericTaskSet]

        
# class BackendTest(HttpUser):
#     wait_time = between(1, 5)

#     @task(3)
#     def hello_world(self):
#         self.client.get("/web")
#         self.client.get(
#             "/web#cids=1&menu_id=409&action=575&model=epgi.policy&view_type=list")
#         self.client.get(
#             "/web#cids=1&menu_id=454&action=621&model=epgi.policy&view_type=list")
#         self.client.get(
#             "/web#cids=1&menu_id=124&action=170&model=res.partner&view_type=kanban")

#     @task
#     def view_items(self):
#         for item_id in range(662, 789):
#             self.client.get(
#                 f"/web#id={item_id}&cids=1&menu_id=409&action=575&model=epgi.policy&view_type=form", name="/polices")
#             time.sleep(1)

#     def on_start(self):
#         self.client.post(
#             "/web/login", json={"username": "admin", "password": "admin"})
