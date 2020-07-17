import pyttsx3
import PyPDF2


pdfReader = PyPDF2.PdfFileReader(r"Z:\PDF_to_audiopdf\PDF-to-AudioBook\Automate the Boring Stuff with Python_ 2nd Edition - Al Sweigart.pdf")
pages = pdfReader.numPages

for num in range(1,pages):
	page = pdfReader.getPage(num)
	text = page.extractText()
	player = pyttsx3.init()
	#player.say(text)
	print(text)
	player.runAndWait()