# 📧 Mail Merge Project

A simple Python project that automates the process of creating personalized letters for multiple people.

Instead of manually writing a separate letter for every person, the program reads a list of names, replaces the placeholder `[name]` in a letter template, and creates a separate personalized letter for each person.

## 📌 Project Overview

The program performs these main steps:

1. Reads the names from `invited_names.txt`.
2. Removes unnecessary whitespace and newline characters from each name.
3. Reads the letter template from `starting_letter.txt`.
4. Replaces the `[name]` placeholder with each person's name.
5. Creates a separate `.txt` file for every person.
6. Saves the personalized letters inside the `Output/ReadyToSend` folder.

## 📁 Project Structure

```text
Mail Merge Project/
│
├── main.py
│
├── Input/
│   ├── Names/
│   │   └── invited_names.txt
│   │
│   └── Letters/
│       └── starting_letter.txt
│
└── Output/
    └── ReadyToSend/
        ├── Alice.txt
        ├── Bob.txt
        └── Charlie.txt
```

## 🐍 Technologies Used

* Python
* File Handling
* List Comprehension
* String Methods
* `with open()` Context Manager

## 🔍 How the Program Works

### 1. Read the names

The program opens the names file and stores all names in a list.

```python
with open("Input/Names/invited_names.txt") as file:
    names = [name.strip() for name in file.readlines()]
```

`strip()` removes unnecessary spaces and newline characters from each name.

For example:

```text
Alice\n
Bob\n
Charlie\n
```

becomes:

```python
["Alice", "Bob", "Charlie"]
```

### 2. Read the letter template

The letter template is read using the `read()` method.

```python
with open("Input/Letters/starting_letter.txt") as file:
    personalized_letter = file.read()
```

The template contains a placeholder such as:

```text
Dear [name],

You are invited to my party!
```

### 3. Personalize the letter

For each name, the `[name]` placeholder is replaced with the actual name.

```python
result = personalized_letter.replace("[name]", name)
```

For example:

```text
Dear [name],
```

becomes:

```text
Dear Alice,
```

### 4. Create separate output files

A separate file is created for each person.

```python
with open("Output/ReadyToSend/" + name + ".txt", "w") as file:
    file.write(personalized_letter)
```

The `"w"` mode allows Python to create the file and write the personalized content into it.

For example:

```text
Output/ReadyToSend/Alice.txt
Output/ReadyToSend/Bob.txt
Output/ReadyToSend/Charlie.txt
```

## 🧠 Python Concepts Practiced

This project helps practice several important Python concepts:

* `open()`
* `with open()`
* `read()`
* `readlines()`
* `write()`
* `strip()`
* `replace()`
* List comprehension
* `for` loops
* File paths
* Reading and writing text files
* Creating files dynamically

## ▶️ How to Run

1. Make sure Python is installed.
2. Open the project in VS Code.
3. Make sure the required input files are present.
4. Run:

```bash
python main.py
```

5. Check the `Output/ReadyToSend` folder for the generated letters.

## 🎯 Purpose

This project demonstrates how Python can automate repetitive tasks involving files and text.

It is a beginner-friendly example of **file handling and automation in Python**.
