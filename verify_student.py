
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'COLLEGE',
    'password': 'Soni@1530',
    'database': 'COLLEGE'
}

def verify_student():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM STUDENT WHERE EMAIL = 'testuser@example.com'")
        student = cursor.fetchone()
        
        if student:
            print(f"SUCCESS: Student found: {student['NAME']}, Roll No: {student['ROLL_NO']}")
            print(f"Roll No Type Verification: {type(student['ROLL_NO'])}")
        else:
            print("FAILURE: Student not found.")
            
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    verify_student()
