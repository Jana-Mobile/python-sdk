#!/usr/bin/env python

from jana_api.client import Client

def fetch_irl_url(client_id, secret_key, offer_id, api_url=None):
    client = Client(client_id, secret_key, api_url)
    response = client.get_jia_link(offer_id)
    if response and response['success']:
        return (True, response['link'])
    else:
        return (False, response['error'])
    

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 4 or len(sys.argv) > 5:
        sys.stderr.write('Usage: retrieve_url.py <client_id> <secret_key> <offer_id> [api_url]\n')
        sys.exit(1)
    
    client_id = sys.argv[1]
    secret_key = sys.argv[2]
    offer_id = sys.argv[3]

    api_url = None
    if len(sys.argv) == 5:
        api_url = sys.argv[4]
        
    result = fetch_irl_url(client_id, secret_key, offer_id, api_url)

    if result[0]:
        print "url retrieved: " + result[1]
    else:
        print "error: " + result[1]

    
