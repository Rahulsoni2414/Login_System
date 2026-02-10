
import mysql.connector
from mysql.connector import Error

db_config = {
    'host': 'localhost',
    'user': 'COLLEGE',
    'password': 'Soni@1530',
    'database': 'COLLEGE'
}

def check_db():
    conn = None
    try:
        print(f"Connecting to database '{db_config['database']}' as '{db_config['user']}'...")
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print("Successfully connected to the database.")
            
            cursor = conn.cursor()
            cursor.execute("DESCRIBE STUDENT")
            columns = cursor.fetchall()
            
            print("\nColumns in STUDENT table:")
            col_names = [col[0] for col in columns]
            for col in columns:
                print(f"- {col[0]} ({col[1]})")
                
            required_cols = ['EMAIL', 'PASSWORD', 'OTP', 'IS_VERIFIED', 'ROLL_NO']
            missing = [col for col in required_cols if col not in col_names]
            
            if missing:
                print(f"\nCRITICAL: Missing columns: {missing}")
            else:
                print("\nSchema looks correct (EMAIL and PASSWORD exist).")
                
    except Error as e:
        print(f"\nError: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()
            print("\nConnection closed.")

if __name__ == "__main__":
    check_db()
