def main():
    a=0
    b=1
    for i in range(5):
        a,b = b,a+b
        print(b) 

main()