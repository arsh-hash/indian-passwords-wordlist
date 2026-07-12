from datetime import date, timedelta

start = date(1950, 1, 1)
end = date(2050, 12, 31)

primary = []
secondary = []

current = start
while current <= end:
    d = f"{current.day:02d}"
    m = f"{current.month:02d}"
    y = f"{current.year:04d}"

    # Primary: DDMMYYYY, MMDDYYYY, YYYYMMDD
    primary.append(f"{d}{m}{y}")
    primary.append(f"{m}{d}{y}")
    primary.append(f"{y}{m}{d}")

    # Secondary: YYYYDDMM, DDYYYYMM, MMYYYYDD
    secondary.append(f"{y}{d}{m}")
    secondary.append(f"{d}{y}{m}")
    secondary.append(f"{m}{y}{d}")

    current += timedelta(days=1)

output_path = "dates_wordlist.txt"
with open(output_path, "w") as f:
    for entry in primary:
        f.write(entry + "\n")
    for entry in secondary:
        f.write(entry + "\n")

total = len(primary) + len(secondary)
print(f"[+] Output file   : {output_path}")