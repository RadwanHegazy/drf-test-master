from ..base import BaseTestCase


class BaseCreate (BaseTestCase) : 

    def get_body(self) : 
        raise NotImplementedError("Subclasses must implement get_body method")


class TestUnAuthorized (BaseCreate) : 

    def test_unauthenticated (self) : 
        req = self.client.post(
            self.get_url(),
            data=self.get_body(),
        )

        self.assertEqual(req.status_code, 401)
        return req


class TestPermissionForbidden (BaseCreate) : 

    def get_forbidden_headers (self) :
        raise NotImplementedError("Subclasses must implement get_forbidden_headers method")
    
    def test_permission_forbidden (self) : 
        headers = self.get_forbidden_headers()
        req = self.client.post(
            self.get_url(),
            headers=headers,
            data=self.get_body(),
        )

        self.assertEqual(req.status_code, 403)
        return req


class TestSendEmptyBody (BaseTestCase) : 

    def test_send_empty_body (self) : 
        headers = self.get_headers()

        if headers :
            req = self.client.post(
                self.get_url(),
                headers=headers,
            )
        else:
            req = self.client.post(
                self.get_url(),
            )

        self.assertEqual(req.status_code, 400)
        return req

class TestSendValidBody (BaseCreate) : 

    def test_send_valid_body (self) : 
        headers = self.get_headers()

        if headers :
            req = self.client.post(
                self.get_url(),
                headers=headers,
                data=self.get_body(),
            )
        else:
            req = self.client.post(
                self.get_url(),
                data=self.get_body(),
            )

        self.assertEqual(req.status_code, 201)
        return req