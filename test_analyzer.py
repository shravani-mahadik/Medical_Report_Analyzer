from utils.image_reader import read_image
from utils.analyzer import extract_parameters

print("Program Started")

# Read text from image
text = read_image("uploads/blood_report.jpg")

print("\n========== OCR TEXT ==========\n")
print(text)

# Extract parameters
parameters = extract_parameters(text)

print("\n========== EXTRACTED PARAMETERS ==========\n")

for key, value in parameters.items():
    print(f"{key:20} : {value}")