import os
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
from PIL import Image
from tkinter import Tk, filedialog, messagebox

class PDFConverter:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def pdf_to_image(self):
        images = convert_from_path(self.pdf_path)
        return images

    def crop_image(self, image_path, left, top, right, bottom):
        image = Image.open(image_path)
        cropped_image = image.crop((left, top, right, bottom))
        return cropped_image

if __name__ == "__main__":
    Tk().withdraw()  # Hide the main tkinter window

    # Ask the user to select the PDF file
    print("Please select the PDF file.")
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

    if not file_path:
        print("No file selected. Exiting...")
    else:
        pdf_converter = PDFConverter(file_path)
        images = pdf_converter.pdf_to_image()

        # Choose the page number (starting from 0) you want to crop
        page_number = 0

        # Define the coordinates for cropping (left, top, right, bottom)
        left, top, right, bottom = 100, 200, 400, 600

        image_path = f"page_{page_number}.png"
        images[page_number].save(image_path)

        cropped_image = pdf_converter.crop_image(image_path, left, top, right, bottom)

        # Save the cropped image with the same name as the PDF file and page number
        output_filename = os.path.splitext(os.path.basename(file_path))[0]
        output_filename = f"{output_filename}_page_{page_number}.png"
        cropped_image.save(output_filename)

        # Remove the temporary image file
        os.remove(image_path)

        # Ask the user if they want to open the cropped image
        choice = messagebox.askyesno("Image Saved", "Cropped image saved successfully. Do you want to open it now?")

        if choice:
            cropped_image.show()
