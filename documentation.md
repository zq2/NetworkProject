# Documentation
> ### Project Directive:
> - Attendance tool for classes; how to prevent checking in a friend?  what about really large classes?
# Introduction
### Problem to fix:
- Prevent students from checking in other students.
- Ensure students come to class
- Students who don't show up to class, do not get marked as present
### Existing Solutions:
- iClicker
    - Check in by answers questions on a clicker device or mobile app.
    - **Limitations:**
        - Students could lend each other their devices.
- Mobile Attendance Apps
    - Students can check in via their smartphones. These apps use GPS location to verify if students are in the classroom
    - Apps like **Acadly** use *geofencing* to constrain students to having to be within a specified radius.
    - **Limitations:**
        - Students can spoof GPS locations.
    - An additional feature of OTPs can work to mitigate this.
- Biometric Systems
    - Biometric systems use facial recognition or fingerprint scanning to mark attendance. Students must be physically present and pass biometric verification to check in for class.
    - Very difficult to spoof
    - **Limitations:**
        - Very expensive to implement
        - Problems could arise is biometric device malfunctions.
- Wi-Fi / Network Based Tools
    - *Eduroam* is one example
    - Mark attendance based on student's device being connected to the university's network. Eduroam allows universities to authenticate users based on their network credentials.
    - **Limitations:**
        - Students could still share credentials with other students. (I think)

### Our Solution: Attendance Web App

- The team first created a simple web app using the Flask micro web framework for Python
- In theory, students should check their name only, click ‘Check In’, and a timestamp for that class period will be recorded in the database
- Teachers can then see each student’s check-ins on the Attendance Record page

### Verifying Check-ins:
- The team created functions to verify the student is on the correct network by hardcoding the chosen network subnet and comparing that against the network the student is currently on
- In production, the hardcoded network would need to be updated to the correct network subnet for the school

### Authentication:
- In a production environment, something like 2-factor authentication would be used to log check-ins and prevent checking in multiple students from the same device during the same class period
- During development, the team created a rudimentary 2-factor authentication service to display a randomly generated code and have the user input the code in the terminal
- To keep the web app realistic, the team chose to log the IPs of the students when they check in, and prevent multiple check-ins from the same IP, opposed to requiring the user to type in the terminal
- In production, any log preventing multiple check-ins would need to be reset before a new class period

### Preventing Multiple Check-ins:
- The team disabled the ability to choose multiple students at the same time when checking in
- Any attempt to check in multiple students from the same device is prevented. This also flags the attempt and displays the IP address in the terminal
- An attempt to check in multiple students also displays an error message for the user

### Lessons Learned:
- Students can use tools like VPNs to circumvent network-based location checks
- Additional verification mechanisms, like GPS, OTPs, or biometric checks, are needed to improve security
- Adding these features increases development time and costs
- The app may perform differently depending on the network environment, such as the type of Wi-Fi or network configuration used by the school

### Conclusion:
- The team’s attendance tool offers a practical solution for tracking student attendance with features like network verification and authentication methods
- Adding additional features, like GPS or biometric checks, are impractical for this project due to the associated costs
- Using an existing product may offer a more efficient and cost-effective solution for attendance tracking compared to custom-built systems

### Proposed Questions:
1. Compare biometric and GPS verification methods in ensuring accurate attendance. Which would be more effective and why?
2. What are the limitations of using network and location-based verification methods for attendance tracking?
3. How can an attendance system prevent students from checking in multiple times on the same device?

