#from cgitb import text

# Create your models here.
import torch
import transformers
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config
from bs4 import BeautifulSoup
import requests

#class Summar:
model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer=T5Tokenizer.from_pretrained('t5-small')
device=torch.device('cpu')

def summarizer(url):
    text=getTextFromURL(url)
    preprocessed_text=text.strip().replace('\n',' ')
    t5_input_text="summarize: "+preprocessed_text
    tokenized_text=tokenizer.encode(t5_input_text,return_tensors='pt',max_length=1024).to(device)
    summary_ids=model.generate(tokenized_text,min_length=30,max_length=600)
    summary=tokenizer.decode(summary_ids[0],skip_special_tokens=True)
    return summary
def getTextFromURL(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    texts = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return texts