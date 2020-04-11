import json
import datetime as DT, datetime


def file_name_reader(name):
    with open(name, "r") as f:
        text = json.load(f)
        return text


def file_name_writer(text, name):
    with open(name, "w") as f:
        json.dump(text, f, indent=4)


def verification_of_the_entered_data(path, name):
    while True:
        name = input(f"{name}")
        if name in path:
            return name
        else:
            print("Invalid data entered")


class Commands:
    def __init__(self):
        self.text_target = file_name_reader("targets.json")
        self.text_deadline = file_name_reader("deadline.json")
        self.text_exp = file_name_reader("exp.json")
        self.text_lvl = file_name_reader("lvl.json")
        self.write_target = file_name_writer
        self.today = datetime.date.today()
        print("You can:\n  Add a branch - [add_b]")
        print("  Review your achievements - [review]")
        print("  Add a target to a branch - [add_t]")
        print("  Delete a target - [del_t]")
        print("  Delete a branch - [del_b]")
        print("  Completed the target? - [mscp]")

    def print_targets(self):
        result = ""
        for i in self.text_target:
            result += i + "/"
        "".join(result)
        print(result)
        return result

    def get_targets(self):
        Commands.print_targets(self)
        data = verification_of_the_entered_data(self.text_target, "Enter a branch name: ")
        result = ""
        for i in self.text_target[data]:
            result += f"| {i} |"
        print(result)
        deldata = verification_of_the_entered_data(self.text_target[data], "Enter a target name: ")
        return data, deldata

    def del_t(self, data=None, deldata=None, a=False):
        if a is False:
            data, deldata = Commands.get_targets(self)
        self.text_target[data].remove(deldata)
        file_name_writer(self.text_target, "targets.json")
        self.text_deadline[data].pop(deldata, None)
        file_name_writer(self.text_deadline, "deadline.json")
        self.text_exp[data].pop(deldata, None)
        file_name_writer(self.text_exp, "exp.json")
        print("Mission complete!")

    def mscp(self):
        data, deldata = Commands.get_targets(self)
        deadline = self.text_deadline[data][deldata]
        deadline = "".join(deadline.split("/"))
        deadline = DT.datetime.strptime(deadline, '%Y%m%d').date()
        if deadline >= datetime.date.today():
            new_exp = self.text_exp[data].get(deldata)
            old_exp = self.text_lvl[data]["exp"]
            lvl = self.text_lvl[data]["lvl"]
            exp = new_exp + old_exp
            while exp >= 100:
                lvl += 1
                exp -= 100
                print("Level up!")
            self.text_lvl[data].update({"lvl": lvl, "exp": exp})
            file_name_writer(self.text_lvl, "lvl.json")
        else:
            Commands.del_t(self, data=data, deldata=deldata, a=True)
            print("You don`t complete the task on time")
            print("You will not receive a level increase")
            exit()

    def del_b(self):
        while True:
            x = input("Enter the name of the branch you want to delete: ")
            if x in self.text_target or x in self.text_deadline[x] or x in self.text_exp[x] or x in self.text_lvl:
                break
            else:
                continue
        self.text_target.pop(x, None)
        file_name_writer(self.text_target, "targets.json")
        self.text_deadline.pop(x, None)
        file_name_writer(self.text_deadline, "deadline.json")  # removal of the branch
        self.text_exp.pop(x, None)
        file_name_writer(self.text_exp, "exp.json")
        self.text_lvl.pop(x, None)
        file_name_writer(self.text_lvl, "lvl.json")

        print("Mission complete!")

    def review(self):
        for i in self.text_target:
            lvl = 0
            exp = 0
            y = ""
            lvl += self.text_lvl[i].get("lvl")  # review of the branches and targets, lvl
            exp += self.text_lvl[i].get("exp")
            for j in self.text_target[i]:
                y += f"| {j} - {self.text_exp[i].get(j)}exp - {self.text_deadline[i][j]} |"
            print(f"{i} - {y}  - {lvl} lvl [{exp}/100]")

    def add_target(self, branch, addb=False):
        target = input("Enter target: ")
        if target in self.text_target[branch]:
            print("Such a target already exists")
            exit()
        while True:
            deadline = input("Set a deadline [YYYY/MM/DD]: ")
            y, m, d = deadline.split("/")
            a = "".join(deadline.split("/"))
            try:
                a = DT.datetime.strptime(a, '%Y%m%d').date()
                if len(y) != 4 or len(m) != 2 or len(d) != 2:
                    print("Invalid date entered")
                    continue
                elif a < self.today:
                    print("Date should not be in the past")
                    continue
                else:
                    break
            except ValueError:
                print("Invalid date entered")
                continue
        self.text_target[branch].append(target)
        self.write_target(self.text_target, "targets.json")  # add target to the branch
        data_dl = self.text_deadline
        data_dl.update({branch: {target: deadline}})
        file_name_writer(data_dl, "deadline.json")
        print("how many experience points do you get after completing the task? [0-75]")
        while True:
            exp = int(input(" - "))
            if exp > 75 or exp < 0:
                print("The number of points is incorrect")
                continue
            else:
                break
        if addb is True:
            self.text_exp.update({branch: {}})
        self.text_exp[branch].update({target: exp})
        file_name_writer(self.text_exp, "exp.json")
        print("Mission complete!")

    def add_b(self):
        while True:
            name_b = input("Enter name branch: ")
            if name_b in self.text_target:
                print("A branch with this name already exists")  # create a branch
                continue
            else:
                break
        self.text_target.update({name_b: []})
        self.write_target(self.text_target, "targets.json")
        self.text_lvl.update({name_b: {"lvl": 0, "exp": 0}})
        file_name_writer(self.text_lvl, "lvl.json")
        Commands.add_target(self, name_b, addb=True)

    def add_t(self):
        print("Select the branch to which you want to add a target")
        result = Commands.print_targets(self)
        while True:
            branch = input("- ")
            if branch in self.text_target:  # create target
                break
            else:
                print("There is no such branch")
                print(result)
        Commands.add_target(self, branch)


if __name__ == '__main__':
    Commands()
