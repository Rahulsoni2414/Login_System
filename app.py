from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here' # Needed for flash messages

# Database Configuration
db_config = {
    'host': 'localhost',
    'user': 'COLLEGE',
    'password': 'Soni@1530',
    'database': 'COLLEGE'
}

def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.route('/')
def home():
    return render_template('index.html')

from utils.email_utils import generate_otp, send_otp_email

# Email Configuration moved to utils/email_utils.py

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        roll_no = request.form['roll_no']
        email = request.form['email']
        password = request.form['password']
        city = request.form['city']
        marks = 0 
        grade = 'N'
        
        # Generate OTP
        otp = generate_otp()
        
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            try:
                # Insert with IS_VERIFIED = False (0)
                sql = "INSERT INTO STUDENT (ROLL_NO, NAME, EMAIL, PASSWORD, CITY, MARKS, GRADE, OTP, IS_VERIFIED) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (roll_no, name, email, password, city, marks, grade, otp, 0)
                cursor.execute(sql, val)
                conn.commit()
                
                # Send Email
                if send_otp_email(email, otp):
                    flash('Registration successful! OTP sent to your email.', 'success')
                else:
                    flash('Registration successful! Failed to send email (Check console for OTP).', 'warning')
                
                conn.close()
                return redirect(url_for('verify_otp')) 
            except Error as e:
                flash(f'Registration failed: {e}', 'error')
                conn.close()
                return redirect(url_for('login'))
        else:
             flash('Database connection error.', 'error')
             return redirect(url_for('login'))

@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        otp_input = request.form['otp']
        
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            # Find user with this OTP and not verified
            cursor.execute("SELECT * FROM STUDENT WHERE OTP = %s AND IS_VERIFIED = 0", (otp_input,))
            user = cursor.fetchone()
            
            if user:
                # Update status
                cursor.execute("UPDATE STUDENT SET IS_VERIFIED = 1 WHERE ROLL_NO = %s", (user['ROLL_NO'],))
                conn.commit()
                conn.close()
                flash('Email verified! You can now login.', 'success')
                return redirect(url_for('login'))
            else:
                conn.close()
                flash('Invalid or expired OTP.', 'error')
                return redirect(url_for('verify_otp'))
    
    return render_template('verify_otp.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM STUDENT WHERE EMAIL = %s AND PASSWORD = %s", (email, password))
            user = cursor.fetchone()
            conn.close()
            
            if user:
                if user['IS_VERIFIED']:
                    flash('Login successful!', 'success')
                    return redirect(url_for('dashboard')) 
                else:
                    flash('Please verify your email first.', 'error')
                    # Optional: Offer to resend OTP logic (omitted for brevity)
                    return redirect(url_for('verify_otp'))
            else:
                flash('Invalid email or password.', 'error')
                return redirect(url_for('login'))
        else:
             flash('Database connection error.', 'error')
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return "<h1>Welcome to the Student Dashboard</h1>"

@app.route('/api/stats')
def get_stats():
    # Placeholder for fetching real stats from DB
    return jsonify({
        'students': 1200,
        'faculty': 75,
        'courses': 30,
        'placements': '95%'
    })

if __name__ == '__main__':
    app.run(debug=True)
