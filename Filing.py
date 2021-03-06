import os


class file:
    def __init__(self):
        self.name = ''
        self.score = 0.0

    def collect(self, name, score):
        # noinspection PyBroadException
        try:
            if isinstance(float, score):
                self.score = score
            else:
                raise Exception
        except Exception:
            self.score = float(score)
        finally:
            self.name = name

    def filer(self):
        try:
            with open('Reg.txt', 'a') as output_file:
                output_file.write(self.name + ' Scored: ')
                output_file.write(str(self.score)+'\n')
        except FileNotFoundError:
            print("File Not Found")
        finally:
            output_file.close()

    def reader(self):
        read = []
        try:
            with open('Reg.txt', 'r') as input_file:
                for line in input_file:
                    read.append(line.strip('\n'))
        except FileNotFoundError as fnf:
            print(fnf)
        finally:
            input_file.close()
            return read

    @staticmethod
    def del_file():
        try:
            os.remove("Reg.txt")
        except FileNotFoundError:
            pass