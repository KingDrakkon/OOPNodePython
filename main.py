from account import (
    SavingsAccount, checkingAccount, HighInterestSavingsAccount, OverDraftCheckingAccount, PremiumOverdraftCheckingAccount
)


def main():
    # Create and interact with account
    savings = SavingsAccount("12345", "Bob Smith", 1000)
    premium = PremiumOverdraftCheckingAccount("67890", "Alice Johnson", 2000)

    # perform some operation
    savings.deposit(500)
    premium.withdraw(2500)
    premium.deposit(1000)

    # display balances
    savings.display_balance()
    premium.display_balance()

if __name__ == "__main__":
    main()