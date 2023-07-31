# ReportLab-auto-insertion
a Python script that uses the ReportLab library to create a PDF document containing images from a specified directory. 
"""
Script: create_pdf_with_images.py
Description: Generate a landscape-oriented PDF document containing images from a specified directory.
Author: [Ebrahim Ramadan]
GitHub: [[GitHub](https://github.com/Ebrahim-Ramadan)]

Libraries:
- reportlab: A library for creating PDFs and graphics.

Functions:
1. create_pdf_with_images(images_directory, output_pdf_path)
    Description: Generates a PDF document containing images from the specified directory.
    Parameters:
        - images_directory (str): The path to the directory containing the image files.
        - output_pdf_path (str): The path where the generated PDF will be saved.
    Returns:
        None

2. page_number_footer(canvas, doc)
    Description: Adds the page number to the bottom of each page in the PDF.
    Parameters:
        - canvas: The canvas object provided by ReportLab for drawing.
        - doc: The document object to which the page number is added.
    Returns:
        None

Usage:
- To use this script, you need to have ReportLab installed in your Python environment.
  You can install it using `pip install reportlab`.

- Call the `create_pdf_with_images` function with the appropriate parameters to generate the PDF.
  Pass the path to the directory containing images in `images_directory` and the output PDF path in `output_pdf_path`.

- The PDF will be created with landscape orientation, and the images will be resized to fit the page.
  The default image size for each page is 9x6.3 inches.

- The `page_number_footer` function adds page numbers to the bottom of each page.
  The page numbers will be displayed as "Page X", where X is the page number.

PLUS FEATURE:
- The code includes an adjustable layout size for the pages.
  To adjust the layout size, uncomment the following lines inside the `page_number_footer` function:
    ```
    # Adjust the coordinates to position the text at the bottom-right corner
    # text_width = canvas.stringWidth(text, "Helvetica", 9)
    # canvas.drawRightString(doc.width - text_width - 10, 0.75 * inch, text)
    ```
  This will position the page number text at the bottom-right corner, making it appear closer to the corner of the page.

Note:
- Make sure the `images_directory` contains only image files with extensions `.png`, `.jpg`, or `.jpeg`.
- Ensure that the `output_pdf_path` specifies a valid path and filename for the generated PDF.

"""

# (Rest of the code is unchanged)

