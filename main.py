import pypdf,pyttsx3
# open your pdf for reading in binary
pdfreader = pypdf.PdfReader(open('book.pdf', 'rb'))

# init function to get an engine instance for speech synthesis 
speaker = pyttsx3.init()

finText = ""
#loop through pdf pages
for page_num in range(len(pdfreader.pages)):
    # extract text
    text = pdfreader.pages[page_num].extract_text()
    cleanText = text.strip().replace('\n',' ')
    finText += cleanText
# save text as .mp3 file
speaker.save_to_file(finText, 'story.mp3')
#process voice command
speaker.runAndWait()

speaker.stop()
