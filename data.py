import requests

def main():
    # URL of the endpoint for authentication
    auth_url = 'https://beta.ohmconnect.com/api/cold_cuts/authenticate'

    # URL of the endpoint you want to request after authentication
    data_url = 'https://beta.ohmconnect.com/api/cold_cuts/get_prices?products=pepperoni'

    # Request payload (username and password) in JSON format
    auth_payload = {
        "username": "hoagie_helper_prachik",
        "password": "VdcwuBa3fdHPpo_zbGUkWUHjlMrFe4T1"
    }

    # Headers for the authentication request
    auth_headers = {
        'Content-Type': 'application/json'
    }

    try:
        # Send a POST request with JSON payload for authentication
        auth_response = requests.post(auth_url, json=auth_payload, headers=auth_headers)

        # Check if the authentication request was successful (status code 200)
        if auth_response.status_code == 200:
            print("Authentication successful!")

            # Extract access token from the authentication response
            access_token = auth_response.json().get('accessToken')

            # Make another request using the access token
            if access_token:
                data_headers = {
                    'Authorization': f'bearer {access_token}'
                }

                # Send a GET request with the access token
                data_response = requests.get(data_url, headers=data_headers)

                # Check if the data request was successful (status code 200)
                if data_response.status_code == 200:
                    print("Data request successful!")
                    print("Data Response:")
                    print(data_response.json())
                else:
                    print("Data request failed with status code:", data_response.status_code)


            else:
                print("Access token not found in authentication response")
        else:
            print("Authentication failed with status code:", auth_response.status_code)
            print("Authentication Response:")
            print(auth_response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
