# Phân loại Cảm xúc Tiếng Việt – Vietnamese Sentiment Analysis Web App  
Dựa trên PhoBERT (wonrax/phobert-base-vietnamese-sentiment)

Một ứng dụng web đơn giản, đẹp mắt, chạy cục bộ giúp phân loại cảm xúc tiếng Việt thành 3 nhãn:  
**Tích cực – Tiêu cực – Trung tính**  
với độ chính xác rất cao (~95%) và hỗ trợ cả văn bản thiếu dấu, teencode.

## Tính năng nổi bật
- Phân loại cảm xúc tiếng Việt siêu chính xác nhờ PhoBERT fine-tuned  
- Hỗ trợ tiếng Việt thiếu dấu, viết tắt: “Rat vui hom nay”, “dở tệ”, “bt mà”…  
- Giao diện web xinh xắn, responsive (Flask + HTML/CSS/JS)  
- Lưu lịch sử phân loại bằng SQLite  
- Hiển thị độ tin cậy (confidence score)  
- Không cần GPU, chạy mượt trên laptop thường  

## Yêu cầu hệ thống
- Python 3.11 (khuyên dùng 3.11)

## Cài đặt & chạy

```bash
# 1. Clone dự án
git clone https://github.com/lamkbvn/huggingface-wonrax-phobert-base-vietnamese-sentiment-web.git
cd huggingface-wonrax-phobert-base-vietnamese-sentiment-web

# 2. Tạo virtual environment (khuyến khích)
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# 3. Cài đặt thư viện
pip install -r requirements.txt

# 4. Chạy ứng dụng
python app.py
```

Mở trình duyệt và truy cập: http://127.0.0.1:5000

Ứng dụng sẽ tự động tải model PhoBERT lần đầu (khoảng 500MB), lần sau chạy rất nhanh!

## Cấu trúc thư mục
```
├── app.py                  → File chính chạy Flask
├── requirements.txt        → Danh sách thư viện
├── sentiment_model.py      → Xử lý PhoBERT + underthesea
├── database.db             → SQLite tự tạo khi chạy lần đầu
├── templates/
│   └── index.html          → Giao diện chính
├── static/
│   ├── css/style.css
│   └── js/main.js
└── history.db              → Lịch sử phân loại (SQLite)
```


## Tác giả
- Mai  Phúc Lâm
- Email: lamkbvn@gmail.com  
- GitHub: https://github.com/lamkbvn

## Giấy phép
MIT License – bạn được tự do sử dụng, chỉnh sửa, thương mại hóa.

---
