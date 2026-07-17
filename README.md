# Indian Passwords Wordlist

A curated collection of password wordlists tailored for **India-specific brute-force and dictionary attack engagements** during authorized penetration tests, red team assessments, and CTF challenges. Unlike generic lists (RockYou, SecLists), this repo focuses on password patterns common among Indian users — names, DOB formats, and mobile-number-based passwords.

## Why This Exists

Generic wordlists give broad coverage but low hit-rate against regionally-influenced password habits. This project narrows the search space by generating and curating lists based on:

- Common Indian names, festivals, and cultural terms
- Date-of-birth patterns (a widely reused password base in India)
- Mobile number based passwords (10-digit patterns are frequently reused as-is or with minor suffixes)
- Filtered/extracted entries from RockYou relevant to Indian usage

Smaller, targeted wordlists = faster cracking and lower noise during time-boxed engagements (OSCP-style labs, CTFs, or client pentests with rate-limiting/lockout policies).

## Repository Structure

```
indian-passwords-wordlist/
├── 1. Build on prebuild lists/          # Lists derived/refined from existing public wordlists
├── 2. extracted from rock you/          # Subset of RockYou filtered for Indian-relevant entries
├── 3. passwords based on DOB From 1950 to 2050/   # DOB-pattern generated passwords (DDMMYYYY, MMDDYY, etc.)
├── 4. Passwords list based on mobile numbers/      # Mobile-number-derived password patterns
└── README.md
```

> Note: generator scripts are Python. If a folder contains both `.py` generators and `.txt` output lists, the script builds the corresponding list programmatically (useful for regenerating with a custom range/seed rather than storing huge static files).

## Usage

### With Hydra (online brute force)
```bash
hydra -l admin -P "3. passwords based on DOB From 1950 to 2050/dob_list.txt" ssh://<target>
```

### With John the Ripper / Hashcat (offline cracking)
```bash
hashcat -m 0 hashes.txt "2. extracted from rock you/indian_rockyou.txt"
john --wordlist="4. Passwords list based on mobile numbers/mobile_passwords.txt" hashes.txt
```

### With Burp Suite Intruder
Load the relevant `.txt` file as a payload set for credential-stuffing / login brute-force tests on web app assessments.

### Regenerating a list (if a Python generator is included)
```bash
python3 gen_dob_list.py --start 1950 --end 2050 --format DDMMYYYY -o dob_list.txt
```
(Adjust script name/args to match the actual file in that folder.)

## Recommended Workflow

1. Start with the smallest, most targeted list (DOB or mobile-based) before falling back to the full RockYou-derived set — reduces lockout risk on accounts with attempt limits.
2. Combine with tools like `cewl` or OSINT-gathered names/DOBs from the target to build a custom mutated list (`hashcat` rules or `mentalist`) for even higher hit rates.
3. Always throttle requests (`hydra -t`, Burp Intruder resource pool) to avoid tripping WAF/IDS during authorized tests.

## Legal / Ethical Use Disclaimer

This wordlist is intended **strictly for authorized security testing** — penetration tests with signed scope/ROE, bug bounty programs, CTFs, and personal lab environments (HTB, THM, etc.).

- Do **not** use this against any system you do not own or have explicit written authorization to test.
- Unauthorized access attempts are illegal under laws such as India's IT Act, 2000 (Section 66) and equivalent legislation elsewhere.
- The author(s) assume no liability for misuse.

## Contributing

PRs adding new pattern categories (e.g., vehicle registration numbers, PIN codes, common Hindi/regional transliterated words) are welcome. Please keep lists deduplicated and sorted, and note the generation methodology in the folder.

## License

Specify a license here (e.g., MIT) if you intend this for public/OSS use — currently unspecified in the repo.
