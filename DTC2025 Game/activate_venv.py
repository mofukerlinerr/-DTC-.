import os
import sys

def activate_venv():
    venv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.venv'))
    activate_this = os.path.join(venv_path, 'Scripts', 'activate_this.py')
    
    if not os.path.exists(activate_this):
        raise RuntimeError(f"Cannot find the virtual environment activation script at {activate_this}")

    exec(open(activate_this).read(), {'__file__': activate_this})
    
    if sys.prefix == sys.base_prefix:
        raise RuntimeError("Virtual environment not activated successfully")

if __name__ == "__main__":
    activate_venv()