"""
Mualliflik huquqini buzmagan holda kanallarda tarqatishingiz mumkin!
Loyiha muallifi: Arslonbek Xushboqov
Tarqatildi: @Api_Kod kanalida

Demo: @GoTarjimonBot
"""

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


default_lang = "en"

start_message_text = """
Assalomu alaykum {} \U0001F60E Men GoTarjimonBot ya'ni "Google Tarjimon Botman \ud83e\udd16

Menga har qanday soʻzni yuboring men uni ingliz tiliga tarjima qilib beraman boshqa tillarni tanlash uchun /language buyrugini yuboring.

**Mavjud buyruqlar:**
/developer - Bot dasturchisi haqida
/help - Botdan foydalanish boyicha qollanma
/language - Oʻzingiz uchun afzal tilni tanlang

Agar sizda shu bot yoki boshqa botlar' haqida fikringiz boʻlsa dasturchi__ - @Saidjon_okenn ga murojaat qilishingiz mumkin!

Zavqlaning! ☺"""

start_message_reply_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "➕ Meni guruhga qoshing ➕",  url="http://t.me/tarjimon_x1_robot?startgroup=tr")
        ],
        [
            InlineKeyboardButton(  
                        "🔍 Inline izlash",
                        switch_inline_query_current_chat=" "
                    ),
            InlineKeyboardButton(
                "👨‍💻 Dasturchi",  url="https://t.me/Saidjon_okenn"),
        ],
        [
            InlineKeyboardButton(
                "🆘 Yordam",  callback_data="help"),
            InlineKeyboardButton(
                "Xizmatlar 💚",  callback_data=b"Credits")
        ],
        [
            InlineKeyboardButton(
                "📣 Kanal",  url="https://t.me/hacker_vlogss"),
            InlineKeyboardButton(
                "Guruh 👥",  url="https://t.me/hayotiy_damlar"),
        ]
    ]
)

help_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🔙 Orqaga", callback_data="back")],
            ]
        )

credits = """Dasturchi 🧑‍💻
 • @Saidjon_okenn
 • Sizga mukammal tarzda bot yaratib berishimiz mumkin
 • Iltimos lichkaga bot kodini sorab yozmang!

Kanal 💡
 • @hacker_vlogss"""

help_text = """
**Tarjimon Bot**

Tarjimon "G + Tarjimon" so'zi bo'lib, "Google Tarjimon" ma'nosini anglatadi.  Matnni (emojilar bilan) dunyoning boshqa tillaridan koʻplab tillarga tarjima qilishga yordam beradigan bot.

 Tarjimon Bot turli xil tillarni aniqlay oladi, chunki u Google Translate API yordamida ishlaydi.

 Tarjimon Bot-dan shaxsiy suhbatida foydalanishingiz mumkin.  Ammo GoTarjimon Bot Telegram Guruh & Kanal uchun mavjud emas.
 
**Qanday**
Tarjimon Bot-ga nusxa ko'chirilgan matnni yoki boshqa tilga yo'naltirilgan xabarni yuborish kifoya, shunda siz o'zingiz xohlagan tilda tarjimani olasiz.  Qaysi til mavjudligini bilish uchun /language buyrugʻini yuborish kerak.

****Boshqa Yordam****

**Guruhlar**
/tr (til kodi) reply xabarni tarjima qilish  reply orqali

**Asosiy tilni o'zgartirmasdan shaxsiy suhbatda tarjima qiling**
/tr (til kodi) (xabar)

**Inline rejimida tarjima qiling**
@tarjimon_x1_robot (til kodi) (xabar)

---
Muammo bolsa? @Saidjon_okenn ga murojaat qiling

Python dasturlash tilida yaratildi 💚
"""

developer_text = """
Yusufxojayev Saidahror

Qiziqishi:  Dasturchilik ;
Yoshi:  18-yosh ;
Yonalishi:  Html & Css & Js & Python & php ;
Aloqa:  +998936045636 ;
Email:  saidjonbloger@gmail.com ;
Yashash Joyi:  Toshkent shahri Sergeli tumani ;
"""

language_text = """
**Tillar**

__Tarjima qilmoqchi bo'lgan tilni tanlang.__

•/lang (til kodi) 

Masalan: ```/lang uz``` 

Til kodlari ro'yxati: https://cloud.google.com/translate/docs/languages


"""

error_group_no_reply = """Tarjima qilish uchun xabarga javob bering"""

error_ocr_no_reply = """matnni olish uchun fotosuratga javob bering"""

lang_saved_message = """{} sizning asosiy tilingiz sifatida o'rnatildi."""

ocr_message_text = """```rasmdagi matn:``` \n\n {}"""

translate_string_one = """**\ud83c\udf10 Tarjima**:\n\n```{}```\n\n**🔍 Aniqlangan til:** {} \n\n **Tarjima qilingan**: {}"""

translate_string_two = """**\ud83c\udf10 Tarjima**:\n\n```{}```\n\n**🔍 Aniqlangan til:** {}"""

inline_text_string_one = """So'z tarjima qilindi {} dan {} ga"""
