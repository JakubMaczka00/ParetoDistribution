import matplotlib.pyplot as plt
import powerlaw as powerlaw
import PyPDF2
import collections

class PDFConverter:
    
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
    
    def convert_to_text(self, text_path):
        with open(self.pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            with open(text_path, 'w', encoding='utf-8') as text_file:
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text_file.write(page.extract_text())
                    
class PowerLawFitter:
    
    def __init__(self, filename):
        self.data = self.load_data(filename)
        print(self.data)
        self.fit = powerlaw.Fit(self.data)
        
    def load_data(self, filename):
        data = []
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split() 
                data.extend(words)
        word_counts = collections.Counter(data)
        top_5 = word_counts.most_common(5)
        print(top_5)
        frequencies = list(word_counts.values())
        return frequencies


        
    def plot_pdf(self):
        figure = self.fit.plot_pdf(color='blue', linewidth=2)
        self.fit.plot_pdf(color='red', linestyle='--', ax=figure)
        plt.xlabel('Value')
        plt.ylabel('Probability Density')
        plt.title('Power Law Distribution')
        plt.show()
        
    def print_parameters(self):
        print(self.fit.alpha)
        print(self.fit.xmin)

#pdf_converter = PDFConverter('./pdfFiles/Kryptografia.pdf')
#pdf_converter.convert_to_text('./txtFiles/Kryptografia.txt')

filename = './txtFiles/Kryptografia.txt'

fitter = PowerLawFitter(filename)
fitter.plot_pdf()
fitter.print_parameters()