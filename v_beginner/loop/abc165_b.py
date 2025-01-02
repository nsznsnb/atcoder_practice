X = int(input())

i = 0
saving = 100
while saving < X:
    i += 1
    saving += saving // 100

print(i)