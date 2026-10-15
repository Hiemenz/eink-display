from PIL import Image

# Open the image file
img = Image.open('images/image3.webp')

# Convert to grayscale (for black and white displays)
img = img.convert('L')

# Or, for a 3-color scheme, enhance contrast and convert
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(5)  # Adjust contrast
img = img.convert('1')  # Convert to black and white

# Resize image to match your eInk display resolution
img = img.resize((800, 480))  # Adjust to your display's resolution

# Save the processed image
img.save('processed_image2.bmp')