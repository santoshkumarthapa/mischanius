class person():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    def __eq__(self, other):
        if not isinstance(other,person):
            raise NotImplemented
        return self.first_name ==other.first_name and self.last_name==other.last_name
    def custom(self,other):
        self.__class__ == other.__class__
    def __hash__(self):
        return (self.first_name, self.last_name).__hash__()
        
if __name__ == "__main__":
    per1 = person("rame", "thapa")
    per2 = person("rame", "thapa")
    print(per1.__eq__(per2))  
    print(per1 is per2)
    print(per1.__hash__())
    print(per2.__hash__())
    print(id(per1), id(per2))
    print(per1 is per2)
    D = {per1:1, per2:2}
    print(D)
    