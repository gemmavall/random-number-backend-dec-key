import requests

def get_key_using_keyid(KEY_ID):
    # Define the URL
    url = "https://192.36.164.182/api/v1/keys/alice_client1/dec_keys?key_ID="+KEY_ID

    # Define the paths to the certificates and key
    ca_cert = "rootCA_auth.crt"
    client_cert = "bob_client1.crt"
    client_key = "bob_client1.key"

    # Set the headers
    headers = {
        "Content-Type": "application/json"
    }

    # Make the request with the certificates and key
    response = requests.get(
        url,
        headers=headers,
        cert=(client_cert, client_key),
        verify=ca_cert
    )

    result = response.json()
    return result['keys'][0]