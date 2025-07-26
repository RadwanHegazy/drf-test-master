from ..base import BaseTestCase


class BaseList (BaseTestCase) : 

    def data_response_key (self) : 
        return None
    


class TestUnAuthorized (BaseTestCase) : 

    def test_unauthenticated (self) : 
        req = self.client.get(
            self.get_url()
        )

        self.assertEqual(req.status_code, 401)

        return req

class TestPermissionForbidden (BaseTestCase) : 

    def get_forbidden_headers (self) :
        raise NotImplementedError("Subclasses must implement get_forbidden_headers method")
    
    def test_permission_forbidden (self) : 
        headers = self.get_forbidden_headers()
        req = self.client.get(
            self.get_url(),
            headers=headers
        )

        self.assertEqual(req.status_code, 403)
        return req

class TestGetEmptyResults (BaseList) : 

    def test_get_empty_results (self) : 
        headers = self.get_headers()

        if headers :
            req = self.client.get(
                self.get_url(),
                headers=headers
            )
        else:
            req = self.client.get(
                self.get_url(),
            )

        self.assertEqual(req.status_code, 200)

        key = self.data_response_key()  
        if key :
            self.assertEqual(req.json()[key], [])
        else:
            self.assertEqual(req.json(), [])
        
        return req
    

class TestGetNotEmptyResults (BaseList) : 

    def test_get_not_empty_results (self) : 
        headers = self.get_headers()
        self.model_creation()
        if headers :
            req = self.client.get(
                self.get_url(),
                headers=headers
            )
        else:
            req = self.client.get(
                self.get_url(),
            )

        self.assertEqual(req.status_code, 200)

        key = self.data_response_key()  
        if key :
            self.assertNotEqual(req.json()[key], [])
        else:
            self.assertNotEqual(req.json(), [])

        return req    