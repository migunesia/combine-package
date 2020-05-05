# Combine Package

Combine your npm package, yarn package or similiar into one place, so your storage will be more **efficient** & can be used as a **cdn**

## Features 

## How to use

- With file list .txt (recommended)

First, Create a .txt file that lists the package.json files that will be combined, seperate by enter. Example:

```
C:\xampp\htdocs\github\projek1\package.json
C:\xampp\htdocs\github\projek2\package.json
```

Then run the command below to combine the package into path **C:\xampp\htdocs\github\cdn**

```
python3 combine-package.py start --file_list="C:\xampp\htdocs\github\cdn\list.txt"
```

- With arguments files

```
python3 combine-package.py start --files="C:\xampp\htdocs\github\projek1\package.json","C:\xampp\htdocs\github\projek2\package.json" --combine_to="C:\xampp\htdocs\github\cdn"
```

The **--files** arguments is the package.json file that will be combined and the **--combine_to** argument is the path of combined results.


## Contributions

Please have look at contributing.md