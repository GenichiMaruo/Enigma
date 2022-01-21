class RotatingRotor:
    def __init__(self, r_dict, r_cnt):
        self.rotor_dict = r_dict
        self.rotate_cnt = r_cnt

    def output(self, input, face):
        if face == 0:
            out = self.rotor_dict[(input + self.rotate_cnt) % len(self.rotor_dict)]
        elif face == 1:
            for out in range(len(self.rotor_dict)):
                if self.rotor_dict[out] == input:
                    break
        return out

    def rotor_countup(self):
        self.rotate_cnt = (self.rotate_cnt + 1) % len(self.rotor_dict)
        if self.rotate_cnt == 0:
            return 1
        else:
            return 0

class PlagBoard:
    def __init__(self, p_list):
        self.plag_list = p_list

    def output(self, input):
        for plag in self.plag_list:
            if plag[0] == input:
                return plag[1]
            elif plag[1] == input:
                return plag[0]
        return input
