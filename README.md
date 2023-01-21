# PDF to Audio Converter

This project is a simple script that converts a PDF file to an audio file (MP3).

## Requirements

- Python 3
- PyPDF2
- gTTS

## Installation

1. Install Python 3 if it is not already installed on your system.
2. Install the required libraries by running the following command:

```pip install pypdf2 gtts```

## Usage

1. Place the script and the PDF file you want to convert in the same directory.
2. Open a terminal and navigate to the directory containing the script and the PDF file.
3. Run the script with the following command:

```python pdf_to_audio.py```

4. The script will generate an MP3 file named `output.mp3` in the same directory as the script and the PDF file.

## Notes

- The script currently only supports converting the entire PDF file to an audio file.
- The script uses the default voice of the gTTS library, which can be changed by passing a `lang` parameter to the gTTS constructor.
- The script uses the default filename 'output.mp3' for the generated audio file. It could be changed in script by replacing the 'audio.save("output.mp3")' line with 'audio.save("your_file_name.mp3")'
