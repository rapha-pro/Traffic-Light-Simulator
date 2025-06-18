import os
import subprocess

def create_dirs():
    dirs = [
        "data/raw",
        "data/processed",
        "notebooks",
        "src/data",
        "src/features",
        "src/models",
        "src/visualization",
        "tests"
    ]
    for path in dirs:
        os.makedirs(path, exist_ok=True)
        print(f"📁 Created: {path}")

def create_gitignore():
    content = """# Byte-compiled / cache
__pycache__/
*.py[cod]
*.ipynb_checkpoints

# Environments
.env
.venv
env/
venv/
Pipfile.lock

# Data
/data/raw/
/data/processed/

# Jupyter
.ipynb_checkpoints/

# VSCode
.vscode/
"""
    if not os.path.exists(".gitignore"):
        with open(".gitignore", "w", encoding="utf-8") as gitignore_file:
            gitignore_file.write(content)
        print("✅ Created .gitignore")
    else:
        print("⚠️  .gitignore already exists, skipped.")


def create_readme():
    content = """# 🚦 Smart Traffic Light Predictor
A machine learning project that predicts:
- The state of the next traffic light (green/red)
- The time until the light changes
Based on vehicle trajectory data from the HighD dataset (Germany highway driving data).

## 🧠 Skills Practiced
- Data preprocessing and wrangling
- Time-based feature engineering
- Binary classification and regression (ML)
- Model interpretability and performance analysis

## 🚀 Goals
Get this project to a point where it could land you a data science or ML internship at Tesla, Ford, or Mercedes.

## 📁 Structure
- `data/`: raw and processed HighD data
- `src/`: all ML pipeline and code
- `notebooks/`: exploration and visualization
"""
    if not os.path.exists("REAMDE.md"):
        with open("README.md", "w", encoding="utf-8") as readme_file:
            readme_file.write(content)
            print("✅ Created readme.md")
    else:
        print("⚠️ README.md file already exists, skipped.")


def init_pipenv():
    print("📦 Initializing pipenv...")
    subprocess.call(["pipenv", "install", "pandas", "numpy", "matplotlib", "seaborn", "scikit-learn", "jupyter", "tqdm"])

def main():
    print("🚀 Setting up Smart Traffic Light Prediction Project...\n" + "=" * 60)
    create_dirs()
    create_gitignore()
    create_readme()
    init_pipenv()
    print("\n✅ All done. Open your notebook with:\n  pipenv run jupyter notebook notebooks/")

if __name__ == "__main__":
    main()
