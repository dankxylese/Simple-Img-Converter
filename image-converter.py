from PIL import Image
import re
from os import listdir, makedirs
from os.path import isfile, join

os.makedirs(thumbs)

files = [f for f in listdir("raw") if isfile(join("raw", f))]
print(files, "\n")

print(len(files), "images gathered. Press 'Enter' to begin processing.")

input()

for j in range(0, len(files)):
	foo = Image.open("raw/"+files[j])
	i = str(foo.size)
	i = i[1:-1]
	k = i

	i = re.sub(r'\s', '', i).split(',')

	k = 0.7

	x = round(int(i[0])*k)
	y = round(int(i[1])*k)
	z = round(j/len(files)*100)

	foo = foo.resize((x,y),Image.ANTIALIAS)
	foo.save("thumbs/"+files[j],optimize=True,quality=75)
	print("[{z}%]".format(z=z), k, "compressed to", x, y, "down 70% at 75% quality.")
print("done")