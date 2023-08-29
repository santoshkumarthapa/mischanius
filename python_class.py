class parent:
    def __init__(self, message):
        print(message)
        pass
    def show(self):
        print("parent class")
        
class child(parent):
    def __init__(self):
        super().__init__("a new ")
        print("hello world")
        
    def show(self):
        super().show()
        print("child class")
if __name__ == "__main__":
    obj = child()
    obj.show()
    
        