README for Bira Beast App Automation Using Appium

Introduction
This README file provides a step-by-step guide to setting up your environment and running automation scripts for the Bira Beast App using Appium with Python. Follow the instructions to install the required tools, libraries, and frameworks.

1. Prerequisites
Before starting, ensure the following:
A PC/Laptop with at least 4GB RAM and 20GB free storage.
Java installed (Appium requires Java for execution).
Android Device (Emulator or Physical Device) configured for testing.
Python 3.8+ installed.

2. Installation Guide
Step 1: Install Python
Download the latest Python version from Python's official site.
Install Python and check the option "Add Python to PATH" during installation.
Verify installation:
bash
Copy code
python --version


Step 2: Install Node.js and npm
Appium requires Node.js for execution:
Download and install Node.js from Node.js official site.
Verify installation:
bash
Copy code
node --version
npm --version


Step 3: Install Appium
Use npm to install Appium globally:
bash
Copy code
npm install -g appium


Verify Appium installation:
bash
Copy code
appium --version


Launch Appium:
bash
Copy code
appium


Step 4: Install Appium Desktop (Optional)
For easier debugging, download the Appium Desktop GUI tool from Appium Desktop.

3. Android Studio Setup
Download and install Android Studio from Android Studio's official site.
Configure the Android Virtual Device (AVD) for testing:
Open Android Studio > Tools > AVD Manager > Create Virtual Device.
Set the ANDROID_HOME environment variable:
Add the following paths to your system's environment variables:
makefile
Copy code
ANDROID_HOME = <Path to Android SDK>
PATH = %ANDROID_HOME%\platform-tools



4. Appium Python Client Setup
Install the Appium Python client using pip:
bash
Copy code
pip install Appium-Python-Client


Install other dependencies:
bash
Copy code
pip install pytest selenium


Verify the installations:
bash
Copy code
pip list



5. Pycharm IDE Setup
Download and install Pycharm Community Edition from JetBrains website.
Create a new project:
File > New Project > Select Python as the project type.
Configure the Python interpreter:
File > Settings > Project Interpreter > Add Python interpreter path.
Install additional Python packages in the IDE terminal:
bash
Copy code
pip install pytest pytest-html



6. Device Setup
Enable Developer Options on your Android device.
Enable USB Debugging.
Verify device connection using ADB:
bash
Copy code
adb devices



7. Running Automation Tests
Clone the Bira Beast App Automation repository:
bash
Copy code
git clone <repository_url>
cd <repository_folder>


Run tests using pytest:
bash
Copy code
pytest --html=report.html


Ensure Appium server is running during execution:
bash
Copy code
appium



8. Common Commands
Install a package:
bash
Copy code
pip install <package_name>


Uninstall a package:
bash
Copy code
pip uninstall <package_name>


Run Appium server:
bash
Copy code
appium


Start Android emulator:
bash
Copy code
emulator -avd <AVD_NAME>


Generate HTML reports for pytest:
bash
Copy code
pytest --html=report.html



9. Troubleshooting
Appium server not starting:
Ensure Node.js and Appium are correctly installed.
Check if another instance of Appium is already running.
Device not detected:
Ensure USB debugging is enabled.
Restart ADB server:
bash
Copy code
adb kill-server
adb start-server


Emulator issues:
Verify that the Android Virtual Device is configured correctly.

10. Directory Structure
## Project Structure ##
project/
├── config/
│   ├── config.json             # Stores session, environment, and app config details
│   ├── capabilities.json       # Desired capabilities for devices and platforms
├── logs/
│   ├── test.log                # Log files for test execution
├── reports/
│   ├── report.html             # Test execution reports
├── screenshots/
│   ├── screenshot_1.png        # Screenshots captured during tests
├── src/
│   ├── __init__.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_login.py       # Test cases for login
│   │   ├── test_feature1.py    # Test cases for a feature
│   │   ├── test_feature2.py    # Test cases for another feature
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── login_page.py       # Page Object for Login
│   │   ├── home_page.py        # Page Object for Home
│   │   ├── feature_page.py     # Page Object for a feature
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── appium_utils.py     # Functions for Appium-specific utilities
│   │   ├── session_manager.py  # Manage session storage and retrieval
│   │   ├── logger.py           # Logging configuration
├── requirements.txt            # Python dependencies
├── conftest.py                 # Pytest fixtures and hooks
├── pytest.ini                  # Pytest configuration
├── README.md                   # Project documentation

11. Notes
Keep all dependencies updated regularly.
Use virtual environments for better dependency management:
bash
Copy code
python -m venv env
source env/bin/activate  # (Linux/Mac)
.\env\Scripts\activate   # (Windows)



