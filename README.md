Mobile Phone Number Contact System
==================================

A simple command-line contact book built with Python. It lets you add new phone contacts, retrieve them by nickname, and update existing entries. Contacts are stored in plain-text files named after each contact's nickname, making the data portable and easy to inspect.

Project Highlights
------------------
- Add new contacts with name, country code, and phone number.
- Retrieve saved contacts by their nickname.
- Update the details of an existing contact after reviewing them.
- Looping menu so you can manage multiple contacts in a single session.

Prerequisites
-------------
- Python 3.8 or higher.
- Operating system with a terminal or command prompt (Windows, macOS, Linux).

Getting Started
---------------
1. Clone or download this repository.
2. Open a terminal in the `Mobile-Phone-Number-Contact-System` directory.
3. Run the program:
   ```
   python main.py
   ```

Usage Overview
--------------
The application prompts you to choose between adding a contact or finding an existing one. When you save a contact, its data is written to `contacts.<nickname>.txt`. You can review and edit the contact after retrieval. For a detailed walkthrough with screenshots and example input/output, see `HOW_TO_USE.md`.

Folder Structure
----------------
- `main.py`: Main CLI script that handles user interaction and file I/O.
- `contacts.<nickname>.txt`: Individual files generated for each saved contact (created at runtime).
- `HOW_TO_USE.md`: Step-by-step usage guide.

Contributing
------------
1. Fork the repository and create a feature branch.
2. Apply your changes and add descriptive comments where logic is non-obvious.
3. Test your updates by running `python main.py`.
4. Open a pull request summarizing the changes and testing steps.

License
-------
This project is provided as-is without a specific license. Feel free to adapt it for personal or educational use.
