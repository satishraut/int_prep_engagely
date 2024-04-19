# 1)
def question1():
    a=(10)
    return (type(a)) #<class 'int'>
def question2():
    #what will be the output
    try:
        print("Hi")
        return 1
    except:
        pass
    finally:
        return "Done!"
def question3():
    #remove duplates from two list and create unque one
    a=[1,2,3,4,5,6,7,8,9,10,50]
    b=[1,2,3,4,5,6,7,8,9,10,11,12]
    c=list(set(a).union(set(b)))
    return c
#print(question1())
#print(question2())
print(question3())

#