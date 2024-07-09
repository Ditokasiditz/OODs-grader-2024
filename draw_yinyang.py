inp = int(input("Enter Input : "))

#first line 
for i in range(inp+1):print('.',end='')
print('#+',end='')
for i in range(inp+1): print('+',end='')
print('')

#upper part 
for i in range(inp):
    for j in range(inp-i):
        print('.',end='')
    for j in range(i+2):
        print('#',end='')
    print('+',end='')
    for j in range(inp):
        print('#',end='')
    print('+')

#middle part 
for i in range(2):
    for j in range(inp+2):
        print('#',end='')
    for j in range(inp+2):
        print('+',end='')
    print('')

#under part 
for i in range(inp):
    print('#',end='')
    for j in range(inp):
        print('+',end='')
    print('#',end='')
    for j in range(inp+1-i):
        print('+',end='')
    for j in range(i+1):
        print('.',end='')
    print('')

# last line 
for i in range(inp+1): print('#',end='')
print('#+',end='')
for i in range(inp+1):print('.',end='')
