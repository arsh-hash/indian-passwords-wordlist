# Indian Passwords Wordlist

A collection of password lists made for password-guessing during **authorized** security testing (like CTFs, HTB/THM labs ).

These lists are focused on password patterns common in India — names, dates of birth, and mobile numbers — instead of generic lists like RockYou.

## What's Inside

```
indian-passwords-wordlist/
├── 1. Build on prebuild lists/          → lists built from other public wordlists
├── 2. extracted from rock you/          → passwords picked out from RockYou which are common across people besides their country 
├── 3. passwords based on DOB From 1950 to 2050/   → passwords made from birth dates
├── 4. Passwords list based on mobile numbers/     → passwords made from indian phone numbers
└── README.md
```

Each folder is just `.txt` files with passwords, one per line. Some folders may also have a Python script used to generate the list.

## How to Download It

**Clone with Git**
```bash
git clone https://github.com/arsh-hash/indian-passwords-wordlist.git
cd indian-passwords-wordlist
```

## How to Use the Lists

You just point your tool at one of the `.txt` files. Here are some common examples:

**Hashcat (cracking password hashes)**
```bash
hashcat -m 0 hashes.txt "2. extracted from rock you/rockyou_indian.txt"
```

**John the Ripper**
```bash
john --wordlist="3. passwords based on DOB From 1950 to 2050/dob_list.txt" hashes.txt
```

**Hydra (guessing login passwords online)**
```bash
hydra -l admin -P "4. Passwords list based on mobile numbers/mobile_list.txt" ssh://target-ip
```

**Burp Suite**
Load any `.txt` file as a payload list under Intruder.

*(File names above are examples — check the folder to see the real file name.)*


## Important: Use It the Right Way

- Only use this on systems you **own** or have **written permission** to test.
- Using this against someone else's account or system without permission is illegal.
- This is meant for learning, CTFs, and authorized security testing only.

## Want to Contribute?

Feel free to add new password patterns (like PIN codes or common Indian words). Just keep the list clean (no duplicates) and add it to the right folder.
