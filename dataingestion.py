import os
import subprocess
import sys

def check_requirements_file():
    """Check if the requirements.txt file exists in the current directory."""
    if not os.path.exists('requirements.txt'):
        print("requirements.txt not found in the current directory.")
        sys.exit(1)
    else:
        print("requirements.txt found.")

def install_requirements():
    """Install the dependencies listed in requirements.txt."""
    try:
        # Use subprocess to run the pip command to install requirements
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("All dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing dependencies: {e}")
        sys.exit(1)

def main():
    check_requirements_file()
    install_requirements()

if __name__ == "__main__":
    main()
