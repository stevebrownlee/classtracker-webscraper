import csv
from Student import Student
from replit import get_replit_exercises, find_student_exercises
from codecademy import scrape_codecademy
from profiles import get_profiles

def main():
    student_profiles = get_profiles()
    all_submitted_exercises = get_replit_exercises(student_profiles)

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
