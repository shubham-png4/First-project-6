import random

class DataAnalyzer:
    def __init__(self):
        self.data = []
    
    def add_data(self, value):
        self.data.append(value)
    
    def get_statistics(self):
        if not self.data:
            return "No data available"
        
        return {
            'total': sum(self.data),
            'average': sum(self.data) / len(self.data),
            'min': min(self.data),
            'max': max(self.data),
            'count': len(self.data)
        }
    
    def display_report(self):
        stats = self.get_statistics()
        if isinstance(stats, dict):
            print("=" * 40)
            print("DATA ANALYSIS REPORT")
            print("=" * 40)
            print(f"Total: {stats['total']:.2f}")
            print(f"Average: {stats['average']:.2f}")
            print(f"Minimum: {stats['min']}")
            print(f"Maximum: {stats['max']}")
            print(f"Count: {stats['count']}")
            print("=" * 40)
        else:
            print(stats)

# Usage
analyzer = DataAnalyzer()
print("Enter numbers (type 'done' to finish):")

while True:
    try:
        user_input = input("> ")
        if user_input.lower() == 'done':
            break
        analyzer.add_data(float(user_input))
    except ValueError:
        print("Please enter a valid number!")

analyzer.display_report()