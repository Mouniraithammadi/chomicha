from google.cloud import vision
client = vision.ImageAnnotatorClient()
def detect_text(path):
    """Detects text in the file."""
    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")

    for text in texts:
        print(f'\n"{text.description}"')

        vertices = [
            f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
        ]

        print("bounds: {}".format(",".join(vertices)))

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )




import os
import PyPDF2
from pdf2image import convert_from_path

# Path to the PDF file
pdf_file_path = 'your_pdf_file.pdf'

# Create a folder to save extracted images
output_folder = 'output_images'
os.makedirs(output_folder, exist_ok=True)

# Open the PDF file
def extractText(pdf_file_path):
    pdf_file = open(pdf_file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Iterate through each page and extract images
    for page_number in range(pdf_reader.numPages):
        # Extract images from the current page
        images = convert_from_path(pdf_file_path, first_page=page_number + 1, last_page=page_number + 1)

        for i, image in enumerate(images):
            # Save each image to the output folder
            image.save(os.path.join(output_folder, f'page_{page_number + 1}_image_{i + 1}.jpg'), 'JPEG')

    # Close the PDF file
    pdf_file.close()








