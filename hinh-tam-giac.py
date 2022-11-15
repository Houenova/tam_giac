a=float(input("nhập a= "))
b=float(input("nhập b= "))
c=float(input("nhập c= "))

dk1= a+b>c and b+c>a and c+a>b 
dk2= a>0 and b>0 and c>0 
if (dk1 and dk2):
    d=a+b+c
    print("chu vi tam giác",d)
    g=(a+b+c)/2
    print("diện tích hình tam giác",1/2*g*c )
else: 
    print("đây ko phải tam giác")
