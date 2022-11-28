print("choose number of subjects from 3 and 5")
x=int(input("number of subjects:"))
count=1
t=0
a=0
b=0
c=0
d=0
f=0
s=1
z=students=2
if x==3 or x==5:
        while s<=z:
            print("name of student",s,":")
            y=input()
            while count<=x:
                print("marks of subject",count)
                i=float(input("marks:"))
                if i<=100:
                    t=float(t+i)
                    count=count+1
                    percent=float(t/x)
                    if a<t:
                      e=str(y)
                      a=t
                      if c<a :
                        b=str(y)
                        e=d
                        d=b
                        c=a
                        a=f
                        f=c

                else:
                    print("Invalid marks")                  
            print("The percentage is :",percent)
            if 94<=percent<=100:
                print("GPA is 4.0")
            if 85<=percent<=93:
                print("GPA is 4.0")
            if 80<=percent<=84:
                print("GPA is 3.7")
            if 75<=percent<=79:
                print("GPA is 3.4")
            if 70<=percent<=74:
                print("GPA is 3.0")
            if 67<=percent<=69:
                print("GPA is 2.7")
            if 64<=percent<=66:
                print("GPA is 2.4")
            if 60<=percent<=63:
                print("GPA is 2.0")
            if 57<=percent<=59:
                print("GPA is 1.7")
            if 54<=percent<=56:
                print("GPA is 1.4")
            if 50<=percent<=53:
                print("GPA is 1.0")
            if percent<50:
                print("Fail")
                
            s=s+1
            count=1
            t=0

        print("Student",b," secured first position")
        print("Student",e," secured second position")        
else:
    print("Invalid Number of subjects entered")
