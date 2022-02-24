







    
with open('new 2.txt') as f:
    flat_list=[word for line in f for word in line.split()]
           

print(flat_list)