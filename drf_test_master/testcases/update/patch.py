from ..base import BaseTestCase

class BaseUpdate (BaseTestCase) : 
    
    def get_body(self) : 
        raise NotImplementedError("Subclasses must implement get_body method")

class TestUnAuthorized (BaseUpdate) : 

    def test_unauthorized (self) : 
        model = self.model_creation()
        req = self.client.patch(
            self.get_url(model.id),
            data=self.get_body(),
        )

        self.assertEqual(req.status_code, 401)

        return req

class TestForbidden (BaseUpdate) : 

    def get_forbidden_headers (self) : 
        raise NotImplementedError("Subclasses must implement get_forbidden_headers method")
    
    def test_forbidden (self) :
        headers = self.get_forbidden_headers() 
        model = self.model_creation()
        req = self.client.patch(
            self.get_url(model.id),
            headers=headers,
            data=self.get_body(),
        )
        self.assertEqual(req.status_code, 403)

        return req

class TestNotFoundResource (BaseUpdate) :

    def test_not_found_resources (self) : 
        headers = self.get_headers()

        if headers:
            req = self.client.patch(
                self.get_url(999),
                headers=headers,
                data=self.get_body()
            )
        else:
            req = self.client.patch(
                self.get_url(999),
                data=self.get_body()
            )   
        
        self.assertEqual(
            req.status_code,
            404
        )

        return req

class TestUpdateSuccess (BaseUpdate) :

    def test_update_success (self) : 
        headers = self.get_headers()
        model = self.model_creation()
        if headers:
            req = self.client.patch(
                self.get_url(model.id),
                headers=headers,
                data=self.get_body(),
            )
        else:
            req = self.client.patch(
                self.get_url(model.id),
                data=self.get_body(),
            )   
        
        self.assertEqual(
            req.status_code,
            200
        )

        return req

class TestSendEmptyBody (BaseUpdate) : 

    def test_send_empty_body (self) : 
        headers = self.get_headers()
        model = self.model_creation()
        if headers :
            req = self.client.patch(
                self.get_url(model.id),
                headers=headers,
            )
        else:
            req = self.client.patch(
                self.get_url(model.id),
            )

        self.assertEqual(req.status_code, 200)

        return req