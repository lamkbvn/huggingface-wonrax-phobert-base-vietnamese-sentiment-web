import torch
from transformers import RobertaForSequenceClassification, AutoTokenizer
from underthesea import word_tokenize

# Load model và tokenizer
model = RobertaForSequenceClassification.from_pretrained(
    "wonrax/phobert-base-vietnamese-sentiment"
)
tokenizer = AutoTokenizer.from_pretrained(
    "wonrax/phobert-base-vietnamese-sentiment", use_fast=False
)

sentences = ["Hôm nay tôi rất vui "]

for sentence in sentences :

    # Tách từ theo chuẩn PhoBERT
    segmented = word_tokenize(sentence, format="text")

    # Mã hóa bằng tokenizer
    encoded = tokenizer.encode(segmented)

    print(tokenizer.convert_ids_to_tokens(encoded))

    # Tạo tensor input
    input_ids = torch.tensor([encoded])

    # ===== PREDICT =====
    with torch.no_grad():
        logits = model(input_ids).logits
        probs = logits.softmax(dim=-1).tolist()[0]


    # ===== MAP NHÃN =====
    label_map = {
        0: "NEGATIVE",
        1: "POSITIVE",
        2: "NEUTRAL"
    }

    predicted_label = label_map[probs.index(max(probs))]

    # ===== FORMAT OUTPUT =====
    output = {
        "text": sentence,
        "sentiment": predicted_label,
        "percent" : probs
    }

    print(output)
