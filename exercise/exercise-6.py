# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe() ” method (which prints “name” and “kind” in a sentence).
class Food:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def __repr__(self) -> str:
        return str(self.__dict__)
    # @classmethod
    def describe(self):
        return print("que rica {}, es un {}".format(self.name, self.kind))

    # def __repr__(self) -> str:
    #     return str(self.__dict__)
    
# Food().describe()

# 2) Try turning describe()  from an instance method into a class and a static method. Change it back to an instance method thereafter.

class Foodt:
    name = 'X'
    kind = 'K'

    @classmethod
    def describe(self):
        return print("que rica {}, es un {}".format(self.name, self.kind))

    # def __repr__(self) -> str:
    #     return str(self.__dict__)
Foodt.name = 'Torta'   
Foodt.kind = 'Dulce'
Foodt.describe()

class Foodr:
    @staticmethod
    def describe(name, kind):
        return print("que rica {}, es un {}".format(name,kind))

    # def __repr__(self) -> str:
    #     return str(self.__dict__)
Foodr.describe('Torta', 'DUlce')

# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.

class Meat(Food):
    def cook(self):
        print('cooking ')

# class Fruit(Food):
#     def clean(self):
#         print('cleannin')

# banana = Fruit('Bnana', 'asdasd')
# banana.clean()
# banana.describe()


b = Meat('s', 'e')
b.cook()
b.describe()

print(b)

# 4) Overwrite a “dunder” method to be able to print your “Food” class.