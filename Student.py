class Student(object):
    def __init__(self):
        self.function_exercises = set()
        self.function_percent = 0

        self.condition_exercises = set()
        self.condition_percent = 0

        self.iteration_exercises = set()
        self.iteration_percent = 0

        self.iteration_intro_exercises = set()
        self.intro_iteration_percent = 0

        self.variables_intro_exercises = set()
        self.intro_variables_percent = 0

        self.objects_intro_exercises = set()
        self.intro_objects_percent = 0

        self.functions_intro_exercises = set()
        self.intro_functions_percent = 0

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
            f'Repl.it Intro to Variables: {self.intro_variables_percent:.1f}\n'
            f'Repl.it Intro to Arrays: {self.intro_iteration_percent:.1f}\n'
            f'Repl.it Intro to Objects: {self.intro_objects_percent:.1f}\n'
            f'Repl.it Intro to Functions: {self.intro_functions_percent:.1f}\n'
            f'Repl.it Conditions: {self.condition_percent:.1f}\n'
            f'Repl.it Iteration: {self.iteration_percent:.1f}\n'
            f'Repl.it Functions: {self.function_percent:.1f}\n'
        )