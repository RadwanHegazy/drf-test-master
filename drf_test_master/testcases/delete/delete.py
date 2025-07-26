from ..base import BaseTestCase


class TestUnAuthorized (BaseTestCase) : 

    def test_unauthorized (self) : 
        model = self.model_creation()
        req = self.client.delete(
            self.get_url(model.id),
        )

        self.assertEqual(req.status_code, 401)
        return req


class TestForbidden (BaseTestCase) : 

    def get_forbidden_headers (self) : 
        raise NotImplementedError("Subclasses must implement get_forbidden_headers method")
    
    def test_forbidden (self) :
        headers = self.get_forbidden_headers() 
        model = self.model_creation()
        req = self.client.delete(
            self.get_url(model.id),
            headers=headers
        )
        self.assertEqual(req.status_code, 403)
        return req


class TestNotFoundResource (BaseTestCase) :

    def test_not_found_resources (self) : 
        headers = self.get_headers()

        if headers:
            req = self.client.delete(
                self.get_url(999),
                headers=headers
            )
        else:
            req = self.client.delete(
                self.get_url(999),
            )   
        
        self.assertEqual(
            req.status_code,
            404
        )
        return req

class TestResourceExists (BaseTestCase) :

    def test_resources_exists (self) : 
        headers = self.get_headers()
        model = self.model_creation()
        if headers:
            req = self.client.delete(
                self.get_url(model.id),
                headers=headers
            )
        else:
            req = self.client.delete(
                self.get_url(model.id),
            )   
        
        self.assertEqual(
            req.status_code,
            204
        )
        return req
        