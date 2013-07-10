import time, random, json, base64, hashlib, hmac
import requests

DEFAULT_API_URL = 'https://api.jana.com/api/'
MAX_NONCE = 999999999

class Client(object):

    def __init__(self, client_id, secret_key, api_url=None):
        self.client_id = client_id
        self.secret_key = secret_key
        if api_url is None:
            self.api_url = DEFAULT_API_URL
        else:
            self.api_url = api_url

    def get_jia_link(self, offer_id):
        data = self.base_request_data()
        data['method'] = 'jia-request'
        data['offer'] = offer_id

        encoded = self.encode_data(data)
        sig = self.sign_data(encoded)

        response = self.post_to_jana(encoded, sig, 'jia-request')
        
        return response

    def base_request_data(self):
        return {
            'algorithm': 'HMAC-SHA256',
            'timestamp': int(time.time()),
            'nonce': random.randint(0, MAX_NONCE),
            'client_id': self.client_id            
        }

    def encode_data(self, data):
        json_str = json.dumps(data)
        encoded = base64.urlsafe_b64encode(json_str).rstrip('=')
        return encoded

    def sign_data(self, data):
        sig = hmac.new(self.secret_key, msg=data, digestmod=hashlib.sha256).digest()
        encoded_sig = base64.urlsafe_b64encode(sig).rstrip('=')
        return encoded_sig        

    def post_to_jana(self, encoded, sig, method):
        url = self.api_url + method
        payload = { 'request' : encoded, 'sig' : sig }
        r = requests.post(url, data=payload)
        return r.json()
        
    


    