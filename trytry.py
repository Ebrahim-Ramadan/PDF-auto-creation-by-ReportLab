# from reportlab.lib.pagesizes import letter, portrait
# from reportlab.platypus import SimpleDocTemplate, Image, PageTemplate, Frame
# from reportlab.lib import colors

# def insert_images(images_folder, output_file):
#     # Set the page size to portrait orientation
#     page_width, page_height = portrait(letter)

#     doc = SimpleDocTemplate(output_file, pagesize=(page_width, page_height))

#     # List all the image files in the folder
#     image_files = [os.path.join(images_folder, filename) for filename in os.listdir(
#         images_folder) if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

#     # Create a list to store the image objects
#     elements = []

#     # Get the frame size for the page
#     frame_width = page_width - 2 * inch
#     frame_height = page_height - 2 * inch
#     frame = Frame(inch, inch, frame_width, frame_height)

#     for image_file in image_files:
#         # Adjust image size to fit the frame
#         image = Image(image_file, width=frame_width, height=frame_height)
#         elements.append(image)

#     # Add a PageTemplate for adding page numbers
#     template = PageTemplate(id='test', frames=frame, onPage=page_number_footer)
#     doc.addPageTemplates([template])

#     # Build the document
#     doc.build(elements)

# def page_number_footer(canvas, doc):
#     # This function adds the page number to the bottom-right of each page.
#     page_num = canvas.getPageNumber()
#     text = "Page %s" % page_num
#     canvas.setFont("Helvetica", 9)
#     canvas.setFillColor(colors.gray)
#     text_width = canvas.stringWidth(text, "Helvetica", 9)
#     canvas.drawRightString(doc.width - inch, inch, text)

# if __name__ == "__main__":
#     images_folder = "picturesDIR"
#     output_file = "output.pdf"

#     insert_images(images_folder, output_file)


from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Image, PageTemplate, Frame, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def create_pdf_with_images(images_directory, output_pdf_path):
    # List all the image file names in the directory
    import os
    image_files = [f for f in os.listdir(
        images_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Landscape page size (11x8.5 inches)
    page_width, page_height = landscape(letter)

    # Create the PDF document
    doc = SimpleDocTemplate(
        output_pdf_path, pagesize=(page_width, page_height))

    # Create a list to hold the flowables (elements) of the PDF
    elements = []

    # Loop through each image and add it to the PDF
    for image_file in image_files:
        image_path = os.path.join(images_directory, image_file)
        # Adjust the image size to fit the page, e.g., 9x6.3 inches
        image = Image(image_path, width=9*inch, height=6.3*inch)
        elements.append(image)

    # Add a PageTemplate for adding page numbers
    frame = Frame(0, 0, page_width, page_height, id='normal')
    template = PageTemplate(id='test', frames=frame, onPage=page_number_footer)
    doc.addPageTemplates([template])

    # Build the PDF document
    doc.build(elements)


def page_number_footer(canvas, doc):
    # This function adds the page number to the bottom of each page.
    page_num = canvas.getPageNumber()
    text = "Page %s" % page_num
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.gray)
    canvas.drawRightString(10 * inch, 0.75 * inch, text)

    # PLUS FEATURE
    # Adjust the coordinates to position the text at the bottom-right corner
    # text_width = canvas.stringWidth(text, "Helvetica", 9)
    # canvas.drawRightString(doc.width - text_width - 10, 0.75 * inch, text)


if __name__ == "__main__":
    images_directory = "picturesDIR"
    output_pdf_path = "output.pdf"

    create_pdf_with_images(images_directory, output_pdf_path)
