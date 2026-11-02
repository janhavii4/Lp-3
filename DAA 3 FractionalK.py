n =5
capacity = 60

weight = [5,10,15,22,25]
value = [30,40,45,77,90]

ratio = [value[i]/weight[i] for i in range(n)]

items = sorted(range(n),key=lambda i: ratio[i],reverse = True)

total_value = 0
print("Item selected:")

for i in items:
    if capacity == 0:
        break

    if weight[i] <=capacity:
        capacity -= weight[i]
        total_value += value[i]
        print("Item", i + 1,":Full item")
    else:
        fraction = capacity / weight[i]
        total_value += value[i]* fraction
        print("Item", i + 1,":", round(fraction,2),"fraction")             
        
        capacity = 0

print("Maximum value:", round(total_value,2))