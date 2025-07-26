from rest_framework.test import APITestCase

class BaseTestCase (
    APITestCase
) : 

    def model_creation(self) :
        """Method for create the dummy data of your model"""
        raise NotImplementedError("please override on `model_creation` method")

    
    def get_url(self, *args, **kwargs) : 
        """The url for testing"""
        raise NotImplementedError("please override on `get_url` method")
    
    def get_headers(self) : 
        """Get header of custom user to implement an action"""
        return None