import requests, sys

EMAIL = 'chest.sammm@gmail.com'
PASSWORD = 'BadgerPlenty1'

URL = 'www.pof.com'

def main():
    # Start session
    session = requests.session(config={'verbose':sys.stderr})

    login_data = {
        'username': EMAIL,
        'password': PASSWORD,
        'submit': 'login',
    }

    # auth
    r = session.post(URL, data=login_data)
    print('session post')
    print(r)
    
    # access restricted page
    r = session.get('www.pof.com/viewmatches.aspx')

    print('session restricted')
    print(r)
