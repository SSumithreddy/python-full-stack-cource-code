'''
for var in seq:
  #stmts

seq: list,tuple,set,dict,str,range


products = {'bread','butter','milk','suger','salt'}
for item in probucts
print(item)



products = {'bread': 30,'butter':50,'milk':20,'suger':45,'salt':60}
for item in products:
    print("product name: ",item)
    print("product price:",probucts[item])
    print("Buy now l add to cart")
    print("Add to fav")
    print('_________________________')

s = 'python programming'
for ch in s:
    print(ch)


#range(start,stop+1,step) = (0,step+1,1)


n = int(input("Enter the number: "))
for i in range(1,21):
    print(f'{n}*{i}={n*i}')


for i in range(10):
    if i==5:
        break
    print(i)
else:
    print("End of thr number")
'''
for i in range(5):
    user_pin = int(input("Enter the pin: "))
    if user_pin == pin:
        print("Login succesful")
        break
    else:
        print("Invalid password,trt again")
    else:
        print("you have reached the max attempts,try again 5 mins")
    
    


