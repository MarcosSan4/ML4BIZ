# ML4BIZ - Assignment 1 Setup Guide 🚀

## 📋 Project Overview
Bank Marketing Campaign - Predicting Term Deposit Subscription

**Team Members**: Javier Rodríguez Márquez, Marcos Santiago Soto  
**NIA**: 100498243

---

## 🔧 Setup Instructions for Your Teammate

### **Option 1: Local Development (Recommended)**

#### Step 1: Clone the Repository
```bash
git clone https://github.com/MarcosSan4/ML4BIZ.git
cd ML4BIZ
```

#### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv .venv

# Activate it (macOS/Linux)
source .venv/bin/activate

# Activate it (Windows)
# .venv\Scripts\activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Open Jupyter Notebook
```bash
# Option A: Using Jupyter Notebook
jupyter notebook

# Option B: Using VS Code (recommended)
# Just open "Assignment 1.ipynb" in VS Code
# VS Code will automatically detect and use the .venv environment
```

---

### **Option 2: Google Colab (No setup needed!)**

1. Go to [Google Colab](https://colab.research.google.com/)
2. Upload the notebook: `Assignment 1.ipynb`
3. Upload the dataset: `bank_24.pkl`
4. Run all cells!

**Note**: Colab has most libraries pre-installed (pandas, numpy, scikit-learn, matplotlib, seaborn)

---

## 📦 What's NOT Shared on GitHub

### **The `.venv/` folder is NOT in GitHub** because:
- It's too large (~500MB)
- It's machine-specific
- Each person needs to create their own using `requirements.txt`

### **What IS shared**:
- ✅ Notebooks (`.ipynb` files)
- ✅ Dataset (`bank_24.pkl`)
- ✅ Requirements file (`requirements.txt`)
- ✅ Documentation (`.md` files)

---

## 🔄 Git Workflow for Collaboration

### **Making Changes**

```bash
# 1. Always pull latest changes first
git pull origin main

# 2. Make your changes to the notebook

# 3. Check what changed
git status

# 4. Add your changes
git add "Assignment 1.ipynb"

# 5. Commit with descriptive message
git commit -m "Add EDA section with visualizations"

# 6. Push to GitHub
git push origin main
```

### **⚠️ Important Git Rules**

1. **Always `git pull` before starting work** (avoid merge conflicts!)
2. **Commit often** with clear messages
3. **Never commit** `.venv/` folder
4. **Communicate** with your teammate about which sections you're working on

---

## 🐍 Python Package Management

### **Installing New Packages**

If you need a new library (e.g., `xgboost`):

```bash
# 1. Activate virtual environment
source .venv/bin/activate

# 2. Install package
pip install xgboost

# 3. Update requirements.txt
pip freeze > requirements.txt

# 4. Commit requirements.txt
git add requirements.txt
git commit -m "Add xgboost dependency"
git push origin main

# 5. Tell your teammate to run:
# pip install -r requirements.txt
```

---

## 🆘 Troubleshooting

### **"Module not found" error**
```bash
# Make sure venv is activated
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### **Merge conflicts in notebook**
- Notebooks can be tricky with Git
- **Prevention**: Work on different sections
- **Solution**: Use VS Code's merge conflict resolver or keep one version

### **"Permission denied" on macOS/Linux**
```bash
chmod +x .venv/bin/activate
```

---

## 📚 Key Files

| File | Description |
|------|-------------|
| `Assignment 1.ipynb` | Main assignment notebook |
| `bank_24.pkl` | Dataset (11,000 samples) |
| `requirements.txt` | Python dependencies list |
| `.gitignore` | Files to exclude from Git |
| `SETUP_GUIDE.md` | This file |

---

## 🎯 Assignment Checklist

- [ ] 1. Simplified EDA (0.5 points)
- [ ] 2. Basic Methods: Trees, KNN, Logistic Regression (1 point)
- [ ] 3. Hyperparameter Optimization (1 point)
- [ ] 4. Advanced Methods: RF, XGBoost, etc. (1.5 points)
- [ ] 5. Results and Final Model (0.5 points)

---

## 💡 Tips for Collaboration

1. **Use comments** in code to explain your logic
2. **Update markdown cells** to document findings
3. **Use Git branches** for experimental features (optional)
4. **Meet regularly** to sync progress
5. **Test on Colab** before submission (teacher uses Colab!)

---

## 🔗 Useful Resources

- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

**Questions?** Contact: Javier or Marcos via Teams/Email

**Good luck! 🍀**
