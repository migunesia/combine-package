from os import path, system
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
            if path.isfile(file_list):
                self.file_list = file_list
                self.path_file_list = path.dirname(path.realpath(self.file_list))
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
                self.files = files.split(",")
            else:
                self.show_error(
                    "<not_yet>",
                    ""
                )
                return

            # valid & fill param combine to
            if path.exists(combine_to):
                self.combine_to = combine_to
            else:
                self.show_error(
                    "<not_yet>",
                    "The given path for combine_to is incorrect"
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

        # path file package.json for combine
        if("\\" in self.path_file_list):
            cdn_package_json = self.path_file_list + "\\package.json"
        else:
            cdn_package_json = self.path_file_list + "/package.json"

        # read file & replace dependencies
        if path.isfile(cdn_package_json):
            # open file package.json
            r_cdn_package_json = open(cdn_package_json, "r")
        else:
            # npm init if package.json is not exists
            system("cd {} && npm init -y".format(self.path_file_list))
            r_cdn_package_json = open(cdn_package_json, "r")

        c_cdn_package_json = json.loads(r_cdn_package_json.read())
        c_cdn_package_json["dependencies"] = dep_combine
        r_cdn_package_json.close()

        # write file
        w_cdn_package_json = open(cdn_package_json, "w")
        w_cdn_package_json.write(json.dumps(c_cdn_package_json, indent=4))
        w_cdn_package_json.close()

    def _npm_by_param(self):
        print("Starting combine package by file below: ")

        dependencies = []
        for f in self.files:
            print(f.strip())
            file_package_json = open(f.strip(), "r")
            package_json = json.loads(file_package_json.read())
            dependencies.append(package_json["dependencies"])

        dep_combine = {}
        for dd in dependencies:
            for dname, dver in dd.items():
                if(dname not in dep_combine):
                    # if package not exists then append
                    dep_combine["{}".format(dname)] = "{}".format(dver)
                # else:
                    # check version
                    # comingsoon: get the last version of the package is coming soon

        # path file package.json for combine
        if("\\" in self.combine_to):
            cdn_package_json = self.combine_to + "\\package.json"
        else:
            cdn_package_json = self.combine_to + "/package.json"

        # read file & replace dependencies
        if path.isfile(cdn_package_json):
            # open file package.json
            r_cdn_package_json = open(cdn_package_json, "r")
        else:
            # npm init if package.json is not exists
            system("cd {} && npm init -y".format(self.combine_to))
            r_cdn_package_json = open(cdn_package_json, "r")

        c_cdn_package_json = json.loads(r_cdn_package_json.read())
        c_cdn_package_json["dependencies"] = dep_combine
        r_cdn_package_json.close()

        # write file
        w_cdn_package_json = open(cdn_package_json, "w")
        w_cdn_package_json.write(json.dumps(c_cdn_package_json, indent=4))
        w_cdn_package_json.close()

    def show_error(self, code, text):
        print(colored.red("ERROR {}: {}." . format(code, text)))


if __name__ == "__main__":
    fire.Fire(CombinePackage)
