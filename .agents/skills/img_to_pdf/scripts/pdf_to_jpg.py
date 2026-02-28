import argparse
import os
import sys

try:
    import pypdfium2 as pdfium
except ImportError:
    print(
        "Error: missing dependency pypdfium2/Pillow. "
        "Install with: pip install pypdfium2 pillow"
    )
    sys.exit(1)


def convert_pdf_to_jpg(input_pdf, output_dir, dpi=200, quality=95, base_name=None):
    if not os.path.exists(input_pdf):
        print(f"Error: {input_pdf} not found.")
        return 1

    os.makedirs(output_dir, exist_ok=True)
    if base_name is None:
        base_name = os.path.splitext(os.path.basename(input_pdf))[0]

    try:
        pdf = pdfium.PdfDocument(input_pdf)
    except Exception as exc:
        print(f"Error opening PDF: {exc}")
        return 1

    page_count = len(pdf)
    if page_count == 0:
        print("Error: PDF has no pages.")
        return 1

    scale = dpi / 72
    pad_width = max(3, len(str(page_count)))

    try:
        for idx in range(page_count):
            page = pdf[idx]
            bitmap = page.render(scale=scale)
            image = bitmap.to_pil().convert("RGB")

            if page_count == 1:
                filename = f"{base_name}.jpg"
            else:
                filename = f"{base_name}_{idx + 1:0{pad_width}d}.jpg"

            out_path = os.path.join(output_dir, filename)
            image.save(out_path, "JPEG", quality=quality, optimize=True)
            print(f"Saved: {out_path}")
    except Exception as exc:
        print(f"An error occurred while rendering/saving JPG: {exc}")
        return 1

    print(
        f"Done. Processed {page_count} page(s) from {input_pdf} -> {output_dir}"
    )
    return 0


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Convert PDF pages to JPG. "
            "Single-page output is <name>.jpg, multi-page output is <name>_001.jpg, <name>_002.jpg..."
        )
    )
    parser.add_argument("input_pdf", help="Path to source PDF file")
    parser.add_argument("output_dir", help="Directory for output JPG files")
    parser.add_argument("--dpi", type=int, default=200, help="Render DPI (default: 200)")
    parser.add_argument(
        "--quality", type=int, default=95, help="JPEG quality 1-100 (default: 95)"
    )
    parser.add_argument(
        "--name",
        default=None,
        help="Base output name (default: input PDF file name without extension)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.dpi < 1:
        print("Error: --dpi must be a positive integer.")
        sys.exit(1)
    if args.quality < 1 or args.quality > 100:
        print("Error: --quality must be between 1 and 100.")
        sys.exit(1)
    sys.exit(
        convert_pdf_to_jpg(
            args.input_pdf,
            args.output_dir,
            dpi=args.dpi,
            quality=args.quality,
            base_name=args.name,
        )
    )
