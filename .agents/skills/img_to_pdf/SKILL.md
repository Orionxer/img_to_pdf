---
name: img_to_pdf
description: Use this skill when the user wants to convert image files (jpg, png, etc.) to PDF documents, or convert PDF pages to JPG images. It provides Python scripts for both directions and can demonstrate usage by setting up an example directory.
---

# Image/PDF Conversion Skill

## Description
This skill supports:
- Convert image files (e.g., JPG, PNG) to a PDF.
- Convert PDF to JPG:
  - single-page PDF -> one JPG (`xxx.jpg`)
  - multi-page PDF -> multiple JPGs (`xxx_001.jpg`, `xxx_002.jpg`, ...)

## Instructions

### 1. Image -> PDF
When the user requests to convert an image to PDF:
1.  Use the project virtual environment at `./.venv`. If it does not exist, create it and install dependencies with:
    ```bash
    python3 -m venv .venv
    ./.venv/bin/pip install pillow
    ```
2.  Locate the script `img_to_pdf.py` (either in the workspace or within this skill's `scripts` folder).
3.  Run the script with the input image and desired output PDF path:
    ```bash
    ./.venv/bin/python img_to_pdf.py <input_image_path> <output_pdf_path>
    ```

### 2. PDF -> JPG
When the user requests to convert a PDF to JPG:
1.  Use the project virtual environment at `./.venv`, and ensure it has `pypdfium2` and `Pillow`:
    ```bash
    python3 -m venv .venv
    ./.venv/bin/pip install pypdfium2 pillow
    ```
2.  Locate `pdf_to_jpg.py` in this skill's `scripts` folder.
3.  Run:
    ```bash
    ./.venv/bin/python .agents/skills/img_to_pdf/scripts/pdf_to_jpg.py <input_pdf_path> <output_dir> --dpi 200 --quality 95
    ```
4.  Output naming behavior (default base name is source PDF file name):
    - source `xxx.pdf` (single-page): `xxx.jpg`
    - source `xxx.pdf` (multi-page): `xxx_001.jpg`, `xxx_002.jpg`, ...
5.  Optional custom base name:
    ```bash
    ./.venv/bin/python .agents/skills/img_to_pdf/scripts/pdf_to_jpg.py <input_pdf_path> <output_dir> --name my_output
    ```
    - single-page: `my_output.jpg`
    - multi-page: `my_output_001.jpg`, `my_output_002.jpg`, ...

### 3. Usage Demonstration (Example)
If the user asks for a complete example:
1.  Create a new directory named `skills_example` in the project root.
2.  Copy the following files into `skills_example/`:
    -   `test.jpg` (from this skill's `assets/` folder)
    -   `img_to_pdf.py` (from this skill's `scripts/` folder)
    -   `pdf_to_jpg.py` (from this skill's `scripts/` folder)
3.  Run an end-to-end demo:
    ```bash
    cd skills_example
    ../.venv/bin/python img_to_pdf.py test.jpg test.pdf
    ../.venv/bin/python pdf_to_jpg.py test.pdf pages --dpi 200 --quality 95
    ```
