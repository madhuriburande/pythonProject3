import  test_module 
from test_module import cities_list
## Access the first city
city=test_module.cities_list[1]
print("Accessing first city in list:=",city)

####revser list
for i in range(len(cities_list)-1,-1,-1):
    
    print(cities_list[i],end=' ')
print()

cities=test_module.cities_list

print("Accessing all cities in list",cities)
