import requests

class BaseApiClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token

    def set_token(self,token):
        self.token = token
    
    def _headers(self):
        headers = {"Content-Type" : "application/json"}

        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        
        return headers
    
    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, self._headers(), **kwargs)
        response.raise_for_status()
        return response.json()
    
class ProductApi(BaseApiClient):
    def get_all(self):
        return self._request("GET", "/products")
    
    def get_by_id(self, product_id):
        return self._request("GET", f"/products/{product_id}")
    
    def create(self, data):
        return self._request("POST", "/products", data)
    
    def update(self, data):
        return self._request("PUT", "/products", data)
    
    def delete(self, product_id):
        return self._request("DELETE", f"/products/{product_id}")
    
class UserApi(BaseApiClient):
    def get_all(self):
        return self._request("GET", "/users/")
    
    def get_by_id(self, user_id):
        return self._request("GET", f"/users/{user_id}")
    
    def create(self, data):
        return self._request("POST", "/users/", data)
    

class AuthApi(BaseApiClient):
    def login(self, email, password):
        return self._request("POST", "/auth/login", json={"email" : email , "password" : password})