# Attendance Tool for CSC 4350 with Dr. Hatch
# Jacob Davis, Pierre Djaroueh, Creed Warf




# Setup
from flask import Flask, render_template, request, redirect, flash # For creating web app
from datetime import datetime # For generating timestamps
import sqlite3 # For database
import ipaddress # For IP address manipulation
import random  # For testing
import requests  # For sending HTTP requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SeCrEtKeY' # Generic key

lockedIPs = [] # List of IP's used to check in a student. Must be reset after each class period



# Authentication class
# This could be changed to just functions to avoid creating a new object every time a student checks in
class Authentication:
    # Constructor
    def __init__(self, correct_network_base='76.72.201.0/24'): # Creed's home network - would need to be changed to the school's network base
        # Initialize the AttendanceSystem with the correct network base
        self.correct_network = ipaddress.ip_network(correct_network_base, strict=False)
        self.test_mode = False
        self.test_ip = None

    # Function to get current external IP address
    def get_current_ip(self):
        if self.test_mode and self.test_ip:
            # Return the test IP if test mode is enabled
            return self.test_ip
        
        try:
            # List of services to get the external IP address
            ip_services = [
                'https://api.ipify.org',
                'https://ip.seeip.org',
                'https://ifconfig.me'
            ]
            
            for service in ip_services:
                # Try to get the IP address from each service
                response = requests.get(service, timeout=5)
                if response.status_code == 200:
                    return response.text.strip()
            
            # Raise an exception if no service could provide the IP
            raise Exception("Could not retrieve external IP")
        
        except requests.RequestException:
            # Handle network errors
            print("Network error retrieving external IP")
            return None

    # Function to check if current external IP is in school network subnet
    def validate_ip(self):
        current_ip = self.get_current_ip()
        
        try:
            # Convert the current IP to an ip_address object
            ip_obj = ipaddress.ip_address(current_ip)
            # Check if the IP is in the correct network
            is_valid = ip_obj in self.correct_network
            print(f"Current IP: {current_ip}")
            print(f"Network Check: {is_valid}")
            return is_valid
        except ValueError:
            # Handle invalid IP address
            return False
        
    # Function to check for multiple check-in attempts from same IP
    def check_locked(self):
        current_ip = self.get_current_ip()

        if current_ip in lockedIPs:
            return True
        else:
            return False

    # Authentication Function - not used
    # This function simulates auth code verification
    # Arbitrary 6-digit code is generated and compared to user input
    def send_authentication_push(self):
        print("Sending authentication request...")
        auth_code = str(random.randint(100000, 999999))
        print(f"Authentication code generated: {auth_code}")
        return auth_code

    # Check if the user input matches the generated code - not used
    def verify_authentication(self, sent_code):
        user_input = input("Enter authentication code: ")
        return user_input == sent_code

    # Main Attendance Marking Function
    # This function combines the IP validation, authentication, and attendance marking
    def mark_attendance(self):
        # IP Network Validation
        if not self.validate_ip():
            print("Error: Not on school network. Cannot mark attendance.")
            print(f"Current IP: {self.get_current_ip()}")
            return False
        if self.check_locked():
            print(f"Multiple student check-in attempt from {self.get_current_ip()}")
            return False
        else:
            lockedIPs.append(self.get_current_ip()) # Lock IP to prevent checking in multiple students
            return True

        # Authentication Push - not used
        #auth_code = self.send_authentication_push()

        # Code Verification - not used
        #if self.verify_authentication(auth_code):
        #    print("Attendance marked successfully!")
        #    return True
        #else:
        #    print("Authentication failed. Attendance not marked.")
        #    return False
# end class Authentication



# Funtion to connect to the database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn




# Check-in
@app.route('/', methods=('GET', 'POST'))
def checkIn():
    auth_system = Authentication() # Create Authentication object
    conn = get_db_connection() # Connect to database
    students = conn.execute('SELECT id, firstName, lastName FROM students').fetchall() # Get all student info
    conn.close() # Close database connection

    if request.method == 'POST':
        selectedStudents = request.form.getlist('students')  # Get selected student
        timestamp = datetime.now()  # Current timestamp
        formattedTime = timestamp.strftime("%B %d, %Y - %I:%M:%S %p") # Formatting timestamp


        # Add timestamp to attendance table
        if selectedStudents and len(selectedStudents) == 1: # One student selected
            try:
                conn = get_db_connection() # Connect to database
                for student_id in selectedStudents:
                    if auth_system.mark_attendance(): # Authenticate the selected student
                        conn.execute('INSERT INTO attendance (id, checkInTime) VALUES (?, ?)', (student_id, formattedTime)) # Create record of checkin in the database
                        flash('Check-in successful!') # Display confirmation message
                    else:
                        flash(('An error occurred while checking in.')) # If auth fails, display error message
                conn.commit() # Commit changes to database
                conn.close() # Close database connection

            except Exception:
                flash('An error occurred while checking in.')

        elif len(selectedStudents) > 1: # Multiple students selected
            flash('Must select only one student.') # Display error message

        else: # No students selected
            flash('Select a student to check in') # Display error message


        return redirect('/') # Refresh the page

    return render_template('checkin.html', students=students) # Return render template




# Attendance
@app.route('/attendanceList', methods=('GET', 'POST'))
def attendanceList():
    conn = get_db_connection() # Connect to database
    students = conn.execute('SELECT id, firstName, lastName FROM students').fetchall() # Get student info from student table in database
    attendanceRecords = conn.execute('SELECT id, checkInTime FROM attendance').fetchall() # Get timestamp info from attendance table in database
    conn.close() # Close database connection

    # Dictionary to track check-ins
    attendanceDict = {student['id']: {'name': f"{student['firstName']} {student['lastName']}", 'checkins': []} for student in students}

    # Add check-in times to dict
    for record in attendanceRecords: # Cycle through attendence records
        student_id = record['id'] # Selects current student
        if student_id in attendanceDict: # If student has checkins, append timestamps to attendence dictionary
            attendanceDict[student_id]['checkins'].append(record['checkInTime'])

    # Create list for rendering
    attendanceList = [] # List declaration
    for data in attendanceDict.values(): # Cycle through attendance dictionary
        # Add element to the list
        attendanceList.append({
            'name': data['name'],
            'checkins': data['checkins']
        })

    return render_template('attendanceList.html', attendanceList=attendanceList) # Return render template




# Hosting
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True) # Hosted locally for testing
