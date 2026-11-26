import os

# Read the funny update note (exactly one line, max 160 chars)
note = "v1.0 - Fixed: hair grows faster when you need it least; Added: ability to forget why you walked into a room for 3 seconds"

# Ensure output directory exists
os.makedirs('output', exist_ok=True)

# Write only the patch note, no extra lines or timestamps
with open('output/entry.txt', 'w') as f:
    f.write(note)

print("Patch notes written successfully!")
