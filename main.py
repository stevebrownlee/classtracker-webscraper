import csv
from Student import Student
from replit import get_replit_submissions, find_student_exercises
from codecademy import scrape_codecademy
from profiles import get_profiles

def main():
    # Get name, replit URL and Codecademy URL from profile submission
    student_profiles = get_profiles()

    # Get all replit submissions
    all_submitted_exercises = get_replit_submissions(student_profiles)

    for student in student_profiles:
        student.codecademy_percent = scrape_codecademy(student.name, student.codecademy_profile) or 0
        find_student_exercises(all_submitted_exercises, student)
        print(student)

    with open('scores.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Student", "repl.it functions", "repl.it iteration", "repl.it conditions", "Codecademy %"])
        for student in student_profiles:
            writer.writerow([student.name, f'{student.function_percent:.1f}', f'{student.iteration_percent:.1f}', f'{student.condition_percent:.1f}', f'{student.codecademy_percent}'])


if __name__ == "__main__":
    main()
