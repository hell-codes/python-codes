#takes user age and eligible to vote or not
def can_vote(age):
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

can_vote(20)
can_vote(16)
