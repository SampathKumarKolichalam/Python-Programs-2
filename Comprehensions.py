#List Comprehensions:-
num=[1,2,3,4,5,6]
even_list=[i for i in num if i%2==0]
sq_num=[i*i for i in num]
print(even_list)
print(sq_num)
#Set Comprehensions:-
s=set([1,2,3,4,3,2])
print(s)
even_set={i for i in s if i%2==0}
print(even_set)
#Dictionary Comprehensions:-
cities=["Hyderabad","Melbourne","New york"]
countries=["India","Australia","USA"]
z=zip(cities,countries)
dict={city:country for city,country in zip(cities,countries)}
print(dict)