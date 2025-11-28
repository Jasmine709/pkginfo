# pkginfo — Python Command Line Package Info Tool

Project Duration: Oct 2024

A lightweight Python 3 command-line utility designed to parse and analyse a simple package list file.  
The tool supports listing installed packages, calculating total size, retrieving package details by name, and printing student information.

This project was originally developed as part of a coursework exercise, and is included here to demonstrate clean Python scripting, command-line argument parsing, modular design, and basic file handling.

## Features

### **1. List all installed packages (`-a`)**
Reads the provided file and prints all package names.

### **2. Show total size (`-s`)**
Sums the total size (in kilobytes) of all packages listed in the file.

### **3. Look up a package by name (`-l name`)**
Displays detailed information:
- Category  
- Package Name  
- Description  
- Size (kB)

### **4. Show student information (`-v`)**
Prints the student information defined in the script.

## Error Handling
The tool includes:
- Invalid option detection
- Missing argument detection
- File existence & readability checks
- Graceful “package not found” messages
