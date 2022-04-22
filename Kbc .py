
print("hello everyone")
print("__welcome to KBC__")
print("**very good luck for your game**")
print("so lets play the game")
question=["what is the capital of india ?","how many colours in rainbow ?","how many girls in navgurukul ?","which courses we are doing in navgurukul ?"]
options=[["bihar","delhi","kolkata","canada"],["8","9","7","10"],["118","120","100","104"],["beauty parlour","swimming","fashion designer","engineer courses"]]
lifeline=[["bihar","delhi"],["7","10"],["120","118"],["engineer course","fashion designer"]]
solution=[2,3,2,4]
solution1=[2,1,1,1]
i=0
count=0
while i<len(question[i]):
    print("Q.",i+1,question[i])
    j=0
    while j<len(options[i]):
        print(j+1,options[i][j])
        j+=1
    user=int(input("choose your option"))
    if user==solution[i]:
        print("wow!! congratulations")
    elif user==5050:
        if count==0:
            k=0
            while k<len(lifeline[i]):
                print(k+1,lifeline[i][k])
                k+=1
            count+=1
            user1=int(input("enter"))
            if user1==solution1[i]:
                print("you are right")
            else:
                print("wrong")
                break
        else:
            print("oops! you already used")
            num=int(input("enter any number"))
            if num==solution[i]:
                print("correct")
            else:
                print("oops! sorry")
    else:
        print("wrong...better luck for the next time")
        break
    i+=1 