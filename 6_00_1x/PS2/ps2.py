#!/usr/bin/python

def main():
    # Test suite
    test_remaining_balance = False
    test_fixed_pmt = False
    test_fixed_pmt_bisection = True

    if test_remaining_balance:
        balance, annualInterestRate, monthlyPaymentRate = (42, .2, .04)
        remaining_balance(balance, annualInterestRate, monthlyPaymentRate)

        balance, annualInterestRate, monthlyPaymentRate = (484, .2, .04)
        remaining_balance(balance, annualInterestRate, monthlyPaymentRate)

    if test_fixed_pmt:
        balance, annualInterestRate = (3329, .2)
        fixed_pmt(balance, annualInterestRate)

        balance, annualInterestRate = (4773, .2)
        fixed_pmt(balance, annualInterestRate)

        balance, annualInterestRate = (3926, .2)
        fixed_pmt(balance, annualInterestRate)

    if test_fixed_pmt_bisection:
        balance, annualInterestRate = (320000, .2)
        fixed_pmt_bisection(balance, annualInterestRate)

        balance, annualInterestRate = (999999, .18)
        fixed_pmt_bisection(balance, annualInterestRate)

    return 0


def remaining_balance(balance, annualInterestRate, monthlyPaymentRate):
    '''
    Calculates the remaining balance on a credit card at the end of 12 months
    balance: int or float
    annualInterestRate: percent (decimal)
    monthlyPaymentRate: percent (decimal)
    Output: prints and returns remaining balance
    '''
    monthlyInterestRate = annualInterestRate / 12

    for month in range(1, 13):
        minimumPayment = monthlyPaymentRate * balance
        balance -= minimumPayment
        interestPayment = monthlyInterestRate * balance
        balance += interestPayment
        # print('Month {} Remaining balance : {}'.format(month, round(balance,2)))

    print('Remaining balance: {}'.format(round(balance, 2)))
    return balance


def fixed_pmt(balance, annualInterestRate):
    '''
    Calculates the fixed payment necessary to pay a credit card balance off within a year, with given annual interest rate.
    balance: int or float
    annualInterestRate: percent (decimal)
    Output: prints and returns the fixed payment
    '''
    monthlyInterestRate = annualInterestRate / 12

    for pmtGuess in range(10, balance, 10):
        # Reset test_balance for new test case
        test_balance = balance
        # Simulate paying down test_balance in a year
        for month in range(1, 13):
            test_balance -= pmtGuess
            interestPayment = monthlyInterestRate * test_balance
            test_balance += interestPayment
        # print('Remaining balance: {} for monthly pmt of {}'.format(round(test_balance, 2), pmtGuess))

        if test_balance <= 0:
            break

    print('Lowest Payment: {}'.format(pmtGuess))
    return pmtGuess


def fixed_pmt_bisection(balance, annualInterestRate):
    '''
    Uses bisection search to calculate the fixed payment necessary to pay a credit card balance off within a year, with given annual interest rate.
    balance: int or float
    annualInterestRate: percent (decimal)
    Output: prints and returns the fixed payment
    '''
    monthlyInterestRate = annualInterestRate / 12
    lower = balance / 12
    upper = (balance * (1 + monthlyInterestRate)**12 ) / 12
    pmtGuess = (lower + upper) / 2

    while upper - lower >= 0.01:
        # Reset test_balance for new test case
        test_balance = balance
        # Simulate paying down test_balance in a year
        for month in range(1, 13):
            test_balance -= pmtGuess
            interestPayment = monthlyInterestRate * test_balance
            test_balance += interestPayment

        if test_balance < 0:
            # Payments too high
            upper = pmtGuess
            pmtGuess = (upper + lower) / 2
        else:
            # Payments too low
            lower = pmtGuess
            pmtGuess = (upper + lower) / 2

    print('Lowest Payment: {}'.format(round(pmtGuess, 2)))
    return pmtGuess


if __name__ == '__main__':
    main()
