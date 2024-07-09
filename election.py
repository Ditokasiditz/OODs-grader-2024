print("*** Election ***")


voter_num = int(input("Enter a number of voter(s) : "))
voter_list = list(map(int, input().split()))
voter_list.sort()
valid_votes = [num for num in voter_list if 1 <= num <= 20]

if not valid_votes:
    print("*** No Candidate Wins ***")
else:
    counts = {}
    for num in valid_votes:
        counts[num] = counts.get(num, 0) + 1

    max_votes = max(counts.values())
    winners = [candidate for candidate, votes in counts.items() if votes == max_votes]

    if winners:
        print(*winners)
    else:
        print("*** No Candidate Wins ***")