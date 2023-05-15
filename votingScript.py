## contestant details
contestant1 = input("Enter the name of !st contestant: ")
contestant2 = input("Enter the name of 2nd contestant: ")

## initial vote count to zero
contestant1_votes = 0
contestant2_votes = 0

voter_id = [1,2,3,4,5]
number_of_voters = len(voter_id)

while True:
    if voter_id == []:
        print("Voting Session is Over")
        if contestant1_votes > contestant2_votes:
            percentage = (contestant1_votes / contestant2_votes) * 100
            print(contestant1, "has won the election with ",percentage, "%" "of votes")
            break
        elif contestant2_votes > contestant1_votes:
            percentage = (contestant2_votes / contestant1_votes) * 100
            print(contestant2, "has won the election with ",percentage, "%" "of votes")
            break
        else: 
            print("There was a tie between both contestants")
            break
    
    voter = int(input("Enter your Voter's Id: "))
    if voter in voter_id:
        print("You are eligible to vote")
        voter_id.remove(voter) ## remove the id so that the person can't vote again
        print("---------------------------------------------------------------------")
        print("To vote for" ,contestant1, "press 1")
        print("To vote for" ,contestant2, "press 2") 
        print("---------------------------------------------------------------------")
        vote = int(input("Cast Your Vote ! ------ "))
        if vote == 1:
            contestant1_votes +=1
            print ("Thanks for voting" ,contestant1,"!")
        elif vote == 2: 
            contestant2_votes +=1
            print ("Thanks for voting" ,contestant2,"!")
        elif vote > 2:
            print("Recheck Your Options")
    else:
        print("You are not eligible to Vote")
