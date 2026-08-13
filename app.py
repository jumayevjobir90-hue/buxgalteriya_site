from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    services = [
        {"title": "Soliq va Moliyaviy Hisobotlar", "desc": "Barcha turdagi soliq va moliyaviy hisobotlarni o'z vaqtida hamda xatosiz topshirish.", "icon": "bi-calculator"},
        {"title": "Kadrlar Hisobi va Oylik Maosh", "desc": "Xodimlarni ishga qabul qilish, buyruqlar tayyorlash va ish haqini aniq hisoblash.", "icon": "bi-people"},
        {"title": "1S va E-imzo integratsiyasi", "desc": "Elektron schyot-faktura (ESF), 1S bazasini yuritish hamda e-imzo operatsiyalari.", "icon": "bi-laptop"},
        {"title": "Buxgalteriya Tiklash va Konsultatsiya", "desc": "Chalkashib ketgan hisob-kitoblarni tartibga solish va biznes uchun doimiy maslahatlar.", "icon": "bi-shield-check"}
    ]
    
    info = {
        "name": "Jumayev Jobir",
        "title": "Masofaviy Buxgalteriya Xizmati",
        "experience": "8 yillik tajribaga ega buxgalter",
        "phone1": "+998906149496",
        "phone1_fmt": "+998 (90) 614-94-96",
        "phone2": "+998936519496",
        "phone2_fmt": "+998 (93) 651-94-96",
        "telegram": "J11031990J",
        "work_hours": "24/7 (Doimiy aloqada)",
        "price": "Narxlar kelishilgan holda"
    }
    testimonials = [
        {"name": "Nurali Valiyev", "comment": "Jobir aka bilan ishlash juda qulay, barcha hisobotlar o'z vaqtida.", "rating": 5},
        {"name": "Madina Karimova", "comment": "Buxgalteriya bo'yicha eng yaxshi maslahatlar va yordam, tavsiya qilaman!", "rating": 5},
        {"name": "Sherzod Aliyev", "comment": "1S bazasini yuritishda katta yordam berdi, ishonchli mutaxassis.", "rating": 5},
        {"name": "Djamol Muzafarov", "comment": "Korxonamni hisob kitobini ancha yillardan beri yuritib kelmoqda, hozirgacha hechqanday kamchilik ko'rganim yoq.", "rating": 5},
        {"name": "Abdurashid Safarov", "comment": "Soliqdan katta qarzdorlik chiqargan edi, xudoga shukur bartaraf qilib berdilar.", "rating": 5}
    ]
    
    return render_template("index.html", services=services, info=info, testimonials=testimonials)

if __name__ == "__main__":
    app.run(debug=True)