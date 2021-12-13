import tokenize
result=[]
token_counts ={}
index = 0
with tokenize.open('hello.py') as f:
    tokens = tokenize.generate_tokens(f.readline)
    listm = []
    for token in tokens:
        print(token)
        if(token.string == '\n'):
            if(len(listm)!=0):
                result.append(listm)
            listm=[]
        else:
            listm.append(token.string)
print(result[0][0])
        
for sentence in result:
    for i in range(len(sentence)):
        #print(sentence[i])
        if(token_counts.get(sentence[i])==None):
           token_counts[sentence[i]] = 1
        else:
           token_counts[sentence[i]] += 1

token_counts = {" ".join(token): counts for token, counts in token_counts.items()}
print("----------")
print("Token Result = ", result)
print("\n")
print("token_counts : ", token_counts)
'''
num_merges = 10
for i in range(num_merges):
    pairs = get_stats(token_counts)
    best = max(pairs, key=pairs.get)
    token_counts = merge_vocab(best, token_counts)
    print(f'Step {i+1}')
    print(best)
    print(token_counts)
    print('\\n')
   '''        

