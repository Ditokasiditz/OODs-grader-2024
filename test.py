number_vote = int(input("Enter the number of voter(s) : "))

vote_list = [int(e) for e in input("Enter the votes separated by spaces: ").split()]

# Filter the valid votes between 1 and 20
valid_votes = [vote for vote in vote_list if 1 <= vote <= 20]

# Create a dictionary to store the frequency of each vote
frequency_dict = {}

# Populate the dictionary with vote counts
for vote in valid_votes:
    if vote in frequency_dict:
        frequency_dict[vote] += 1
    else:
        frequency_dict[vote] = 1

# Find the maximum frequency
max_frequency = max(frequency_dict.values(), default=0)

# Find all numbers with the maximum frequency
most_frequent_numbers = [num for num, freq in frequency_dict.items() if freq == max_frequency]

# Sort the most frequent numbers in descending order
most_frequent_numbers.sort(reverse=True)

# Print the result
if most_frequent_numbers:
    print(" ".join(map(str, most_frequent_numbers)))
else:
    print("*** No Candidate Wins ***")
