import pyotp
USERNAME = '#######@email.com'
PASSWORD = '########'

def get_username():
    return USERNAME

def get_password():
    return PASSWORD

def get_mfa_code():
    totp = pyotp.TOTP("############").now()
    return totp

# If this file is executed, OTP is printed.
if __name__ == "__main__":
    print(get_mfa_code())
