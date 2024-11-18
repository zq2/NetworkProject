# import socket # For getting the device's IP address // REMOVED
import ipaddress # For IP address manipulation
import random  # For testing
# import getpass  # For secure password input // REMOVED
import requests  # For sending HTTP requests

class AttendanceSystem:
    def __init__(self, correct_network_base='76.72.201.0/24'):
        # Initialize the AttendanceSystem with the correct network base
        self.correct_network = ipaddress.ip_network(correct_network_base, strict=False)
        self.test_mode = False
        self.test_ip = None

    def get_current_ip(self):
        """Get current external IP address."""
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

    def validate_ip(self):
        """Check if current external IP is in school network subnet."""
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

    # Test Mode Functions
    # These functions are used to simulate IP and authentication
    # Must be removed or disabled in production code
    def enable_test_mode(self, test_ip=None):
        """Enable test mode with optional IP override."""
        self.test_mode = True
        self.test_ip = test_ip
        print(f"Test mode enabled. Current test IP: {self.test_ip}")

    # Disable test mode and reset test IP

    def disable_test_mode(self):
        """Disable test mode and reset test IP."""
        self.test_mode = False
        self.test_ip = None
        print("Test mode disabled.")

    # Authentication Function
    # This function simulates auth code verification
    # Arbitrary 6-digit code is generated and compared to user input
    def send_authentication_push(self):
        """Simulate Duo push or authentication method."""
        print("Sending authentication request...")
        auth_code = str(random.randint(100000, 999999))
        print(f"Authentication code generated: {auth_code}")
        return auth_code

    # Check if the user input matches the generated code
    def verify_authentication(self, sent_code):
        """Verify authentication code."""
        user_input = input("Enter authentication code: ")
        return user_input == sent_code

    # Main Attendance Marking Function
    # This function combines the IP validation, authentication, and attendance marking
    def mark_attendance(self):
        """Main attendance marking workflow."""
        # IP Network Validation
        if not self.validate_ip():
            print("Error: Not on school network. Cannot mark attendance.")
            print(f"Current IP: {self.get_current_ip()}")
            return False

        # Authentication Push
        auth_code = self.send_authentication_push()

        # Code Verification
        if self.verify_authentication(auth_code):
            print("Attendance marked successfully!")
            return True
        else:
            print("Authentication failed. Attendance not marked.")
            return False

def main():
    attendance_system = AttendanceSystem()
    
    while True:
        # Main menu for the attendance system
        print("\n--- Network Attendance System ---")
        print("1. Mark Attendance")
        print("2. Enable Test Mode")
        print("3. Disable Test Mode")
        print("4. Exit")
        # User input for menu selection
        choice = input("Select an option: ")
        # Menu option handling
        if choice == '1':
            attendance_system.mark_attendance()
        elif choice == '2':
            attendance_system.enable_test_mode()
        elif choice == '3':
            attendance_system.disable_test_mode()
        elif choice == '4':
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
