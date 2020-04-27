import os.path

import fire
from clint.textui import colored

class CombinePackage:

    type = "npm"
    support_type = ["npm", "yarn"]

    def start(self, type = "", file_list = "", files = [], combine_to = "", overwrite = True):
        # type of package manager for combine
        if type != "":
            if type in self.support_type:
                self.type = type
            else:
                self.show_error("<not_yet>", "Type package manager not supported yet")
                return

        # valid required param
        if file_list == "" and len(files) == 0:
            self.show_error("<not_yet>", "You must fill param file_list or files")
            return

        # valid & fill param file_list
        if file_list != "":
            # check file_list is exists
            if os.path.isfile(file_list):
                self.file_list = file_list
            else:
                self.show_error("<not_yet>", "The file list is not exists")
                return

        # valid & fill param files
        if len(files) > 0:
            # loop for check file exists
            all_exists = True

            if all_exists:
                self.files = files
            else:
                self.show_error("<not_yet>", "")
                return

            # valid & fill param combine to 
            if os.path.exists(combine_to):
                self.combine_to = combine_to
            else:
                self.show_error("<not_yet>", "")
                return

        # combine package
        if self.type == "npm":
            self.npm_combine()
        elif self.type == "yarn":
            print("yarn")

    def _npm_combine(self):
        if file_list != "":
            self._npm_by_file_list()
        else:
            self._npm_by_param()

    def _npm_by_file_list(self):
        print("Starting combine package by list defined ....")

    def _npm_by_param(self):
        print("Starting combine package by files param ....")

    def show_error(self, code, text):
        print(colored.red("ERROR {}: {}." . format(code, text)))



if __name__ == "__main__":
    fire.Fire(CombinePackage)