# OPUS - An elegant book-tracker app 📖
Created by Kewbish, development beginning February 2020.  
Made with [Kivy](https://kivy.org) and Python.  
## Packaging
Due to issues with equipment (I have a Windows machine and use an iPhone - quirky, I know.), I won't be able to package this as an .ipa. Therefore, I've also decided to leave packaging up to the end user.  
Note: if you see this, and you'd like to help with packaging (i.e. have a Mac and are willing to help), please send me an email at [kewbish@gmail.com](mailto:kewbish@gmail.com). I'd be happy to work with you!  
Documentation for packaging can be found [on the Kivy site](https://kivy.org/doc/stable/guide/packaging.html).  
### Getting the files
Find the `Clone or Download` button on this repository, and select `Download as ZIP`. Extract the files.  
Ensure `python` and `pip` are installed, and that you are somewhat familiar with the command-line.
### Before packaging
Before packaging, please change two parameters in the opus.py file.  
```
def send_email_button(self):
        email = "mymail@mail.com"  # Change this to your email.
        password = "verysecurepassword"  # Change this to your password.
```
These will need to be set to the email and password of a valid user. If you're unsure about the security of this, please audit the code yourself - there are no malicious data-savers.
