from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import random

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Преподаватели и предметы
teachers = [
    "E.Tulegenov", "A.Sarsembayeva", "N.Makhambetov", "Z.Kairatova",
    "A.Tynyshev", "M.Zhakenova", "Y.Kenzhebekov", "A.Abdykarimova",
    "D.Kairbekov", "G.Asanova", "T.Kairzhanov", "B.Nurmagambetova",
    "A.Sagyndykov", "Z.Aitbayeva", "A.Sultangali", "S.Serikbayeva",
    "T.Zhaksylyk", "A.Kairbekova", "Y.Mukhametov", "B.Nurmagambetova"
]

subjects = [
    "Python bagdarlamalau negizderi", "Web-damu negizderi", "Derekqorlar menen is jurgizu",
    "Mashinalyq oqytu", "Jasandy intelekt", "Kiberqauipsizdik", "Mobildi qosymshalar jasau",
    "Serverlik bagdarlamalau", "UI/UX dizayn", "Cloud Computing",
    "DevOps negizderi", "Python-da derekter taldau", "Web-skreypping",
    "Grafikalyq interfeyster jasau", "Ashyq derektermen jumys",
    "Internet zattary (IoT)", "Blockchain tehnologiyalary",
    "Tabigi tilderdi ondeu (NLP)", "Grafikter bagdarlamalau", "Kross-platformalyq mobildi damu"
]

# Кабинеты старого и нового корпуса
old_corpus_cabinets = [f'Eski korpys {i}' for i in range(110, 291)]
new_corpus_cabinets = [f'Jana korpys {i}' for i in range(291, 331)]
cabinets = old_corpus_cabinets + new_corpus_cabinets


# Генерация расписания
def generate_schedule():
    schedule = {}
    groups = [f"Sw{str(i).zfill(2)}" for i in range(1, 9)]
    days = ["Дүйсенбі", "Сейсенбі", "Сәрсенбі", "Бейсенбі", "Жұма"]

    for group in groups:
        schedule[group] = {}
        for day in days:
            schedule[group][day] = []
            for _ in range(3):  # 3 сабақ
                subject = random.choice(subjects)
                teacher = random.choice(teachers)
                cabinet = random.choice(cabinets)
                schedule[group][day].append((subject, teacher, cabinet))

    return schedule


@app.get("/")
async def read_root(request: Request):
    schedule = generate_schedule()
    return templates.TemplateResponse("index.html", {"request": request, "schedule": schedule})