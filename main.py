from fastapi import FastAPI, Form, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")



# Add this right after app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Database connection helper
def get_db():
    conn = psycopg2.connect(
        host="localhost",
        database="fitness_db",
        user="postgres",
        password="yourpassword"
    )
    return conn

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit_lead")
async def submit_lead(
    name: str = Form(...), 
    email: str = Form(...), 
    goal: str = Form(...)
):
    # Insert data into PostgreSQL
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO leads (name, email, goal) VALUES (%s, %s, %s)",
        (name, email, goal)
    )
    conn.commit()
    cur.close()
    conn.close()
    
    return {"status": "success", "message": f"Plan created for {name}!"}

# Bonus: Route to retrieve all users
@app.get("/admin/leads")
async def get_leads():
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM leads ORDER BY created_at DESC")
    leads = cur.fetchall()
    cur.close()
    conn.close()
    return leads
