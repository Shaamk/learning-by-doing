class PassWordChecker():
    def __init__(self, requirements):
        self.requirements = requirements

    
    def check(self, password):
        self.password = password
        full_requirement = True
        for requirement in self.requirements:
            succes = requirement.check(password)
            full_requirement = full_requirement and succes
        return full_requirement
    

    def messages(self):
        returning_messages_list = []
        for requirement in self.requirements:
            if not requirement.check(self.password):
                returning_messages_list.append(requirement.message())            
        return returning_messages_list
