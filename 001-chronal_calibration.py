class Calibrator:
    def __init__(self, input_file):
        self.input = open(input_file, 'r')
        self.state = 0
        self.state_history = [0]


    def calibrate(self):
        return sum([int(line) for line in self.input])


    def get_first_repeated_state(self):
        while True:
            self.input.seek(0)
            for line in self.input:
                delta = int(line)
                self.state += delta
                # print('{} -> {}'.format(delta, self.state))
                if (self.state in self.state_history):
                    return self.state
                else:
                    self.state_history.append(self.state)

if __name__ == "__main__": 
    calibrator = Calibrator('frequencies.txt')
    print(calibrator.calibrate())
    print(calibrator.get_first_repeated_state())
