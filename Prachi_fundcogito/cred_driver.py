'''
We are creting the credential class and declaring one user over here
In production environment we can follow  similar practices for the config files
creating user for the different environment
'''

class credential:
    def __init__(self, username, password):
        self.username = username
        self.password = password




prachi_credentials=credential("prachikolte25@gmail.com", 'MY7NsWfXL2CYPWu!')