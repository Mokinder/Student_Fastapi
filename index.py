from fastapi import APIRouter,FastAPI
from schemas.student import Student
from config.db import con
from models.index1 import students
from sqlalchemy import select,insert,delete,update,func

app=FastAPI()
#app = APIRouter()


@app.get('/api/home')
async def home():
    return "Home Page !!"


@app.get('/api/get_all_dts')
async def getdetails():
    data=con.execute(students.select()).fetchall()
    return{
         "success":True,
        "data":data
    }


@app.post('/api/create')
async def create(student : Student):
    data = con.execute(students.insert().values(
        name=student.name,
        email=student.email,
        age=student.age,
        country=student.country
    ))
    if data.is_insert :
        return {
            "success ": True,
            "msg": "student created successfully !!"
        }
    else :
        return{
            "success":False,
            "msg":"Some thing wrong..!"
        }


@app.put("/api/update/{id}")
async def update(id:int,updat: Student):
    con.execute(students.update().values(
        name=updat.name,
        email=updat.email,
        age=updat.age,
        country=updat.country
    ).where(students.c.id == id))
    return con.execute(students.select()).fetchall()


@app.delete("/api/delete/{id}")
async def delete(id:int):
    data= con.execute(students.delete().where(students.c.id == id))
    if data:
        return {
            "success":True,
            "msg": f" {id} is deleted successufully!!"
        }
    else:
        return {
            "success": True,
            "msg":"some problem is raised!!"
        }

@app.get("/api/search/{search}")
async  def search_id(search):
    data=con.execute(students.select().where(students.c.id.like('%'+search+'%'))).fetchall()
    if data:
      return {
        "success":True,
        "data":data
    }
    else:
        return {
            "success": True,
            "msg":"some problem is raised !!"
        }
