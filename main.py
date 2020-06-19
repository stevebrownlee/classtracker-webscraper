import csv
from Student import Student
from replit import get_replit_submissions, find_student_exercises
from codecademy import scrape_codecademy
from profiles import get_profiles


def main():
    # Get name, replit URL and Codecademy URL from profile submission
    student_profiles = get_profiles()
    student_profiles.sort(key=lambda s: s.name.split(" ")[0])

    # Get all repl.it submissions from Google sheet
    all_submitted_exercises = get_replit_submissions(student_profiles)

    # Calculate all pre-work percentages from repl.it and Codecademy
    calculate_percentages(student_profiles, all_submitted_exercises)

    # Export data to students.csv
    export_data_to_csv(student_profiles)


def calculate_percentages(student_profiles, all_submitted_exercises):
    for student in student_profiles:
        # Determine Codecademy precentage
        student.codecademy_percent = scrape_codecademy(
            student.name, student.codecademy_profile) or 0

        # Determine repl.it percentages
        find_student_exercises(all_submitted_exercises, student)

        print(student)


def export_data_to_csv(student_profiles):
    with open('scores.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Student",
                         "repl.it variables intro",
                         "repl.it arrays intro",
                         "repl.it objects intro",
                         "repl.it functions intro",
                         "repl.it conditions",
                         "repl.it iteration",
                         "repl.it functions",
                         "Codecademy"])
        for student in student_profiles:
            writer.writerow([student.name,
                            f'{student.intro_variables_percent:.1f}',
                            f'{student.intro_iteration_percent:.1f}',
                            f'{student.intro_objects_percent:.1f}',
                            f'{student.intro_functions_percent:.1f}',
                            f'{student.condition_percent:.1f}',
                            f'{student.iteration_percent:.1f}',
                            f'{student.function_percent:.1f}',
                            f'{student.codecademy_percent}'])


if __name__ == "__main__":
    main()
