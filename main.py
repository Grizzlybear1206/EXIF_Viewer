from PIL import Image # Extract EXIF data from loaded image
from PIL import ExifTags # Convert EXIF data to human readable words
from tkinter import filedialog # tkinter's built in file explorer
import pyperclip # used to copy EXIF Data to clipboard

AcceptedFileTypes = [
    ("Image Files", ".png .jpg")
]

Tags = ExifTags.TAGS

### KNOWN ERROR: File explorer hidden behind terminal when EXIF Viewer is rerun

def ExtractExif():
    SelectedImage = filedialog.askopenfilename(filetypes=AcceptedFileTypes, title="EXIF File Select")
    

    print(SelectedImage + "\n")

    LoadedImage = Image.open(SelectedImage)

    EXIFData = LoadedImage.getexif()

    EXIFString = ""

    for k, v in EXIFData.items():
        print(Tags[k], v)
        EXIFString += f'{Tags[k]}: {v}'

    command = input("\nType \"c\" to copy EXIF data to clipboard\nType \"r\" to select another file\nType \"cr\" to do both\nPress ENTER to exit EXIF Viewer\n>: ")

    if command.lower() == "c":
        pyperclip.copy(EXIFString)

    elif command.lower() == "r":
        ExtractExif()

    elif command.lower() == "cr":
        pyperclip.copy(EXIFString)
        ExtractExif()

ExtractExif()
