import subprocess
import os
import sys

def fix_requirements():
    venv_dir = "venv-fix"
    python_exe = os.path.join(venv_dir, "Scripts", "python.exe")
    pip = os.path.join(venv_dir, "Scripts", "pip.exe")

    print("📦 Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)

    print("🧹 Installing packages with conflict resolution...")
    subprocess.run([pip, "install", "--upgrade", "setuptools", "wheel"], check=True)
    subprocess.run([pip, "install", "-r", "requirements.txt"], check=True)

    print("🗒️  Freezing resolved requirements to requirements-fixed.txt...")
    with open("requirements-fixed.txt", "w") as f:
        subprocess.run([pip, "freeze"], stdout=f, check=True)

    print("✅ All done! Please rename 'requirements-fixed.txt' to 'requirements.txt' and redeploy.")

if __name__ == "__main__":
    fix_requirements()
