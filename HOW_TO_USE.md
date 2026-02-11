How to Use the Contact System
=============================

This guide walks through each option provided by `main.py`, including example prompts and outputs. Run all commands from the `Mobile-Phone-Number-Contact-System` directory.

Launching the Program
---------------------
```
python main.py
```
The script greets you with:
```
What do you want to do? add or find:
```

Adding a New Contact
--------------------
1. Type `add` and press Enter.
2. Respond to the prompts:
   - Contact name (full name).
   - Country code (e.g., `+1`, `+92`).
   - Phone number (digits only).
   - Nickname (used as the filename suffix).
3. The program confirms that the contact was saved and creates a file named `contacts.<nickname>.txt`. Example contents:
   ```
   Name: Alice Johnson
   Country Code: +1
   Number: 5551234567
   ```

Finding an Existing Contact
---------------------------
1. At the main prompt, type `find`.
2. Enter the nickname associated with the contact file (case-insensitive).
3. The program displays the stored details from `contacts.<nickname>.txt`.

Updating Contact Information
----------------------------
After viewing a contact, the program asks:
```
Do you want to change the contact data? yes or no:
```
- Typing `yes` opens the same prompts as when adding a contact, overwriting the existing file.
- Typing `no` leaves the file unchanged.

Continuing or Exiting
---------------------
At the end of each cycle, you are asked:
```
Do you want to use our program? yes or no:
```
- Typing `yes` restarts the process so you can add or find another contact.
- Typing `no` exits the application with a farewell message.

Tips
----
- Keep nicknames unique to avoid overwriting other contacts.
- Contact files are plain text, so you can back them up or edit them manually if needed.
- If an incorrect nickname is entered, the script raises a `FileNotFoundError`. Re-run the program and double-check the nickname.
