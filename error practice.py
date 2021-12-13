import tokenize
import sys
result=[]
token_counts ={}
index = 0
tokens = []
line = 0
error=['SyntaxError', 'NameError', 'AttributeError', 'ValueError', 'TypeError', 'IndexError', 'ImportError']
ErrorName = ""
ErrorM = ""
Error=[]

def token_error(name):
    global ErrorName
    global ErrorM
    global Error
    global line
    with tokenize.open(name) as f:
        tokens = tokenize.generate_tokens(f.readline)
        for token in tokens:
            print(token)
            if (token.string== 'line'):
                line = int(next(tokens).string)
                #print(type(line))
                #print("line : ", line)
            if(token.string != ":" and ErrorName != ""):
                ErrorM += token.string + " "
            if(token.string in error):
                #print("Error token : ", token.string)
                ErrorName = token.string
        Error.append(line)
        Error.append(ErrorName)
        Error.append(ErrorM)

error_message = ""
for i in range(4):
    error_message = error_message + str(sys.stdin.readline())
print("error_message : " , error_message)
k = open("error1.txt", "w")
k.write(error_message)
k.close()
token_error("error1.txt")

print("line : ", line)
print("ErrorName : ", ErrorName)
print("ErrorM : ", ErrorM)
print("Error : ", Error)
