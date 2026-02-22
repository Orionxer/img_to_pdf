---
name: img_to_pdf
description: Use this skill when the user wants to convert image files (jpg, png, etc.) to PDF documents. It provides a Python script to perform the conversion. It can also demonstrate the usage by setting up an example directory.
---

# Image to PDF Conversion Skill

## Description
This skill allows users to convert image files (e.g., JPG, PNG) into PDF documents using a Python script.

## Instructions

### 1. Direct Conversion
When the user requests to convert an image to PDF:
1.  Ensure a Python environment with `Pillow` installed is available.
2.  Locate the script `img_to_pdf.py` (either in the workspace or within this skill's `scripts` folder).
3.  Run the script with the input image and desired output PDF path:
    ```bash
    python img_to_pdf.py <input_image_path> <output_pdf_path>
    ```

### 2. Usage Demonstration (Example)
If the user asks for an example or how to use this skill:
1.  Create a new directory named `skills_example` in the project root.
2.  Copy the following files into `skills_example/`:
    -   `test.jpg` (from the project root or source)
    -   `img_to_pdf.py` (from the project root or this skill's `scripts/` folder)
3.  Execute the conversion within the `skills_example` directory:
    ```bash
    cd skills_example
    python img_to_pdf.py test.jpg test.pdf
    ```
