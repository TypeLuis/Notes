from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

users = {
    "john": "hello",  # key value pair is username and password
    "susan": "bye"
}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            users[username] == password:
        # check_password_hash(users.get(username), password):
        return username
