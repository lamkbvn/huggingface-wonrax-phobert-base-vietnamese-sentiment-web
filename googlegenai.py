from google import  genai

client = genai.Client(api_key="AIzaSyBpbcHviNnIUyDR7-3zULlDdgomXRu5Ggk")

chat_session = client.chats.create(model="gemini-2.5-flash")

def correct_spelling(input) :
    BASE_PROMPT = f"""
    {input}

    Bạn sẽ thực hiện công việc viết lại câu cho đúng chính tả cho câu trên.

    Quy tắc:
    - Chỉ trả về kết  quả
    - Không thêm giải thích
    - Nếu người dùng gõ linh tinh (không phải câu tiếng Việt hợp lệ) → trả về chính xác y chang input, không sửa.
    """
    response = chat_session.send_message(BASE_PROMPT)
    text = response.text
    return text
