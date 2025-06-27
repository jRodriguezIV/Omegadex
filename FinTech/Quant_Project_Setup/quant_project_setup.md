# 🧠 Quant Notebook Project Setup Guide

Use this checklist every time you want to start a new notebook-based project with GitHub and a clean environment.

---

## ✅ Step-by-Step Instructions

### 🗂️ 1. Create Your Project Folder
```bash
mkdir New_Project_Name
cd New_Project_Name
```

---

### 📁 2. Create and Activate Conda Environment
```bash
conda create -n new_env_name python=3.10
conda activate new_env_name
```

---

### 📦 3. Install Core Packages
```bash
conda install numpy pandas matplotlib seaborn jupyter scikit-learn -c conda-forge
pip install yfinance
```

---

### 📝 4. Create a Jupyter Notebook
```bash
jupyter notebook
```

Save it as `new_strategy.ipynb`

---

### 🔒 5. Create a .gitignore
```bash
echo "venv/\n__pycache__/\n.ipynb_checkpoints/\n*.csv" > .gitignore
```

---

### 🧪 6. Create a Clean `requirements.txt`
```bash
echo numpy > requirements.txt
echo pandas >> requirements.txt
echo matplotlib >> requirements.txt
echo seaborn >> requirements.txt
echo yfinance >> requirements.txt
echo jupyter >> requirements.txt
echo scikit-learn >> requirements.txt
```

---

### 🔬 7. Create Minimal `environment.yml` (optional)
```bash
echo "name: new_env_name" > environment.yml
echo "channels:" >> environment.yml
echo "  - conda-forge" >> environment.yml
echo "  - defaults" >> environment.yml
echo "dependencies:" >> environment.yml
echo "  - python=3.10" >> environment.yml
echo "  - numpy" >> environment.yml
echo "  - pandas" >> environment.yml
echo "  - matplotlib" >> environment.yml
echo "  - seaborn" >> environment.yml
echo "  - yfinance" >> environment.yml
echo "  - jupyter" >> environment.yml
echo "  - scikit-learn" >> environment.yml
```

---

### 📄 8. Add a README
```bash
echo "# New Project\n\nThis project contains research for a new trading strategy." > README.md
```

---

### 🔧 9. Initialize Git and Commit
```bash
git init
git add .
git commit -m "Initial commit"
```

---

### ☁️ 10. Create GitHub Repo and Push

1. Create a new GitHub repo (no README or license).
2. Then:
```bash
git remote add origin https://github.com/YOUR_USERNAME/YourRepoName.git
git branch -M main
git push -u origin main
```

---

Enjoy your project 🚀