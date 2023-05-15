from fastapi import FastAPI, HTTPException
import uvicorn
import mysql.connector
import datetime


app = FastAPI()

@app.get("/insert/{studentId}/{studentName}/{AttToday}")
def insert(studentId, studentName, AttToday):
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'adminadmin1',
        'database': 'attendace'    
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    sql = "INSERT INTO attendance (regiDate, studentId, studentName, AttToday) VALUES (%s, %s, %s, %s)"
    date = datetime.datetime.now()
    
    cursor.execute(sql, (date, studentId, studentName, AttToday))
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "Data inserted successfully"}
    
        
if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000)
