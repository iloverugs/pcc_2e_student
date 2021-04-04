def one():
    var = 0
    for i in range(15):
        var += 1

    return var

def two():
    var = 0
    for i in range(15):
        var *= 1

    return var

print(one())
print(two())