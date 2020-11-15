
loanPrincipal = float(input("Enter the loan amount: "))
interestRate = float(input("Enter the interest rate in percent: "))/100
compoundPeriod = float(input("Enter the interest compounding period: "))
minimumPayment = float(input("Enter the minimum monthly payment: "))
additionalPayment = float(input("Enter the amount on top of the minimum payment you would like to make: "))


loanPrincipal2calculate = loanPrincipal

runningPrincipal_min = [loanPrincipal]
runningInterest_min = [0.0]
runningInterest_addit = [0.0]
runningPrincipal_addit = [loanPrincipal]
rValue = interestRate/compoundPeriod
totalInterest_min = 0.0
totalInterest_addit = 0.0

increasedPayment = minimumPayment + additionalPayment

#   minimum payment calculations
while loanPrincipal2calculate > 0:

    #minimum payment calculations
    if (loanPrincipal2calculate-minimumPayment) > 0:    #check to ensure repayment doesnt go negative
        #calculate next running value
        nextValue = ((1+rValue)*loanPrincipal2calculate)-minimumPayment
        runningPrincipal_min.append(nextValue)
        #calculate interest for this cycle
        runningInterest_min.append(rValue*loanPrincipal2calculate)

    else: #this condition runs on the last cycle of a repayment calculation
        #set running principle to 0 to show loan is paid off
        runningPrincipal_min.append(0)
        #calculate interest for this cycle
        runningInterest_min.append(rValue*loanPrincipal2calculate)

    #sums the total interest paid
    totalInterest_min += runningInterest_min[len(runningInterest_min)-1]


    #sets exit condition and prev value for next cycle
    loanPrincipal2calculate = runningPrincipal_min[len(runningPrincipal_min)-1]

print(runningPrincipal_min)
print(runningInterest_min)
print(totalInterest_min)


# reset loanPrinciple2calculate for additional payment calculations
loanPrincipal2calculate = loanPrincipal


#   additional payment calculations
while loanPrincipal2calculate > 0:
    if (loanPrincipal2calculate-increasedPayment) > 0:    #check to ensure repayment doesnt go negative
        #calculate next running value
        nextValue = ((1+rValue)*loanPrincipal2calculate)-increasedPayment
        runningPrincipal_addit.append(nextValue)
        #calculate interest for this cycle
        runningInterest_addit.append(rValue*loanPrincipal2calculate)

    else: #this condition runs on the last cycle of a repayment calculation
        #set running principle to 0 to show loan is paid off
        runningPrincipal_addit.append(0)
        #calculate interest for this cycle
        runningInterest_min.append(rValue*loanPrincipal2calculate)

    #sums the total interest paid
    totalInterest_addit += runningInterest_addit[len(runningInterest_addit)-1]

    #sets exit condition and prev value for next cycle
    loanPrincipal2calculate = runningPrincipal_addit[len(runningPrincipal_addit)-1]


print(runningPrincipal_addit)
print(runningInterest_addit)
print(totalInterest_addit)
