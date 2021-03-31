import PyPDF2
from wordcloud import WordCloud
from utility import create_hsh_table,separate_dict

pdffile="pdfs/pnp.pdf"
fileobject = open(pdffile,'rb')

pdfReader = PyPDF2.PdfFileReader(fileobject)  #can be parsed to get pages.

n_pages = pdfReader.numPages
i=0
wordtable = dict()

while i<n_pages:
    page = pdfReader.getPage(i)
    i+=1
    create_hsh_table(page.extractText(),wordtable)

#separate_dict is used to separate the frequency table into 5 ranges, i.e. 1-45, 6-10, 11-15, 16-20, 20>
dict_list=separate_dict(wordtable)

wc=[]
for j in range(5):
    wc.append(WordCloud()) 
for k in range(5):
    if len(dict_list[k])>0:
        wc[k].generate_from_frequencies(frequencies=dict_list[k])
        wc[k].to_file("img/"+str(k)+".png")
    else:
        print("no words in this range")

'''plt.figure()
plt.imshow(wc,interpolation="bilinear")
plt.axis("off")
plt.show()'''