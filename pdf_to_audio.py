# Step 1: Install the necessary libraries
!pip
install
pypdf2
gtts

# Step 2: Load the PDF file
import os
import PyPDF2

# Assume the PDF file is in the current directory and is named "document.pdf"
pdf_path = "document.pdf"

# Open the PDF file in read-binary mode
file = open(pdf_path, "rb")

# Create a PDF object
pdf = PyPDF2.PdfReader(file)

# Step 3: Extract the text from the PDF
text = ""

# Iterate over the pages of the PDF
for i in range(len(pdf.pages)):
    # Get the current page
    page = pdf.pages[i]

    # Extract the text from the page
    text += page.extract_text()

# Close the file
file.close()

# Step 4: Generate the audio
from gtts import gTTS

# Generate the audio
audio = gTTS(text)

# Step 5: Save the audio
# Assume the audio file should be saved in the current directory and be named "output.mp3"
audio.save("output.mp3")
