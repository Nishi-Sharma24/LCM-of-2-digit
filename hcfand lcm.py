a=int(input("Enter the first digit:"))
b=int(input("Enter the second digit:"))
HCF=1
if a>b:
    small=b
else:
    small=a
for x in range(2,small+1):
    if a%x==0 and b%x==0:
        HCF=x  
        print("The HCF is",HCF)
LCM=(a*b)/HCF
print("THE LCM is",LCM)
input()
    
    
