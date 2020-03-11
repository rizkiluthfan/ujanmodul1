def hastag(string):
    z = '#'
    x = string.split()
    for i in range(len(x)):
        z += str(x[i]).capitalize()
    print(z)

hastag('ibu ingin anak cantik jelita')