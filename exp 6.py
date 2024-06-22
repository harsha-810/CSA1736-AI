class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment
        self.num_rows = len(environment)
        self.num_cols = len(environment[0])
        self.row = 0
        self.col = 0
        self.performance_score = 0

    def clean(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.environment[row][col] == 'D':
                    self.environment[row][col] = 'C'  # Clean the cell
                    self.performance_score += 1  # Increment performance score

                self.print_environment(row, col)

        print("Cleaning complete!")
        print(f"Performance score: {self.performance_score}")

    def print_environment(self, current_row, current_col):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if r == current_row and c == current_col:
                    print(f"[{self.environment[r][c]}]", end=' ')
                else:
                    print(f" {self.environment[r][c]} ", end=' ')
            print()
        print()

# Example usage:
if __name__ == "__main__":
    # Define an example environment (5x5 grid)
    environment = [
        ['C', 'D', 'C', 'C', 'D'],
        ['C', 'C', 'D', 'C', 'C'],
        ['D', 'C', 'C', 'D', 'C'],
        ['C', 'C', 'D', 'C', 'C'],
        ['D', 'C', 'C', 'D', 'C']
    ]

    # Create a Vacuum Cleaner agent
    vacuum_cleaner = VacuumCleaner(environment)

    print("Initial environment:")
    vacuum_cleaner.print_environment(-1, -1)  # Print initial environment without highlighting

    # Start cleaning
    vacuum_cleaner.clean()
