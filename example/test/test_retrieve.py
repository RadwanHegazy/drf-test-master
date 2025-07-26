from drf_test_master.testcases.get import retrieve 
from example.models import ExampleModel
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class TestExampleNoAuthRetrieveEndpoint(
    retrieve.TestNotFoundResource,
    retrieve.TestResourceExists,
):  
    
    def model_creation(self):
        return ExampleModel.objects.create(name='test')
    
    def get_url(self, id):
        return reverse('retrieve-no-auth', args=[id])
    
class TestExampleIsAuthRetrieveEndpoint(
    retrieve.TestUnAuthorized,
    retrieve.TestNotFoundResource,
    retrieve.TestResourceExists,
):  
    
    def model_creation(self):
        return ExampleModel.objects.create(name='test')
    
    def get_url(self, id):
        return reverse('retrieve-is-auth', args=[id])
    
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
    retrieve.TestForbidden,
    retrieve.TestNotFoundResource,
    retrieve.TestResourceExists,
):  
    
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
        return reverse('retrieve-is-admin', args=[id])

    def get_headers(self):
        user = User.objects.create(
            username='test',
            email = 'test@gmail.com',
            is_staff=True)
        token = Token.objects.create(user=user)
        return {
            "Authorization": f"Token {token.key}"
        }