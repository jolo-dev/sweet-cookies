from __future__ import print_function
import os
import json
import sys

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "


dough = "{{ cookiecutter.dough }}"


def asking_for_more():
    tailwind = input(
        HINT + "Do you want to install tailwind (y/n): " + TERMINATOR
    ).lower()
    if tailwind == "y":
        print(INFO + "Install tailwind using npm" + TERMINATOR)
        os.system("npm install tailwind")
    elif tailwind == "n":
        print(INFO + "The choice is yours" + TERMINATOR)
    else:
        print(WARNING + "Please respond with (y)es or (n)o" + TERMINATOR)

    axios = input(HINT + "Do you want to install axios (y/n): " + TERMINATOR).lower()
    if axios == "y":
        print(INFO + "Install axios using npm" + TERMINATOR)
        os.system("npm install axios")
    elif axios == "n":
        print(INFO + "The choice is yours" + TERMINATOR)
    else:
        print(WARNING + "Please respond with (y)es or (n)o" + TERMINATOR)


if dough == "React":
    os.system("npx create-react-app dough --template typescript --use-npm")

elif dough == "Vue":
    os.system("npx @vue/cli create dough --default")

os.chdir("dough")
asking_for_more()

print(INFO + "npm audit fix" + TERMINATOR)
os.system("npm audit fix")
# Remove Git
os.system("rm -rf ./.git ./.gitignore")

with open("package.json") as f:
    package_json = json.load(f)

package_json["name"] = "{{ cookiecutter.project_slug }}"
package_json["author"] = "{{ cookiecutter.author }}"
package_json["description"] = "{{ cookiecutter.description }}"

with open("package.json", "w") as package_file:
    json.dump(package_json, package_file, indent=4)

os.chdir("..")

if "{{ cookiecutter.chocolate_chips }}" == "Lambdas + Api Gateway":
    os.remove("./chocolate_chips/flask_choco.py")
    os.remove("./chocolate_chips/requirements.txt")
    print(
        INFO + "Don't forget to put your Lambdas as the chocolate chips!" + TERMINATOR
    )
elif "{{ cookiecutter.chocolate_chips }}" == "Flask":
    print(INFO + "create a flask folder" + TERMINATOR)
    os.system(
        "pip install --upgrade -r ./chocolate_chips/requirements.txt --target ./chocolate_chips/flask"
    )

deploy_chocolate = input(
    HINT + "Do you want to deploy the chocolate (y/n): " + TERMINATOR
).lower()

if deploy_chocolate == "y":
    os.system(
        "npx cdk deploy chocolate-chips"
    )
