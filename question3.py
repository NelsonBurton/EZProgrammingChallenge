import copy
class Animation:
    def change_to_x(self, list):
        out = "" 
        for i in range(len(list)):
            if list[i][0] == 'L' or list[i][1] == 'R':
                out += "X"
            else:
                out += "."
        return out

    def all_dots(self, list):
        for i in range(len(list)):
            if list[i][0] != '.' or list[i][1] != '.':
                return False
        return True

    def animate(self, speed, init):
        # initialize as empty
        out = [['.','.'] for i in range(len(init))]
        for i in range(len(init)):
            if init[i] == 'L':
                out[i][0] = 'L'
            elif init[i] == 'R':
                out[i][1] = 'R'
        steps = []
        steps.append(self.change_to_x(out))
        while not self.all_dots(out):
            for l in range(len(out)):
                if out[l][0] == 'L':
                    out[l][0] = '.'
                    if l-speed >= 0: out[l-speed][0] = 'L'
            # go backwards for the right
            for b in range(len(out)):
                r = len(out) - b - 1
                if out[r][1] == 'R':
                    out[r][1] = '.'
                    if r+speed < len(out): out[r+speed][1] = 'R' 
            steps.append(self.change_to_x(out))
        return steps

a = Animation()
print a.animate(2,"..R....")
print a.animate(3, "RR..LRL")
print a.animate(2, "LRLR.LRLR")
print a.animate(1, "...")
