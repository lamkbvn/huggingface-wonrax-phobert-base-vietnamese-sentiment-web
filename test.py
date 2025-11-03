import torch
from transformers import RobertaForSequenceClassification, AutoTokenizer

model = RobertaForSequenceClassification.from_pretrained("wonrax/phobert-base-vietnamese-sentiment")

tokenizer = AutoTokenizer.from_pretrained("wonrax/phobert-base-vietnamese-sentiment", use_fast=False)

# Just like PhoBERT: INPUT TEXT MUST BE ALREADY WORD-SEGMENTED!
sentence = ' vui hom nay '

input_ids = torch.tensor([tokenizer.encode(sentence)])

with torch.no_grad():
    out = model(input_ids)
    probs = out.logits.softmax(dim=-1)
    labels = [ "tiêu cực " ,  " tích cực" ,  "bình thường"]
    pred = torch.argmax(probs , dim= -1).item()
    print(f"label :  {labels[pred]}")
