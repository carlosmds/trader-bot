# from iqoptionapi.stable_api import IQ_Option
from user import User

class Robot:
        def __init__(self, userInfo, mode):
            self.user = User(userInfo)
            self.mode = mode

        def work(self):
            
            Iq = self.user.connect()
            check, reason = Iq.connect()
  
            Iq.change_balance(self.mode)

            asset = "EURJPY"
            maxdict = 10
            size = 300
            duration = 1
            Iq.buy(1, asset, "put", duration)
            
            print("ok?")
            return
            
            