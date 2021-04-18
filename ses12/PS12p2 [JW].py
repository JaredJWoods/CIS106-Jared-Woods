#------------------------CLASS INT-------------------------
class student:
    def __init__(self, fname, lname, code, credits):
        self.fname = fname
        self.lname = lname
        self.code = code
        self.credits = credits

    def tuition(self):
        if self.code == 'I':
            tuition = self.credits * 250
        else:
            tuition = self.credits * 500
        self.tuition = tuition
        return 'TUITION FEES: \t${}'.format(self.tuition, '.2f')

    def studentname(self):
        return 'STUDENT NAME: \t{}, {}'.format(self.lname, self.fname)

    def fullreport(self):
        return '{}\n{}\n{}\n{}\n'.format(self.studentname(), self.message(),
                                       self.credithours(), self.tuition())

    def credithours(self):
        return 'CREDIT HOURS:\t{}'.format(self.credits)

    def message(self):
        if self.code == 'I':
            message = 'InSTATE RATE: \t$250 per credit'
        else:
            message = 'OUT of STATE:\t$500 per credit'
        return message

s1 = student('Jared', 'Woods', 'I', 12)
s2 = student('Stephanie', 'Fossler', 'O', 10)

#--------------------display----------------------------
print(s1.fullreport())
print(s2.fullreport())

#how can s1, s2 etc be put into an array but still used with methods?

