
class MyInt(int):
    
    def __call__(self):
        print("you number!")

age = MyInt()

age()