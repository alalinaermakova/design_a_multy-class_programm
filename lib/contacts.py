class Contacts:
        
        def __init__(self, name, tel):
                self.name = name
                self.tel = tel
                pass
        
        def format(self):
                return f"{self.name}'s tel: {self.tel}"
                pass