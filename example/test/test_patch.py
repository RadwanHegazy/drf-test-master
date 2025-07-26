from drf_test_master.testcases.update import patch
from example.models import ExampleModel
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class TestExampleNoAuthRetrieveEndpoint(
    patch.TestNotFoundResource,
    patch.TestUpdateSuccess,
    patch.TestSendEmptyBody
):  
    def get_body(self):
        return {
            'number' : 45
        }
    
    def model_creation(self):
        return ExampleModel.objects.create(name='test')
    
    def get_url(self, id):
        return reverse('update-no-auth', args=[id])
    
    
class TestExampleIsAuthRetrieveEndpoint(
    patch.TestUnAuthorized,
    patch.TestNotFoundResource,
    patch.TestUpdateSuccess,
    patch.TestSendEmptyBody
):  
    def get_body(self):
        return {
            'name': 'new name'
        }
    
    def model_creation(self):
        return ExampleModel.objects.create(name='test')
    
    def get_url(self, id):
        return reverse('update-is-auth', args=[id])
    
    def get_headers(self):
        user = User.objects.create(
            username='test',
            email = 'test@gmail.com',
        )
        token = Token.objects.create(user=user)
        return {
            "Authorization": f"Token {token.key}"
        }

class TestExampleIsAdminRetrieveEndpoint(
    patch.TestUnAuthorized,
    patch.TestNotFoundResource,
    patch.TestUpdateSuccess,
    patch.TestSendEmptyBody,
    patch.TestForbidden,
):  
    
    def get_body(self):
        return {
            'name': 'new name'
        }
    
    def model_creation(self):
        return ExampleModel.objects.create(name='test')
    
    def get_forbidden_headers(self):
        user = User.objects.create(
            username='test',
            email = 'test@gmail.com',
            is_staff=False
            )
        token = Token.objects.create(user=user)
        return {
            "Authorization": f"Token {token.key}"
        }
    
    def get_url(self, id):
        return reverse('update-is-admin', args=[id])

    def get_headers(self):
        user = User.objects.create(
            username='test',
            email = 'test@gmail.com',
            is_staff=True)
        token = Token.objects.create(user=user)
        return {
            "Authorization": f"Token {token.key}"
        }