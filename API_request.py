import requests
import json

def fetch_and_store_json(url, headers, params, output_file='data.json'):
    """
    Fetch JSON data from the specified API and store it in a file.

    :param url: str - The API endpoint URL.
    :param headers: dict - The headers to include in the API request.
    :param params: dict - The parameters to include in the API request.
    :param output_file: str - The name of the output file (default is 'data.json').
    """
    try:
        # Make the GET request to the API
        response = requests.get(url, headers=headers, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            try: 
                # Parse the JSON response
                json_data = response.json()
                # Save the JSON data to a file
                with open(output_file, 'w') as json_file:
                    json.dump(json_data, json_file, indent=4)
                
                print(f'Data has been saved to {output_file}')
            except json.JSONDecodeError as e:
                print(f'JSON decode error {e}')
        else:
            print(f'Failed to fetch data: {response.status_code}, {response.text}')
    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == "__main__":
    # Example usage
    url = 'https://vmsn-app-planner3test.azurewebsites.net/status/market/bid-result'
    headers = {
        'accept': 'text/plain',
        'ApiKey': 'Api-Planner-996ba74c-cdaf-4f66-9448-ffff'
    }

    params = {
        'ForDate': '2024-02-03',
        'Market': 'FCR-D-D1',
        'CustomerId': 'TestCustomer',
        'Country': 'Sweden'
    }
    fetch_and_store_json(url, headers, params)
