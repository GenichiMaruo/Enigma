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

class Enigma:
    def __init__(self, r_dicts, r_cnts, p_list, r_list):
        self.plagboard = PlagBoard(p_list)
        self.reflector = PlagBoard(r_list)
        self.rotatingrogor = []
        for i in range(len(r_dicts)):
            self.rotatingrogor.append(RotatingRotor(r_dicts[i],r_cnts[i]))
            
    def crypt(self, array):
        outarray = []
        for word in array:
            word = self.plagboard.output(word)
            for i in range(len(self.rotatingrogor)):
                word = self.rotatingrogor[i].output(word, 0)
            word = self.reflector.output(word)
            for i in range(len(self.rotatingrogor)):
                word = self.rotatingrogor[len(self.rotatingrogor)-1-i].output(word, 1)
            word = self.plagboard.output(word)
            outarray.append(word)
            rotating = self.rotatingrogor[0].rotor_countup()
            for i in range(1, len(self.rotatingrogor)):
                if rotating:
                    rotating = self.rotatingrogor[i].rotor_countup()
        return outarray

