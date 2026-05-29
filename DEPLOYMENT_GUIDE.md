# 🚀 Easy Streamlit Cloud Deployment Guide (2 Minutes)

Since local command-line `git` is not installed on your system, you can easily deploy your app by uploading it directly to GitHub using your web browser. Follow these simple steps:

---

### Step 1: Create a GitHub Repository
1. Open your browser and go to [github.com](https://github.com/) (Sign in or sign up for a free account if you haven't already).
2. Click the **"New"** button on the left sidebar (or go to [github.com/new](https://github.com/new)).
3. Name your repository: **`wheelz-coach`**.
4. Set the repository visibility to **Public** or **Private** (both work!).
5. **CRITICAL:** Do NOT check "Add a README file", "Add .gitignore", or "Choose a license". Keep it completely empty.
6. Click **"Create repository"**.

---

### Step 2: Upload Your Files via Browser
1. On the page that appears, look for the text: *"Get started by creating a new file or **uploading an existing file**."*
2. Click the blue **"uploading an existing file"** link.
3. Open your computer's File Explorer to `d:\Eng_Prac`.
4. Drag and drop the following items from your folder into the GitHub box:
   * 📄 **`English_prac.py`**
   * 📄 **`requirements.txt`**
   * 📂 **`tests`** (the entire folder containing the 8 JSON question files)
5. Wait for the files to finish uploading.
6. Scroll down and click the green **"Commit changes"** button.

---

### Step 3: Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io/) in your browser.
2. Click **"Connect GitHub"** and sign in.
3. Once logged in, click the **"New app"** button.
4. Fill in the fields:
   * **Repository:** Select your `github_username/wheelz-coach` repo.
   * **Branch:** Set to `main`.
   * **Main file path:** Type `English_prac.py`.
5. Click **"Deploy!"**
6. Within 1 minute, your app will be live and you will receive a public link (e.g., `https://wheelz-coach.streamlit.app`).

---

### Step 4: Access on your Android Phone
1. Open the deployment link on your **Android phone's Chrome browser**.
2. Tap the **three dots (menu)** in the top-right corner of Chrome.
3. Select **"Add to Home screen"**.
4. A **"Wheelz Coach"** icon will appear on your phone's home screen. Tap it to launch your app full-screen like a native Android app!
