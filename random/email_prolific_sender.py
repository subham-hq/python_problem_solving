"""
Extract the sender with the highest number of email messages from a mailbox file.
The program reads through each line, counts occurrences of email senders,
and prints the one with the highest frequency.
"""

filename = input("Enter file name: ")
if not filename:
    filename = ".txt" # Enter your txt file name here.

try:
    handle = open(filename)
except FileNotFoundError:
    print("File not found.")
    exit()

sender_counts = {}

for line in handle:
    if line.startswith("From "):
        email = line.split()[1]
        sender_counts[email] = sender_counts.get(email, 0) + 1

# Identify sender with highest message count
top_sender = max(sender_counts, key=sender_counts.get)
top_count = sender_counts[top_sender]

print(top_sender, top_count)
