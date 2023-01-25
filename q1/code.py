class AIChatBot:
    def showSubjectName(self):
        print('AI for robot system')
    def showStudentYear(self,id:str):
        print(66-int(id[:2]))
    def calculator(self,a,op,b):
        if op == '*' :
            print(a*b)
        elif op == '-' :
            print(a-b)
        elif op == '+' :
            print(a+b)
        elif op == '/' :
            print(a/b)
        elif op == '^' or op=='**':
            print(a**b)
        else:
            print('')


if __name__ == "__main__":
    ChatBot = AIChatBot()
    while True:
        command = input()
        if command.lower()=='subject':
            ChatBot.showSubjectName()
        elif command.lower()=='year':
            d = input()
            ChatBot.showStudentYear(d)
        elif command.lower()=='calc':
            op = input()
            a = int(input())
            b = int(input())
            ChatBot.calculator(a,op,b)
        else:
            print('unknown command')


        