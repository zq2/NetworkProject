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
    