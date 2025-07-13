# 📔 Daftarche Khatere (دفترچه خاطرات) - CLI Memory Journal

[![Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A bilingual (English/Persian) command-line journal application for preserving memories with simple file-based storage.

**برنامه خط فرمان برای ثبت خاطرات با قابلیت کار به دو زبان انگلیسی و فارسی**

## ✨ Features
- **Add/Remove/List** memories with numbered IDs
- **Automatic day/night mode** detection
- **Plaintext storage** (easy backup/migration)
- **Persian-friendly** interface
- **Zero dependencies** (pure Python)

## 🚀 Quick Start
```bash
# Clone and run
git clone https://github.com/yourusername/daftarche-khatere.git
cd daftarche-khatere
python khatere.py
📋 Usage Examples
$ python khatere.py
Hello and welcome to daftarche khatere software.

What are you going to do? [help/add/remove/show/quit]: add
Enter Your khatereh: امروز پروژه جدیدم رو شروع کردم...
🧠 Core Implementation
# File-based persistence
def add():
    khatere = input("Enter Your khatereh : ").strip()
    with open(file_path, "a") as f: 
        f.write(f"{line_count(file_path) + 1}. {khatere}\n")

# Smart line renumbering during deletion
def remove(file):
    # ... (your elegant line reindexing logic)
🌟 Key Technical Highlights

    1- File I/O Operations: Safe file handling with context managers

    2- CLI Interface: Clean user interaction flow

    3- Time Awareness: Dynamic day/night greetings

    4- Idempotent Deletion: Automatic ID renumbering

🤝 How to Contribute

    Fork the repository

    Create a feature branch (git checkout -b enhance/x)

    Commit changes (git commit -am 'Add some feature')

    Push to branch (git push origin enhance/x)

    Open a Pull Request

📜 License

MIT License - Free for personal and commercial use
Why This Project?

    Demonstrates clean Python fundamentals: File I/O, datetime, CLI handling

    Solves real-world need for private, portable journaling

    Excellent portfolio piece showing practical coding skills

📫 Contact: mani.obara.work@gmail.com |
