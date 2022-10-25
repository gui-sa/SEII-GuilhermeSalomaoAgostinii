import numpy as np

l = [1,2,3]
a = np.array(l) #converting a list into an array
print(l)
print(a)

l.append(4) #puts 4 number into the end of the list
print(l)

#a.append(4) #doesnt have append method

l = l + [5] #puts 4 number into the end of the list

a = a + np.array([4]) # it wont append it... instead of it it will add 4 to every value inside its array
print(a)


l = l * 2  #it will append himself at the end of himself on time.
print(l)
 

a = a*2 #It will multilply element wisely for 2
print(a)

a = np.sqrt(a) #will get the square root of every element in a array
print(a)


a = np.log(a) #will get the log of every element in a array
print(a)

