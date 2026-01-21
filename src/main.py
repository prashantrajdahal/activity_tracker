# main.py
def hello_world():
    return "Hello from virtual environment!"

if __name__ == "__main__":
    print(hello_world())
    # Check we're using venv Python
    import sys
    print(f"Python executable: {sys.executable}")