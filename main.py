import PyPDF2
import re


def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file, strict=False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

        return pdf_text


def write_text_to_file(text, output_file):
    with open(output_file, 'w') as file:
        for page_text in text:
            # Split the page text using regex pattern
            split_message = re.split(r'\s+|[,;?!.-]\s*', page_text.lower())
            for word in split_message:
                file.write(word + '\n')


if __name__ == '__main__':
    print("Provide a pdf file")
    input_file = input("Input pdf file: ")
    converted_text = extract_text_from_pdf(input_file)
    output_file = 'extracted_text.txt'
    write_text_to_file(converted_text, output_file)
    # for text in converted_text:
    #     split_message = re.split(r'\s+|[,;?!.-]\s*', text.lower())
