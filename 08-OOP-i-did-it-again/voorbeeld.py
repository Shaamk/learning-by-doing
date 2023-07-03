class Voorbeeld:
    def __init__(self, parameter):
        self.attribute = parameter

voorbeeld_instance = Voorbeeld('In de Init')
instance_attribuut = voorbeeld_instance.attribute
print('ik heb dit uitgelezen als de atribuut waarde:', instance_attribuut)

voorbeeld_instance.attribute = 'nieuwe waarde'
print('Dit is nu het verschil:', instance_attribuut, ' en de Nieuwe:', voorbeeld_instance.attribute)