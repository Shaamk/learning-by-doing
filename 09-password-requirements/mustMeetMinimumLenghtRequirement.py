class MustMeetMinimumLenghtRequirement():
    # def __init__(self, requirements):
    #     self.requirements = requirements
    
    def check(self, password):
        if len(password) >= 8:
            return True
        else:
            return False
        
    def message(self):
        return f"The password must contain at least 8 characters"