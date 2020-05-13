import csv
from Student import Student
from repl import scrape_replit
from fcc import scrape_freecodecamp
from codecademy import scrape_codecademy

def main():
    students = []
    with open('students.tsv') as students_csv:
        registrations = csv.reader(students_csv)
        for record in registrations:
            items = record[0].split('\t')

            student = Student()
            student.name = items[0]
            student.date_submitted = items[1]
            student.replit_profile = items[2]
            student.codecademy_profile = items[3]
            student.freecodecamp_profile = items[4]

            student.replit_points = scrape_replit(student.name, student.replit_profile) or 0
            student.codecademy_percent = scrape_codecademy(student.name, student.codecademy_profile) or 0
            student.freecodecamp_percent = scrape_freecodecamp(student.name, student.freecodecamp_profile) or 0
            students.append(student)

    with open('scores.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Student", "repl.it", "Codecademy %", "FreeCodeCamp %"])
        for student in students:
            writer.writerow([student.name, student.replit_points, student.codecademy_percent, student.freecodecamp_percent])

if __name__ == "__main__":
    main()
