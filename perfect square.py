n=int(input("Enter the number:"))
Flag =0
for i in range (1,n):
    if i*i==n :
        Flag =1
        break
if Flag==1:
    print("Perfect square")
else : 
    print("It's not a perfect square")