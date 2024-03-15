import random
print('''           欢迎参加猜单词游戏
    请把下列个字母组合成一个正确的单词''')
word_list=["college","English","test","band","four","part","two","listen","comprehension","section","direction","in","this","section","you","will","hear","three","news","report","at","the","end","of","each","news","report","you","will","hear","two","or","three","question","both","the","news","report","and","the","question","will","be","spoken","only","once"]
while(True):
    index=random.randint(0,len(word_list)-1)
    ans=word_list[index]
    ans=list(ans)
    random.shuffle(ans)
    ansstr=''
    for i in range(len(ans)):
        ansstr+=ans[i]
    print(f'乱序后单词:{ansstr}')
    a=input('请你猜:')
    while a not in word_list:
        print('对不起不正确')
        a=input('继续猜:')
    else:
        print('真棒，你猜对了!')
        next=input('是否继续(Y/N):')
        if next=='y':
            continue
        elif next=='n':
            break
