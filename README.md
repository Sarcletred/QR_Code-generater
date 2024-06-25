# QR_Code-generater
This project is a simple QR code generator application built using Python's tkinter library for the graphical user interface (GUI) and pyqrcode library for generating QR codes. The application allows users to enter text data, generate a corresponding QR code, display the QR code within the application, and clear the input data and QR code.

Project Structure
Libraries and Initialization:

Import necessary libraries (pyqrcode for QR code generation and tkinter for GUI).
Initialize the main application window (root).
Define Functions:

gen_qr(): Generates the QR code from user input, converts it to an XBM image, and updates the display.
clear(): Clears the input field and resets the QR code display.
Create and Configure Widgets:

Labels for the application heading and input instructions.
Entry widget for user input.
Buttons for generating and clearing the QR code.
Label to display the generated QR code.
Label to display the message about the entered data.
Layout Management:

Use the pack method for arranging the widgets with padding for better visual spacing.
Set the main window's size and background color for a consistent look and feel.
Main Loop:

Run the tkinter main event loop to start the application.
![Screenshot (101)](https://github.com/Sarcletred/QR_Code-generater/assets/135229520/38300156-f6ba-4d7d-843e-9f5986773cbc)
![Screenshot (102)](https://github.com/Sarcletred/QR_Code-generater/assets/135229520/f70797ec-33ea-4d29-9ff0-f27cb6b1a317)

