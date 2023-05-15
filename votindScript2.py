import math

# Function to calculate percentage


def calculate_percentage(num, total):
    return math.floor(num / total * 100)

# Function to print vote count and percentage


def print_results(candidate1, candidate2):
    total_votes = candidate1['votes'] + candidate2['votes']
    print(candidate1['name'], "received", candidate1['votes'], "votes, which is",
          calculate_percentage(candidate1['votes'], total_votes), "% of total votes")
    print(candidate2['name'], "received", candidate2['votes'], "votes, which is",
          calculate_percentage(candidate2['votes'], total_votes), "% of total votes")


# Initialize contestants and votes
contestant1 = input("Enter the name of 1st contestant: ")
contestant2 = input("Enter the name of 2nd contestant: ")

contestant1_votes = {'name': contestant1, 'votes': 0}
contestant2_votes = {'name': contestant2, 'votes': 0}

voter_id = [1, 2, 3, 4, 5]
number_of_voters = len(voter_id)

while True:
    if not voter_id:
        print("Voting Session is Over")
        if contestant1_votes['votes'] > contestant2_votes['votes']:
            print(contestant1, "has won the election with", calculate_percentage(
                contestant1_votes['votes'], number_of_voters), "% of total votes")
            break
        elif contestant2_votes['votes'] > contestant1_votes['votes']:
            print(contestant2, "has won the election with", calculate_percentage(
                contestant2_votes['votes'], number_of_voters), "% of total votes")
            break
        else:
            print("There was a tie between both contestants")
            break

    voter = int(input("Enter your Voter's Id: "))
    if voter in voter_id:
        print("You are eligible to vote")
        voter_id.remove(voter)
        print("---------------------------------------------------------------------")
        print("To vote for", contestant1, "press 1")
        print("To vote for", contestant2, "press 2")
        print("---------------------------------------------------------------------")
        vote = int(input("Cast Your Vote! ------ "))
        if vote == 1:
            contestant1_votes['votes'] += 1
            print("Thanks for voting", contestant1, "!")
        elif vote == 2:
            contestant2_votes['votes'] += 1
            print("Thanks for voting", contestant2, "!")
        else:
            print("Kindly Recheck Your Options")
    else:
        print("You are not eligible to Vote")

    # Print current vote count after each vote
    print_results(contestant1_votes, contestant2_votes)
