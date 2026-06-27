from pathlib import Path

NUMBER_OF_STUDENTS = 135  # Number of student IDs to check
LOGIN_URL = "https://accounts.google.com/"
WAIT_TIME = 10  # Time to wait for the page to load (in seconds)
BASE_DIR = (
    Path(__file__).resolve().parent.parent
)  # Path to the base directory of the project
OUTPUT_FILE = (
    BASE_DIR / "data" / "gmail_login_results.xlsx"
)  # Path to the output file for storing the results
print(
    f"Output file path: {OUTPUT_FILE}"
)  # Print the output file path for debugging purposes
