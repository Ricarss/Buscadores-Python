set1 = {1,2,3,4}
set2 = {3,4,5,6,7}

print(set1)
print(set2)

set1.add(10)

print(set1)

set3 = set1 | set2

print(set3)

set4 = set1 & set2
print(set4)

set5 = set1 - set2
print(set5)

set6 = set2 - set1
print(set6)

set7 = set1 ^ set2
print(set7)

set_uniques = set.union(set1,set2)
print(set_uniques)

# duplicate deleter

duplicate = [1,1,1,1,1,2,3,4,5,6,6,6]

non_duplicate = list(set(duplicate))

print(non_duplicate)