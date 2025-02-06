import pyttsx3
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

BOT_TOKEN = "7938656231:AAHCtMQehCPWicrqaba8rYDav1IFAPZkJVs"
BOT_ID = "Aliiirosj_bot"
ALLOWED = "ALL" # or ["Aliireza8617'']
# تنظیمات تبدیل متن به گفتار
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # سرعت گفتار
engine.setProperty('volume', 1.0)  # حجم صدا (۰ تا ۱)

# ایجاد یک ربات چت
chatbot = ChatBot('SpeakingBot')

# آموزش ربات با داده‌های پیش‌فرض
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")  # می‌توانید از دیتاست فارسی نیز استفاده کنید

# تابع برای صحبت کردن
def speak(text):
    print(f"ربات: {text}")
    engine.say(text)
    engine.runAndWait()

# شروع چت با ربات
print("ربات چت فعال شد! برای خروج عبارت 'exit' را وارد کنید.")
while True:
    user_input = input("شما: ")
    if user_input.lower() == 'exit':
        speak("خداحافظ! به امید دیدار.")
        break
    response = chatbot.get_response(user_input)
    speak(str(response))