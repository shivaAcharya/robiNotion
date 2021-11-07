#Inspired from: https://github.com/jmfernandes/robin_stocks

import robin_stocks.robinhood as rh
import loginInfo
USER_NAME = loginInfo.get_username()
PASS_WORD = loginInfo.get_password()
MFA_CODE = loginInfo.get_mfa_code()

login = rh.login(USER_NAME, PASS_WORD, mfa_code = MFA_CODE)

my_stocks = rh.build_holdings()
my_stocks_price = {}

def get_stockInfo():
    return my_stocks
