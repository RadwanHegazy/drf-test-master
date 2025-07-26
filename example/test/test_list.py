from drf_test_master.testcases.get import list
from django.urls import reverse
from example.models import ExampleModel
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class TestExampleNoAuthEndpoint (
    list.TestGetEmptyResults,
    list.TestGetNotEmptyResults
):  
    
    def model_creation(self):
        return ExampleModel.objects.create(name='test')
    
    def get_url(self):
        return reverse('list-no-auth')

class TestExampleIsAuthEndpoint (
    list.TestGetEmptyResults,
    list.TestGetNotEmptyResults,
    list.TestUnAuthorized,
):  
    
    def model_creation(self):
        return ExampleModel.objects.create(name='test')
    
    def get_url(self):
        return reverse('list-is-auth')
    
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
    list.TestGetEmptyResults,
    list.TestGetNotEmptyResults,
    list.TestPermissionForbidden,
):  
    
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
        return reverse('list-is-admin')

    def get_forbidden_headers(self):
        user = User.objects.create(
            username = 'test2',
            email = 'test2@gmail.com',
        )
        token = Token.objects.create(user=user)
        return {
            'Authorization' : f"Token {token.key}"
        }