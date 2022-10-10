# class StackNode:
#     def __init__(self,element,next):
#         self._element = element
#         self._next = next

class PrefixConverter:
    def __init__(self):
        self._stacklist = ['?']

    def push(self,data):
        self.stacklist.append(data)

    def peek(self):
        if self.stacklist:
            return self.stacklist[-1]
        else:
            return "Isi Stack Kosong"

    def pop(self):
        if self.stacklist:
            data = self.stacklist.pop(-1)
            return data
        else:
            return "Isi Stack Kosong"

    def cekValidExpression(self,expression):
        if "(" or "()" in expression:
            print("Expresi Infix yang anda masukkan tidak valid!!")
        else:
            return True

    def infixToPrefix(self,expression):
        if " " in expression:
            expression = expression.split()
            if not self.cekValidExpression(expression):
                return "Expression yang dimasukkan tidak valid"
            else:
                return "Expression Prefix-nya adalah: "
        op = []
        baru = []

        for i in expression:
            if i.isdigit():
                baru.append(i)
            elif

        

if __name__ == '__main__':
    expressi1 = PrefixConverter()
    print(expressi1.infixToPrefix("1+2+3*4/2-1"))
    print(expressi1.infixToPrefix("A * (B + C) / D"))
    print(expressi1.infixToPrefix("(1+2)*3"))
    print(expressi1.infixToPrefix("20 * 3 - 10 + 289"))
    print(expressi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))