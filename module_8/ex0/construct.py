import sys
import os
import site
 
 
def is_virtual_env() -> bool:
    """Detect if we are running inside a virtual environment."""
    return sys.prefix != sys.base_prefix or os.environ.get("VIRTUAL_ENV") is not None
 
 
def get_venv_name() -> str:
    """Get the name of the active virtual environment."""
    venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
    return os.path.basename(venv_path)
 
 
def get_package_path() -> str:
    """Get the site-packages path for the current environment."""
    packages = site.getsitepackages()
    return packages[0] if packages else "Unknown"
 
 
def show_outside_venv() -> None:
    """Display info and instructions when outside a virtual environment."""
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python:      {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("  python -m venv matrix_env")
    print("  source matrix_env/bin/activate   # On Unix")
    print("  matrix_env\\Scripts\\activate      # On Windows")
    print()
    print("Then run this program again.")
 
 
def show_inside_venv() -> None:
    """Display info when inside a virtual environment."""
    venv_name = get_venv_name()
    venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
    package_path = get_package_path()
 
    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python:      {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path:    {venv_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(f"  {package_path}")

 
def main() -> None:
    """Main entry point."""
    if is_virtual_env():
        show_inside_venv()
    else:
        show_outside_venv()
 
 
if __name__ == "__main__":
    main()
 