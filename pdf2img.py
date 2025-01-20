from pdf2image import convert_from_path

def convert_pdf_to_jpg(pdf_file, output_folder, dpi=200):
    # Convert PDF to a list of images
    images = convert_from_path(pdf_file, dpi=dpi, first_page=1, last_page=1)

    # Save images to JPG
    for i, image in enumerate(images):
        image_path = f"{output_folder}/page_{i + 1}.jpg"
        image.save(image_path, 'JPEG')
        print(f"Saved image to {image_path}")

# Usage example
convert_pdf_to_jpg('/Users/krislwin/Documents/GitHub/Kris-s-Portfolio/assets/img/portfolio/fullsize/Daitaku.pdf', '/Users/krislwin/Documents/GitHub/Kris-s-Portfolio/assets/img/portfolio/fullsize/')
