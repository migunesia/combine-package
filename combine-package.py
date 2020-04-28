import os.path
import json

import fire
from clint.textui import colored

class CombinePackage:

    type = "npm"
    support_type = ["npm", "yarn"]
    overwrite = True

    file_list = ""
    path_file_list = ""

    files = []
    combine_to = ""

    def start(self, type="", file_list="", files=[], combine_to="", overwrite=True):
        # type of package manager for combine
        if type != "":
            if type in self.support_type:
                self.type = type
            else:
                self.show_error(
                    "<not_yet>",
                    "Type package manager not supported yet"
                )
                return

        # valid required param
        if file_list == "" and len(files) == 0:
            self.show_error(
                "<not_yet>",
                "You must fill param file_list or files"
            )
            return

        # valid & fill param file_list
        if file_list != "":
            # check file_list is exists
            if os.path.isfile(file_list):
                self.file_list = file_list
                self.path_file_list = os.path.dirname(os.path.realpath(self.file_list))
            else:
                self.show_error(
                    "<not_yet>",
                    "The file list is not exists"
                )
                return

        # valid & fill param files
        if len(files) > 0:
            # loop for check file exists
            all_exists = True

            if all_exists:
                self.files = files
            else:
                self.show_error(
                    "<not_yet>",
                    ""
                )
                return

            # valid & fill param combine to
            if os.path.exists(combine_to):
                self.combine_to = combine_to
            else:
                self.show_error(
                    "<not_yet>",
                    ""
                )
                return

        # combine package
        if self.type == "npm":
            self._npm_combine()
        elif self.type == "yarn":
            print("yarn")

    def _npm_combine(self):
        if self.file_list != "":
            self._npm_by_file_list()
        else:
            self._npm_by_param()

    def _npm_by_file_list(self):
        print(
            "Starting combine package by list defined ({}) ...."
            .format(self.file_list)
        )

        # create list of all dependencies
        dependencies = []
        fl = open(self.file_list, "r")
        for line in fl:
            file_package_json = open(line.strip(), "r")
            package_json = json.loads(file_package_json.read())
            dependencies.append(package_json["dependencies"])

        # combine
        dep_combine = {}
        for dd in dependencies:
            for dname, dver in dd.items():
                if(dname not in dep_combine):
                    # if package not exists then append
                    dep_combine["{}".format(dname)] = "{}".format(dver)
                # else:
                    # check version
                    # comingsoon: get the last version of the package is coming soon

        # npm init

        # path file package.json for combine
        if("\\" in self.path_file_list):
            cdn_package_json = self.path_file_list + "\\package.json"
        else:
            cdn_package_json = self.path_file_list + "/package.json"

        # read file & replace dependencies
        r_cdn_package_json = open(cdn_package_json, "r")
        c_cdn_package_json = json.loads(r_cdn_package_json.read())
        c_cdn_package_json["dependencies"] = dep_combine
        r_cdn_package_json.close()

        # write file
        w_cdn_package_json = open(cdn_package_json, "w")
        w_cdn_package_json.write(json.dumps(c_cdn_package_json, indent=4))
        w_cdn_package_json.close()

    def _npm_by_param(self):
        print("Starting combine package by files param ....")

    def show_error(self, code, text):
        print(colored.red("ERROR {}: {}." . format(code, text)))


if __name__ == "__main__":
    fire.Fire(CombinePackage)
