#!/bin/bash

# Function to print in color
print_color() {
    color=$1
    message=$2
    echo -e "\033[${color}m${message}\033[0m"
}

# Update and upgrade system
print_color "93" "Starting update and upgrade..."
pkg update -y && pkg upgrade -y
print_color "92" "System updated and upgraded successfully!"

# Install Python
print_color "93" "Installing Python..."
pkg install python -y
print_color "92" "Python installed successfully!"

# Install pip
print_color "93" "Installing pip..."
pkg install python-pip -y
print_color "92" "pip installed successfully!"

# Install requests module
print_color "93" "Installing requests module..."
pip install requests
print_color "92" "requests module installed successfully!"

# Install git (optional but recommended for version control)
print_color "93" "Installing git..."
pkg install git -y
print_color "92" "git installed successfully!"

# End of script
print_color "93" "All required packages have been installed successfully!"
