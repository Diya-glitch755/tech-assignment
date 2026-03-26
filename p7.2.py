import java.util.Scanner;

class BankAccount {
    double balance;

    // Constructor
    BankAccount(double initialBalance) {
        balance = initialBalance;
    }

    // Display balance
    void displayBalance() {
        System.out.println("Current Balance: " + balance);
    }

    // Deposit amount
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Amount Deposited Successfully");
        } else {
            System.out.println("Invalid Amount");
        }
    }

    // Withdraw amount
    void withdraw(double amount) {
        if (amount > balance) {
            System.out.println("Insufficient Balance");
        } else if (amount <= 0) {
            System.out.println("Invalid Amount");
        } else {
            balance -= amount;
            System.out.println("Withdrawal Successful");
        }
    }
}

public class BankMenu {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Initial Balance: ");
        double initial = sc.nextDouble();

        BankAccount account = new BankAccount(initial);

        int choice;

        do {
            System.out.println("\n--- BANK MENU ---");
            System.out.println("1. Display Balance");
            System.out.println("2. Deposit Amount");
            System.out.println("3. Withdraw Amount");
            System.out.println("4. Exit");
            System.out.print("Enter choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    account.displayBalance();
                    break;

                case 2:
                    System.out.print("Enter amount to deposit: ");
                    double dep = sc.nextDouble();
                    account.deposit(dep);
                    break;

                case 3:
                    System.out.print("Enter amount to withdraw: ");
                    double wd = sc.nextDouble();
                    account.withdraw(wd);
                    break;

                case 4:
                    System.out.println("Thank you!");
                    break;

                default:
                    System.out.println("Invalid Choice");
            }

        } while (choice != 4);
    }
}
