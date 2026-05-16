import streamlit as st
from google import genai
from google.genai import types
import os

# 1. إعدادات الصفحة والمظهر العام للموقع
st.set_page_config(page_title="Asad Al-Dhalam ED.", page_icon="👁️", layout="centered")

# مفتاح الـ API الخاص بك (شغال وجاهز)
API_KEY = "AIzaSyCjqipSFLfTWshfLfqqR68-O8CanHoB-Ng"

# تطبيق الألوان الفخمة (أسود وأحمر داكن) وضبط اتجاه النصوص العربية بالـ CSS
st.markdown("""
    <style>
    .stApp { background-color: #0d0d0d; color: #e5e5e5; }
    h1 { color: #d4af37 !important; text-align: center; font-family: 'Arial', sans-serif; font-size: 28px; padding-bottom: 20px; }
    
    /* تصميم زر الإرسال الاحترافي */
    .stButton>button { 
        background-color: #591313; color: white; 
        border-radius: 8px; border: 1px solid #cc1111;
        width: 100%; font-size: 18px; font-weight: bold;
        height: 45px; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #8c1c1c; border-color: #ff3333; color: white; }
    
    /* صندوق عرض الإجابة الذكي يدعم الكتابة من اليمين لليسار */
    .rtl-text { 
        direction: rtl; 
        text-align: right; 
        background-color: #141414; 
        padding: 18px; 
        border-radius: 8px; 
        border: 1px solid #401515;
        font-size: 16px;
        line-height: 1.6;
        color: #e5e5e5;
    }
    </style>
""", unsafe_allow_html=True)

# 2. العنوان الرئيسي للشاشة
st.markdown("<h1>PREMIUM INTERFACE - ASAD AL-DHALAM ED.</h1>", unsafe_allow_html=True)

# 3. عرض الشعار الفخم بالمنتصف
image_path = "logo.png"
if os.path.exists(image_path):
    st.image(image_path, width=320)
else:
    # لتلافي أي مشكلة بمسار الصورة، نجرّب نبحث عنها بنفس المجلد
    base_dir = os.path.dirname(__file__)
    alt_path = os.path.join(base_dir, "logo.png")
    if os.path.exists(alt_path):
        st.image(alt_path, width=320)
    else:
        st.error("⚠️ لم يتم العثور على صورة logo.png في المجلد! تأكد من وجودها بجانب ملف الكود.")

st.markdown("<br>", unsafe_allow_html=True)

# 4. خانة إدخال السؤال (تم حل مشكلة الـ Label والـ Warning)
user_question = st.text_input(label="اسأل أسد الظلام", placeholder="اكتب سؤالك هنا باللغة العربية ومزج براحتك...", key="input", label_visibility="visible")

# 5. زر المعالجة والإرسال
if st.button("👁️ إرسال السؤال إلى أسد الظلام"):
    if user_question.strip():
        with st.spinner("جاري التفكير وتحضير الإجابة من السيرفر الفخم... ⏳"):
            try:
                client = genai.Client(api_key=API_KEY)
                
                # تلقين الذكاء الاصطناعي شخصيته الأنيقة والذكية
                system_instruction = (
                    "أنت الآن لست مجرد ذكاء اصطناعي عادي، أنت المساعد الذكي المدمج في تطبيق 'أسد الظلام'. "
                    "تحدث مع المستخدم بذكاء شديد، بأسلوب فخم، وبسيط، وودود ومحفز مثل الزملاء والعباقرة. "
                    "أجب دائماً باللغة العربية المسترسلة والواضحة، وقدم حلولاً مباشرة وممتازة دون مقدمات جافة أو رسميات."
                )
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_question,
                    config=types.GenerateContentConfig(system_instruction=system_instruction)
                )
                
                # عرض النتيجة المنسقة داخل صندوق الـ RTL العربي
                st.markdown(f"<div class='rtl-text'>{response.text}</div>", unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"حدث خطأ في الاتصال: {str(e)}")
    else:
        st.warning("الرجاء كتابة سؤالك أولاً قبل الضغط على زر الإرسال!")