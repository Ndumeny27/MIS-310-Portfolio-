def calcTuition(credits):
    if credits >= 12:
        return 20000
    elif credits >= 1:
        return 1200 + (1700 * credits)
    else:
        return 0  # handles 0 or negative credits


def main():
    credits = int(input("Enter number of credits: "))
    tuition = calcTuition(credits)
    print("Tuition for the semester: ${:,}".format(tuition))

# Run the program
main()