# 1024 to binary and hex
print(bin(1024))
print(hex(1024))

print(round(5.23222,2))

s = "hello how are you Mary, are you feeling okay?"
print(s.islower())

s = "twlksudfksj2wskjdjfwsdklf22w"
print(s.count('w'))

# Elements in set 1 not in set 2
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(set1.difference(set2))

# Elements in either set
print(set1.union(set2))

print({x:x**3 for x in range(5)})

[1,2,3,4].reverse()