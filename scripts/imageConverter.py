from PIL import Image
import numpy as np

# Import image to be converted
while True:
    try: 
        imageDirectory = input("Enter the name of the image to be converted (including file extension): ")
        image = Image.open(imageDirectory)
        break
    except FileNotFoundError:
        print("This image does not exist!")

# Conver to list of RGB pixels stored as tuples
pixelData = np.array(image)
height, width, channel = pixelData.shape

pixelMatrix = [[tuple(map(int, pixelData[y][x])) for x in range(width)] for y in range(height)]

# Convert RGB value into average brightness levels
brightnessMatrix = [[round(sum(pixelMatrix[y][x]) / len(pixelMatrix[y][x])) for x in range(width)] for y in range(height)]

# Convert brightness numbers to ASCII characters
symbols = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

asciiArt = []
for row in brightnessMatrix:
    asciiRow = [(symbols[(round((pixelBrightness / 255) * 100) // 5) - 1]) for pixelBrightness in row]
    asciiArt.append("".join(asciiRow))

# Output ascii image
outputName = "asciiImage.txt"
with open(outputName, "w") as f:
    for row in asciiArt:
        f.write(row + "\n")

print(f"Output written to {outputName}.")
