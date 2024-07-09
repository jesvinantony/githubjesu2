count_Odd=0
Count_Even=0
for i in range(1,11):
    if (i%2==1):
        count_Odd=count_Odd+1
    else:
        Count_Even=Count_Even+1
        
print("Odd:", count_Odd)
print("Even:", Count_Even)


count=0
for i in range(1,100):
    if (i%3==0 and i%5==0):
        count=count+1

print(count)

count= int(input("Enter the Number:"))
for i in range(1,count+1):
    print(i)



for i in range(1,3):
    print("Week ", i)
    for j in range(1,4):
        print(" Day ", j)
