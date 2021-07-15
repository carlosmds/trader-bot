from iqoptionapi.stable_api import IQ_Option

class User:
    def __init__(self, userInfo):
        self.username = userInfo["username"]
        self.password = userInfo["password"]
            
    def connect(self):
        
        IQOption = IQ_Option(self.username, self.password)
        
        # print(IQOption.get_profile_ansyc())
        
        return IQOption