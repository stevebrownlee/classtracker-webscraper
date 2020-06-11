class Student(object):
    def __init__(self):
        self.function_exercises = []
        self.function_percent = 0
        self.condition_exercises = []
        self.condition_percent = 0
        self.iteration_exercises = []
        self.iteration_percent = 0
        self.name = ""
        self.date_submitted = None
        self.replit_points = 0
        self.replit_profile = ""
        self.codecademy_percent = 0
        self.codecademy_profile = ""

    def __repr__(self):
        return (
            f'{self.name}\n'
            f'Codecademy: {self.codecademy_percent}%\n'
            f'Repl.it Functions: {self.function_percent:.1%}\n'
            f'Repl.it Iteration: {self.iteration_percent:.1%}\n'
            f'Repl.it Conditions: {self.condition_percent:.1%}\n'
        )