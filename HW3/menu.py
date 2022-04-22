"""Implementation of menu for all tasks by each of the best team"""
from ira_tasks import task_107, task_243a, task_243b


class Menu:
    """Here there is menu for choosing which task will run"""
    msg = {
        "choices": "Available tasks: \n 0 - finish program \n 1 - task86a \n "
                   "2 - task86b \n 3 - task330 \n 4 - task87 \n 5 - task226"
                   " \n 6 - task559 \n 7 - task88a \n 8 - task88b \n "
                   "9 - task322 \n 10 - task107 \n 11 - task243a \n 12 - "
                   "task243b \n 13 - task108 \n 14 - task331a \n 15 - task331b"
                   " \n 16 - task178b \n 17 - task178v \n 18 - task554 \n 19 "
                   "- task178g \n 20 - task178d \n 21 - task555 \n 22 - "
                   "task182 \n 23 - task323 \n 24 - task560 \n",
        "bad_choice": "There is no such command, please, try again",
    }

    def __init__(self):
        self.run_menu()

    def run_menu(self):
        """Function that start running our menu"""
        choices = {"0": exit, "1": task_86a, "2": task_86b, "3": task_330,
                   "4 ": task_87, "5 ": task_226, "6 ": task_559,
                   "7 ": task_88a, "8 ": task_88b, "9 ": task_322,
                   "10": task_107, "11": task_243a, "12": task_243b,
                   "13": task_108, "14": task_331a, "15": task_331b,
                   "16": task_178b, "17": task_178v, "18": task_554,
                   "19": task_178g, "20": task_178d, "21": task_555,
                   "22": task_182, "23": task_323, "24": task_560}
        parameters = {"task_86a": (), "task_86b": (),
                      "task_330": (), "task_87": (),
                      "task_226": (), "task_559": (),
                      "task_88a": (), "task_88b": (),
                      "task_322": (), "task_107": (),
                      "task_243a": (), "task_243b": (),
                      "task_108": (), "task_331a": (),
                      "task_331b": (), "task_178b": (),
                      "task_178v": (), "task_554": (),
                      "task_178g": (), "task_178d": (),
                      "task_555": (), "task_182": (),
                      "task_323": (), "task_560": ()}
        print(self.msg["choices"])
        while True:
            command_input = input("Your choice: ")
            if command_input != "0":
                if command_input in choices.keys():
                    choices[command_input](
                        *parameters[choices[command_input].__name__])
                else:
                    print(self.msg["bad_choice"])
                    print(self.msg["choices"])
            else:
                exit()

Menu()