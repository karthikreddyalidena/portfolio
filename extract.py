import sys
import PyPDF2

def extract_text(pdf_path, out_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        with open(out_path, 'w', encoding='utf-8') as out_file:
            out_file.write(text)

if __name__ == "__main__":
    extract_text(sys.argv[1], sys.argv[2])
