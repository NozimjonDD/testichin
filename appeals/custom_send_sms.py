from api.v1.admin.user.services.send_sms import send_sms


def custom_send_sms(recipient: str, key: str):
    text = f"Ваша заявка принята. Ключевые слова для проверки результата заявки: {key}\n" \
           f"Sizning murojaatingiz qabul qilindi. Murojaat natijasini tekshirish uchun kalit so'z: {key}"
    return send_sms(recipient, text)
