### Factory ###

# F
# aa
# ccc
# tttt
# ooooo
# rrrrrr
# yyyyyyy

message = "Factory"

for i in range(len(message)):
    print(message[i] * (i + 1))


### Factory ###

# F******
# aa*****
# ccc****
# tttt***
# ooooo**
# rrrrrr*
# yyyyyyy

message = "Factory"

for i in range(len(message)):
    # print(message[i] * (i + 1) + "*" * (len(message) -1 - i))     my solution
    print(message[i] * (i + 1), end="*" * (len(message) -1 - i))
    print()