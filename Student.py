class Student(object):
    def __init__(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def date_submitted(self):
        return self.__date_submitted

    @date_submitted.setter
    def date_submitted(self, value):
        self.__date_submitted = value

    @property
    def replit_profile(self):
        return self.__replit_profile

    @replit_profile.setter
    def replit_profile(self, value):
        self.__replit_profile = value

    @property
    def codecademy_profile(self):
        return self.__codecademy_profile

    @codecademy_profile.setter
    def codecademy_profile(self, value):
        self.__codecademy_profile = value

    @property
    def freecodecamp_profile(self):
        return self.__freecodecamp_profile

    @freecodecamp_profile.setter
    def freecodecamp_profile(self, value):
        self.__freecodecamp_profile = value

    @property
    def replit_points(self):
        return self.__replit_points

    @replit_points.setter
    def replit_points(self, value):
        self.__replit_points = value

    @property
    def codecademy_percent(self):
        return self.__codecademy_percent

    @codecademy_percent.setter
    def codecademy_percent(self, value):
        self.__codecademy_percent = value

    @property
    def freecodecamp_percent(self):
        return self.__freecodecamp_percent

    @freecodecamp_percent.setter
    def freecodecamp_percent(self, value):
        self.__freecodecamp_percent = value

    def __repr__(self):
        return (
            f'{self.name}\n'
            f'Free Code Camp: {self.freecodecamp_percent} [{self.freecodecamp_profile}]\n'
            f'Codecademy: {self.codecademy_percent} [{self.codecademy_profile}]\n'
            f'Repl: {self.replit_points} [{self.replit_profile}]\n\n'
        )