def main():
    # Function to set the daily steps goal
    def set_steps_goal():
        goal = int(input("Enter your daily steps goal: "))
        return goal

    # Function to record steps for 7 days
    def record_daily_steps():
        total_steps = 0
        for day in range(1, 8):
            steps = int(input(f"Enter steps for day {day}: "))
            total_steps = total_steps + steps
        return total_steps

    # Function to evaluate weekly performance
    def evaluate_weekly_performance(goal, total_steps):
        average_steps = total_steps / 7
        print(f"\nYour average daily steps: {average_steps:.2f}")

        if average_steps > goal:
            print(f"You exceeded your daily steps goal of {goal} steps!")
        elif average_steps == goal:
            print(f"You met your daily steps goal of {goal} steps!")
        else:
            print(f"You did not meet your daily steps goal of {goal} steps.")

    # Program flow
    goal = set_steps_goal()
    total_steps = record_daily_steps()
    evaluate_weekly_performance(goal, total_steps)


# Run the program
main()