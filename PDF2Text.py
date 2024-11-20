import sys
import PyPDF2
from tkinter import filedialog,messagebox

def pdf_to_text(pdf_path, output_txt):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PdfReader object instead of PdfFileReader
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty string to store the text
        text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # Write the extracted text to a text file
    with open(output_txt, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

if __name__ == "__main__":
    pdf_path = filedialog.askopenfilename(filetypes=(["filetype:",".pdf"],["All Files:","*.*"]))

    if pdf_path == "":
        messagebox.showerror("No File","You have not selected any PDF")
        sys.exit()
    
    output_txt = filedialog.asksaveasfilename()

    if output_txt == "":
        messagebox.showwarning("No Output File Selected","You have not selected where to save Extracted Text\n\n Automatically saved in: output.txt")
        output_txt = "output.txt"

    pdf_to_text(pdf_path, output_txt)

    messagebox.showinfo("Successfull","PDF converted to text successfully!")