from PIL import Image

# insert the image below
# and the image should be black and white

img = Image.open('monalisa.jpg', 'r')

pix_val = list(img.getdata())

a, b = img.size
# print(pix_val)
# print(a, b)

# The White pixel is represented by "  "
# And Black pixel is represented by "# "

i = 0
s = 1
for j in pix_val:
    x = pix_val[i]
    if s % a == 0:
        if x >= 49:
            print('  ')
        else:
            print('# ')
    else:
        if x >= 49:
            print('  ', end="")
        else:
            print('# ', end='')
    i = i+1
    s = s+1
