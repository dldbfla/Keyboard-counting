# Keyboard-counting
Keyboard counting(Currently only w,a,s,d,spacebar )


![스크린샷 2024-03-05 225824](https://github.com/dldbfla/Keyboard-counting/assets/89433437/4a343f1c-42b6-4ae8-952b-6648b95eaf32)

This code is a program that uses tkinter to detect keyboard events, counting the number of times a particular key is pressed and released.

The libraries you need to install are tkinter and keyboard. tkinter is a default library in Python, so you don't need to install it separately. However, the keyboard library needs to be installed separately. The keyboard library can be installed with pip. You can install it using the command below

 ``` 
pip install keyboard
 ``` 

Note that this code requires Python version 3.x to run, and you may need to run the program as administrator to detect keyboard events. Also, additional settings may be required depending on the operating system you run the code on to accurately detect keyboard events.


The code has the ability to count the number of times the 'w', 'a', 's', 'd', and 'space' keys on the keyboard are pressed and released, and display the values on the button. The background color of the button will turn gray for a short time as the number of keys pressed increases, and then return to its original color after 0.1 seconds.


When you run this code, the tkinter window will open, and each time the 'w', 'a', 's', 'd', and 'space' keys are pressed and released, the button will update and display the number of times that key was pressed.



Note that this code uses the keyboard library to detect keyboard events, and tkinter to create the GUI window and display the buttons.

