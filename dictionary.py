a={ "abhi":100,
   "navadeep":50,
   "abhi":44,
   "abhi":43}
print(a ,type(a))
word=input("enter name")
print(a[word])
# METHODS OF DICTIONARY
b=dict.fromkeys(a,0)
print(b)
print(a.items())
print(a.values())
print(a.keys())
print(a.pop("abhi"))#remove key and return value of key
print(a.popitem())#remove and return last key value pair and print as touple
ams=a.setdefault("c",)#setdefault()
print(ams)
print(a)
a.update({"c":4,"d":6})
print(a)
print(a.get("c1"))#prints none
#print(a["c1"])#prints error
#PRACTICE 
s=set()
s.add(20)
s.add(20.0)
#in python 20 and 20.0 are same so len of s is 1 till here
s.add("20")
print(s)