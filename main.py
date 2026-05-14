# Run this file directly in VS Code or from the terminal with:
# python main.py


def workout_level(average):
    """Determine proficiency level based on average score."""

    if 1 <= average <= 1.69:
        return "1"
    elif 1.7 <= average <= 1.99:
        return "2"
    elif 2 <= average <= 2.69:
        return "3"
    elif 2.7 <= average <= 2.99:
        return "4"
    elif average == 3:
        return "5"
    else:
        return (
            "Your average should be between 1 and 3. "
            "Please confirm you have entered your skill levels correctly and try again."
        )


def show_workings(
    total_skills,
    working_below,
    working_at_initial,
    working_at,
    working_above_initial,
    working_above,
    weighted_total,
    average,
):
    """Display how the proficiency level was calculated."""

    print("\n------------------------")
    print(
        f"Based on the values you entered, you are being assessed "
        f"against a total of {total_skills} skills:"
    )

    print(f"You have {working_below} skills below the job level requirement")
    print(f"You have {working_at_initial} skills at the job level requirement")
    print(f"You have {working_above_initial} skills above the job level requirement")

    print(
        "\nThe number of skills where you are working at the expected level "
        "is multiplied by two, and the number of working above skills "
        "is multiplied by three."
    )

    print("\nWith these weightings applied, your skill levels now look like this:")
    print(f"Working below - {working_below} (this remains unchanged)")
    print(f"Working at - {working_at}")
    print(f"Working above - {working_above}")

    print(f"\nThis leaves a total of {weighted_total}.")
    print(
        f"The average of your weighted total skills is {average}, "
        f"which corresponds to proficiency level {workout_level(average)}"
    )


def get_skill_inputs():
    """Collect and confirm user input."""

    while True:
        try:
            working_below = int(
                input(
                    "Enter the number of skills where you are working "
                    "below your expected level: "
                )
            )

            working_at_initial = int(
                input(
                    "Enter the number of skills where you are working "
                    "at your expected level: "
                )
            )

            working_above_initial = int(
                input(
                    "Enter the number of skills where you are working "
                    "above your expected level: "
                )
            )

            total_skills = (
                working_below
                + working_at_initial
                + working_above_initial
            )

            confirm_total = input(
                f"\nYou have {total_skills} skills.\n"
                "Please confirm that this is correct by entering Y below.\n"
                "If this is not correct, enter N or another letter of your choice "
                "and you will be able to enter your skills again.\n"
            )

            if confirm_total.upper() == "Y":
                return (
                    working_below,
                    working_at_initial,
                    working_above_initial,
                    total_skills,
                )

        except ValueError:
            print("\nInvalid input. Please enter whole numbers only.\n")


def main():
    """Main program."""

    (
        working_below,
        working_at_initial,
        working_above_initial,
        total_skills,
    ) = get_skill_inputs()

    # Apply weightings
    working_at = working_at_initial * 2
    working_above = working_above_initial * 3

    weighted_total = (
        working_below
        + working_at
        + working_above
    )

    average = round(weighted_total / total_skills, 2)

    # Display results
    print(f"\nYour average is {average}")
    print(f"You are working at level {workout_level(average)}")

    # Optionally show workings
    confirm_display_workings = input(
        "\nIf you want to see how your proficiency level was worked out, enter Y.\n"
        "If you do not want to see this, enter N or another letter of your choice.\n"
    )

    if confirm_display_workings.upper() == "Y":
        show_workings(
            total_skills,
            working_below,
            working_at_initial,
            working_at,
            working_above_initial,
            working_above,
            weighted_total,
            average,
        )


# Run the program
if __name__ == "__main__":
    main()
