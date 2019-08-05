def add(n1,n2):
    ans=n1+n2
    print(ans)
    
def sub(n1,n2):
    ans=n1-n2
    print(ans)
    
def mult(n1,n2):
    ans=n1*n2
    print(ans)
    
def div(n1,n2):
    ans=n1/n2
    print(ans)

n1=input("Enter a number:")
n2=input("Enter a number:")

print("\n1-Addition[+]")
print("2-Subtraction[-]")
print("3-Multiplication[*]")
print("4-Division[/]")

m=input("\nSelect a method:")

if m==1:
    add(n1,n2)
if m==2:
    sub(n1,n2)
if m==3:
    mult(n1,n2)
if m==4:
    div(n1,n2)
   
