''' write a loop to creat a list of even numbers between 1 to 10 ?'''

even = []
odd = []


for i in range(1, 11):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers:", even)
print("Odd numbers:", odd)  


