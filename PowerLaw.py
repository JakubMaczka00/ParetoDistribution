import matplotlib.pyplot as plt
import powerlaw as powerlaw
import PyPDF2
import collections

path_pdf = './pdfFiles/'
path_txt = './txtFiles/'
pdflist=["Kryptografia","elektromobilnosc",
         "elektromobilnosc2",
         "elektromobilnosc3",
         "Development of Electromobility in European Union Countries under COVID-19 Conditions",
         "European government electromobility plans",
         "The Development of Electromobility in the European Union"]

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
        self.filename = filename
        self.name_of_file= filename.split('/')[-1]
        
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
        plt.title('Power Law Distribution of file: '+self.name_of_file)
        plt.show()
        
    def print_parameters(self):
        print(self.fit.alpha)
        print(self.fit.xmin)

for item in pdflist:
    pdf_converter = PDFConverter(path_pdf+item+'.pdf')
    pdf_converter.convert_to_text(path_txt+item+'.txt')
    filename = path_txt+item+'.txt'
    fitter = PowerLawFitter(filename)
    fitter.print_parameters()
    fitter.plot_pdf()

#TODO: Znajdź artykuły z 3 różnych dziedzin nauki, które zawierają dane, które można opisać rozkładem mocy. i stwórz ładną prezentacje z wykresem i opisem tych rzeczy co wypluł