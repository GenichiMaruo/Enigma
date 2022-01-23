class RotatingRotor:
    def __init__(self, r_dict, r_cnt):
        self.rotor_dict = r_dict
        self.rotate_cnt = r_cnt

    def output(self, input, face):
        print("input =")
        print(input)
        for i in range(len(self.rotor_dict)):
            out = self.rotor_dict[i]
            if out[face] == input:
                break
        print("out =")
        print(out[(face + 1) % 2])
        return out[(face + 1) % 2]

    def rotor_countup(self):
        self.rotate_cnt = (self.rotate_cnt + 1) % len(self.rotor_dict)
        for i in range(len(self.rotor_dict)):
            temp = self.rotor_dict[i]
            temp[1] = (temp[1]-96)%26+97
            self.rotor_dict[i] = temp
        print("rotate!!")
        print(self.rotor_dict)
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
                print("swap!")
                return plag[1]
            elif plag[1] == input:
                print("swap!")
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
        print(array)
        for word in array:
            print("word =")
            print(word)
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
            print("word =")
            print(word)
            print("\n")
        return outarray

