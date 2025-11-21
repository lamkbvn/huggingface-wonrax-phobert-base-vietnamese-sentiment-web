import torch
from transformers import RobertaForSequenceClassification, AutoTokenizer
from underthesea import word_tokenize

def predict_sentiment(sentence) :

    model = RobertaForSequenceClassification.from_pretrained("wonrax/phobert-base-vietnamese-sentiment")

    tokenizer = AutoTokenizer.from_pretrained("wonrax/phobert-base-vietnamese-sentiment", use_fast=False)

    segmented_text = word_tokenize(sentence, format="text")

    input_ids = torch.tensor([tokenizer.encode(segmented_text)])

    with torch.no_grad():
        out = model(input_ids)
        probs = out.logits.softmax(dim=-1)
        pred = torch.argmax(probs , dim= -1).item()
        print(f"{probs.tolist()}")
        labels = ["tiêu cực ", " tích cực", "bình thường"]
        return labels[pred]

sentence = "đẹp nhưng phù hợp "
result =  predict_sentiment(sentence)
print(f"{result}")


