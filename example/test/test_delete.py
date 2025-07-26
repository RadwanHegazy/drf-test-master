from drf_test_master.testcases import delete 
from example.models import ExampleModel
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class TestExampleNoAuthRetrieveEndpoint(
    delete.TestNotFoundResource,
    delete.TestResourceExists,
):  
    
    def model_creation(self):
        return ExampleModel.objects.create(name='test')
    
    def get_url(self, id):
        return reverse('delete-no-auth', args=[id])
    
class TestExampleIsAuthRetrieveEndpoint(
    delete.TestUnAuthorized,
    delete.TestNotFoundResource,
    delete.TestResourceExists,
):  
    
    def model_creation(self):
        return ExampleModel.objects.create(name='test')
    
    def get_url(self, id):
        return reverse('delete-is-auth', args=[id])
    
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
    delete.TestForbidden,
    delete.TestNotFoundResource,
    delete.TestResourceExists,
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
        return reverse('delete-is-admin', args=[id])

    def get_headers(self):
        user = User.objects.create(
            username='test',
            email = 'test@gmail.com',
            is_staff=True)
        token = Token.objects.create(user=user)
        return {
            "Authorization": f"Token {token.key}"
        }