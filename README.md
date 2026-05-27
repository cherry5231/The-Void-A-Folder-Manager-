# The-Void-A-Folder-Manager-
#  VOID PROJECT

A Python-based file system simulation where files can be **consumed, preserved, and restored** using unique V-codes.

---

#  Features

- Generates unique V-codes for each file
- Consume files (moves them to `consumed/`)
- Preserve files (moves them to `survivors/`)
- Restore files using V-codes
- Simple terminal-based interface
- Automatic folder handling (if setup script is used)
- Protoype Login Page 
---

#  Project Structure

```
starting/
└── projects/
    └── Void/
        ├── incoming/     # New files go here
        ├── survivors/    # Preserved files
        ├── consumed/     # Consumed files
```

---

#  How to Run

## 1. Setup folders (if not already created)

Make sure these folders exist:

```
starting/projects/Void/incoming
starting/projects/Void/survivors
starting/projects/Void/consumed
```

OR run your setup script if included.

---

## 2. Run the program

```bash
python void.py
```

---

#  How It Works

## Step 1: V-Code Generation
Each file in `incoming/` is assigned a random V-code.

Example:
```
V-code 4821 :: test.txt
V-code 1903 :: image.gif
```

---

## Step 2: Choose Action

You will be asked:

```
Consume or Preserve?
```

###  Consume
- File moves to `consumed/`

###  Preserve
- File moves to `survivors/`

---

## Step 3: Restore System

You can restore files by:

- Entering RESTORE mode
- Choosing the correct V-code

Restored files go to:
```
survivors/
```

---
## Step 4: Try Prototype Login Page
- Click on void.html
- run it in VS code using HTML,CSS and LIVE SERVER extensions

#  Notes

- V-codes are randomly generated every run
- Files are physically moved between folders
- Ensure folders exist before running
- Works only on local system

---

#  Requirements

Uses only Python standard libraries:

- os
- shutil
- random
- urllib

No external installations needed.

---

#  Future Improvements

- Save V-codes using JSON database
- Add password protection for files
- GUI version of VOID
- File encryption system
- Search system for V-codes

---

#  Concept

VOID simulates a system where:
- Files are judged
- Files are consumed or preserved
- Only selected files survive
```
