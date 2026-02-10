
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'COLLEGE',
    'password': 'Soni@1530',
    'database': 'COLLEGE'
}

def get_otp():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT OTP FROM STUDENT WHERE EMAIL = 'otpuser@test.com'")
        user = cursor.fetchone()
        
        if user:
            print(f"OTP: {user['OTP']}")
        else:
            print("User not found.")
            
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_otp()
