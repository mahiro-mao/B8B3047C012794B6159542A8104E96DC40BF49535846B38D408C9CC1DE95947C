import re

# Sample text containing email addresses
mtxt = "jox r.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com."

# Regex pattern to match valid email addresses
pattern = r'\b[\w.-]+@[A-Za-z]+\.[A-Za-z]{2,}(?:\.[A-Za-z]{2,})?\b'

# Find all valid email addresses
valid_emails = re.findall(pattern, mtxt)
print(valid_emails)

# Open and read the HTML file
with open("tabla.html", encoding="utf-8") as f:
    txt = f.read()

# Regex pattern to find Simpsons showtimes
pattern = r'<td class="svtTablaTime">\s*(\d+\.\d+)\s*</td>\s*<td.*?>\s*<h4.*?>\s*Simpsons\s*</h4>'

# Find all matches in the file
simpsons_showtimes = re.findall(pattern, txt)

# Print each showtime
for time in simpsons_showtimes:
    print("Simpsons airs at:", time)