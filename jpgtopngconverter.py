import sys
import os
from PIL import Image

# grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check if new exists and if not create it
if not os.path.exists(output_folder):
	os.makedirs( output_folder)

#loop thru img folder
for filename in os.listdir(image_folder):
	img = Image.open(f"{image_folder}{filename}")
	clean_name = os.path.splitext(filename)[0]
	#covert to png #save to the new folder
	img.save(f"{output_folder}{clean_name}.png", "png")
	print("Ready")