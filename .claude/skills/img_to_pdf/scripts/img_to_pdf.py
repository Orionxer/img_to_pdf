import sys
import os
from PIL import Image

def convert_img_to_pdf(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    try:
        # Open the image file
        image = Image.open(input_path)
        
        # Ensure image is in RGB mode for PDF compatibility
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Save as PDF
        image.save(output_path, "PDF", resolution=100.0)
        print(f"Successfully converted: {input_path} -> {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python img_to_pdf.py <input_file> <output_file>")
    else:
        convert_img_to_pdf(sys.argv[1], sys.argv[2])
