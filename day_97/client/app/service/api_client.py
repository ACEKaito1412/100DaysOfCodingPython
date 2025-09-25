import requests
from flask import jsonify

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
        try:
            url = f"{self.base_url}{endpoint}"
            response = requests.request(method, url, headers=self._headers(), **kwargs)
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return None
        except requests.exceptions.RequestException as req_err:
            return None


class OrdersApi(BaseApiClient):
    def get_all(self):
        return self._request("GET", "/orders")
    
    def search(self, query):
        return self._request("GET", f"/orders/search?q={query}")
    
    def get_by_id(self, orders_id):
        return self._request("GET", f"/orders/{orders_id}")
    
    def create(self, data):
        return self._request("POST", "/orders", json=data)
    
    def update(self, data, orders_id):
        return self._request("PUT", f"/orders/{orders_id}",json=data)
    
    def delete(self, orders_id):
        return self._request("DELETE", f"/orders/{orders_id}")
    
class ProductApi(BaseApiClient):
    def get_all(self):
        return self._request("GET", "/products")
    
    def search(self, query):
        return self._request("GET", f"/products/search?q={query}")
    
    def get_by_id(self, product_id):
        return self._request("GET", f"/products/{product_id}")
    
    def create(self, data):
        return self._request("POST", "/products", json=data)
    
    def update(self, data, product_id):
        return self._request("PUT", f"/products/{product_id}",json=data)
    
    def delete(self, product_id):
        return self._request("DELETE", f"/products/{product_id}")
    
        
     
class CartApi(BaseApiClient):
    def get_by_id(self):
        return self._request("GET", f"/carts/")
    
    def create(self, data):
        return self._request("POST", "/carts", json=data)
    
    def search(self, query):
        return self._request("GET", f"/carts/search?q={query}")
    
    def add_item(self, data):
        return self._request("PUT", f"/carts/", json=data)
    
    def update(self, data, cart_id):
        return self._request("PUT", f"/carts/{cart_id}", json=data)
    
    def delete(self, cart_id):
        return self._request("DELETE", f"/carts/{cart_id}")
    

class PaymentApi(BaseApiClient):
    def create_order(self, cart_id, data):
        return self._request("POST", f"/payment/create-order/{cart_id}", json=data)
    
    def capture_order(self, data):
        return self._request("GET", f"/payment/capture-order", json=data)
    
class UserApi(BaseApiClient):
    def get_all(self):
        return self._request("GET", "/users/")
    
    def search(self, query):
        return self._request("GET", f"/users/search?q={query}")
    
    def get_by_id(self, user_id):
        return self._request("GET", f"/users/{user_id}")
    
    def create(self, data):
        return self._request("POST", "/users/", json=data)
    
    def update(self, data, user_id):
        return self._request("PUT", f"/users/{user_id}", json=data)
    

class AuthApi(BaseApiClient):
    def login(self, email, password):
        return self._request("POST", "/auth/", json={"email" : email , "password" : password})