from drf_test_master.testcases import create
from django.urls import reverse
from example.models import ExampleModel
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class TestExampleNoAuthEndpoint (
    create.TestSendValidBody,
    create.TestSendEmptyBody
):  
    
    def get_body(self):
        return {
            'name': 'test'
        }
    
    def model_creation(self):
        return ExampleModel.objects.create(name='test')
    
    def get_url(self):
        return reverse('create-no-auth')

    def test_send_valid_body(self):
        req = super().test_send_valid_body()
        print(req.json())
        
class TestExampleIsAuthEndpoint (
    create.TestSendEmptyBody,
    create.TestSendValidBody,
    create.TestUnAuthorized,
):  
    def get_body(self):
        return {
            'name': 'test'
        }
    
    def model_creation(self):
        return ExampleModel.objects.create(name='test')
    
    def get_url(self):
        return reverse('create-is-auth')
    
    def get_headers(self):
        user = User.objects.create(
            username = 'test',
            email = 'test@gmail.com'
        )
        token = Token.objects.create(user=user)
        return {
            'Authorization' : f"Token {token.key}"
        }
    

class TestExampleIsAdminEndpoint (
    create.TestSendEmptyBody,
    create.TestSendValidBody,
    create.TestUnAuthorized,
    create.TestPermissionForbidden,
):  
    def get_body(self):
        return {
            'name': 'test'
        }
    
    def get_headers(self):
        user = User.objects.create(
            username = 'test',
            email = 'test@gmail.com',
            is_staff = True
        )
        token = Token.objects.create(user=user)
        return {
            'Authorization' : f"Token {token.key}"
        }
    

    def model_creation(self):
        return ExampleModel.objects.create(name='test')
    
    def get_url(self):
        return reverse('create-is-admin')

    def get_forbidden_headers(self):
        user = User.objects.create(
            username = 'test2',
            email = 'test2@gmail.com',
        )
        token = Token.objects.create(user=user)
        return {
            'Authorization' : f"Token {token.key}"
        }