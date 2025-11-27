import torch
from transformers import RobertaForSequenceClassification, AutoTokenizer
from underthesea import word_tokenize

from googlegenai import correct_spelling

model = RobertaForSequenceClassification.from_pretrained("wonrax/phobert-base-vietnamese-sentiment")

tokenizer = AutoTokenizer.from_pretrained("wonrax/phobert-base-vietnamese-sentiment", use_fast=False)

def predict_sentiment(sentence) :

    sentence_correct_spelling =  correct_spelling(sentence)

    segmented_text = word_tokenize(sentence_correct_spelling, format="text")
    print(segmented_text)
    input_ids = torch.tensor([tokenizer.encode(segmented_text)])

    with torch.no_grad():
        out = model(input_ids)
        probs = out.logits.softmax(dim=-1)
        pred = torch.argmax(probs , dim= -1).item()
        labels = ["tiêu cực ", " tích cực", "bình thường"]
        return labels[pred]

sentence = "hom nay toi met qua "
result =  predict_sentiment(sentence)
print(f"{result}")


