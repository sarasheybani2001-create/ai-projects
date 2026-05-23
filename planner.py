import math

def get_subjects():
    subjects = []

    count = int(input("How many subjects? "))

    for i in range(count):
        name = input(f"\nSubject {i+1} name: ")
        difficulty = int(input("Difficulty (1-5): "))
        priority = int(input("Priority (1-5): "))

        subjects.append({
            "name": name,
            "difficulty": difficulty,
            "priority": priority
        })

    return subjects


def calculate_weight(subject):
    return subject["difficulty"] * 0.6 + subject["priority"] * 0.4


def generate_plan(subjects, days):

    # sort by importance
    subjects = sorted(subjects, key=calculate_weight, reverse=True)

    plan = {f"Day {i+1}": [] for i in range(days)}

    index = 0

    for subject in subjects:
        repeat = math.ceil(calculate_weight(subject))

        for _ in range(repeat):
            day = f"Day {(index % days) + 1}"
            plan[day].append(subject["name"])
            index += 1

    return plan


def print_plan(plan):
    print("\n🖤 Your Study Plan:\n")

    for day, tasks in plan.items():
        print(day)

        if not tasks:
            print("  Rest / Light Review")
        else:
            for task in tasks:
                print(f"  - {task}")

        print()


def study_tips():
    print("Tips:")
    print("- Study in 45-60 min focused sessions")
    print("- Take 10 min breaks")
    print("- Start with hardest subject first")
    print("- Don’t overwork — consistency > intensity\n")


def main():
    print("AI Study Planner\n")

    subjects = get_subjects()
    days = int(input("\nHow many days until exam? "))

    plan = generate_plan(subjects, days)

    print_plan(plan)
    study_tips()


main()