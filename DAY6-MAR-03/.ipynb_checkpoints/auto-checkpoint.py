import re
import json
import logging

# Set up logging (console output only)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class LaunchAuthorizationSystem:
    """Handles nuclear launch authorization validation."""
    
    AUTH_PATTERN = r"^AUTH-[A-Z0-9]{3,6}-\d{4}-SECURE$"  # Regex for security code validation

    @staticmethod
    def validate_code(code):
        """Validates the launch authorization code."""
        if re.match(LaunchAuthorizationSystem.AUTH_PATTERN, code):
            logging.info("Authorization Code Validated Successfully!")
            return True
        else:
            logging.warning("Invalid Authorization Code!")
            return False
    def validate_dual(code1,code2):
        """Validates the launch authorization code."""
        if re.match(LaunchAuthorizationSystem.AUTH_PATTERN, code1) and re.match(LaunchAuthorizationSystem.AUTH_PATTERN, code2):
            logging.info("Authorization Code Validated Successfully!")
            return True
        else:
            logging.warning("Invalid Authorization Code!")
            return False
    def patrol_region(latitude,longitude):
        pass
