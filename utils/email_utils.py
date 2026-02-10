
import smtplib
import random
import os

# Email Configuration
EMAIL_USER = os.environ.get('EMAIL_USER', 'your_email@gmail.com')
EMAIL_PASS = os.environ.get('EMAIL_PASS', 'your_app_password')

def generate_otp():
    """Generates a 6-digit OTP."""
    return str(random.randint(100000, 999999))

def send_otp_email(to_email, otp):
    """Sends OTP to the given email address using Gmail SMTP."""
    try:
        if EMAIL_USER == 'your_email@gmail.com' or EMAIL_PASS == 'your_app_password':
            print(f"WARNING: Email credentials not set. OTP for {to_email}: {otp}")
            return False

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        
        subject = "Your Future College Verification Code"
        body = f"Hello,\n\nYour OTP for Future College registration is: {otp}\n\nPlease enter this code to verify your account.\n\nRegards,\nFuture College Team"
        
        msg = f"Subject: {subject}\n\n{body}"
        
        server.sendmail(EMAIL_USER, to_email, msg)
        server.quit()
        print(f"Email sent to {to_email}")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        # Fallback logging
        print(f"------------ FALLBACK OTP for {to_email}: {otp} ------------")
        return False
