import pandas 
#milestone 1
#%%
print('This print statement was created in Python')
#%%
Age = 41
print('Age', Age)
#%%
long_word = 'Pneumonoultramicroscopicsilicovolcanoconiosis'
print(len(long_word))
first_c = long_word[0]
last_c = long_word[len(long_word)-1]
print(first_c + last_c)
#%%
h = 25/7
w = 25/2
l = 35

cuboid_volume = h * w * l
cuboid_surface = 2 * (h*w + h*l + l*w)

print('cuboid volume is ', cuboid_volume,' and cuboid surface area is ', cuboid_surface)
#%%
h = 10
r = 3
pi = 3.1415927

cone_volume = pi * r**2 *h/3
cone_surface = pi * r * (r + (r**2 + h**2)**0.5)

print('cone volume is ', cone_volume,' and cone surface area is ', cone_surface)
# %%
a = 42
b = 25
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(type(a * b))
print(type(a / b))
a = 4.2
print(type(a + b))
#%%
tomatoes_6 = 0.87
sugar_500 = 1.09
sponges_10 = 0.29
juice_1_5 = 1.89
foil_30 = 1.29
shopping_bill = 2 * sponges_10 + 2 * juice_1_5 + 2 * tomatoes_6
print(shopping_bill)
#%%
