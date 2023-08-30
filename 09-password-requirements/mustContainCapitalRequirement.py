class MustContainCapitalRequirement():
    # def __init__(self, requirements):
    #     self.requirements = requirements
    
    def check(self, password):
        if [i for i in password if i.isupper()]:
            return True
        else:
            return False
        
    def message(self):
        return f"The password must contain at least one capital"
    