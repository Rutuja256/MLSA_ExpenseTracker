# Give code to build Expense tracker plus . Add features 1.Add expense (amount + category) and 2. Show  total expence  . Add Advanced festures like:category wisw summary,daily/weekly report, display simple text based chart

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        self.expenses.append({'amount': amount, 'category': category})

    def total_expense(self):
        return sum(expense['amount'] for expense in self.expenses)

    def category_summary(self):
        summary = {}
        for expense in self.expenses:
            category = expense['category']
            amount = expense['amount']
            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount
        return summary

    def daily_report(self):
        report = {}
        for expense in self.expenses:
            date = expense.get('date', 'Unknown')
            amount = expense['amount']
            if date in report:
                report[date] += amount
            else:
                report[date] = amount
        return report

    def weekly_report(self):
        report = {}
        for expense in self.expenses:
            week = expense.get('week', 'Unknown')
            amount = expense['amount']
            if week in report:
                report[week] += amount
            else:
                report[week] = amount
        return report

    def display_chart(self):
        category_summary = self.category_summary()
        for category, amount in category_summary.items():
            print(f"{category}: {'#' * int(amount / 10)} ({amount})")
        



tracker = ExpenseTracker()
tracker.add_expense(50, 'Food') 
tracker.add_expense(30, 'Transport')
tracker.add_expense(20, 'Entertainment')  
tracker.display_chart()