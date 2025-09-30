# Step 1: Ask for input
full_name = input("Enter your full name (First, Middle, Last): ")

# Step 2: Split input
first, middle, last = [part.strip() for part in full_name.split(",")]

# Step 3: Capitalize names properly
first = first.capitalize()
last = " ".join([word.capitalize() for word in last.split()])  # handles multi-word last names

# Step 4: Convert middle name to initial
middle_initial = middle[0].upper() + "."

# Step 5: Rearrange format
formatted_name = f"{last}, {first} {middle_initial}"

# Step 6: Display result
print("Formatted Name:", formatted_name)