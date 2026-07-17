
# Banking Loan Eligibility
salary = float(input("Enter monthly salary (₹): "))
credit_score = int(input("Enter credit score: "))
if salary >= 50000 and credit_score >= 750:
    decision = "Loan Approved"
elif salary >= 30000 and 650 <= credit_score < 750:
    decision = "Loan Approved with High Interest"
else:
    decision = "Loan Rejected"
print("\n------ LOAN ELIGIBILITY RESULT ------")
print(f"Salary       : ₹{salary:.2f}")
print(f"Credit Score : {credit_score}")
print(f"Decision     : {decision}")