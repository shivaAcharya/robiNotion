import pyotp
USERNAME = '#######@gmail.com'
PASSWORD = '########'

def get_username():
    return USERNAME

def get_password():
    return PASSWORD

def get_mfa_code():
    totp = pyotp.TOTP("############").now()
    return totp
