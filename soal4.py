# size = int(input('Input hollow Triangle: '))
# z = ''
# for j in range (size+1):
#     if j < size:
#         for k in range (1,size*2):
#             if k <=size-j or k >= size+j:
#                 z += '#'
#             else:
#                 z += '_'
#         z += '\n'            

# print(z)


# kolom = int(input('masukan row: '))
# for row in range(1,kolom+1):
#     for col in range(1,2*kolom):
#         if row == kolom or row+col == kolom+1 or col-row == kolom-1:
#             print('#', end='')
#         else:
#             print(end='_')
#     print()
culum = int(input('Masukan berapa nomor row: '))
x = 2
for y in range(1,culum+1):
    for z in range(1,2*culum):
        if  y+z == culum+1 or z-y == culum-1:
            print('#', end='')
        elif y == culum and z != x:
            print('#',end='')
            x += 2
        else:
            print(end='_')
    print()