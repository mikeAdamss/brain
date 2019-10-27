
import os
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def green(text):
    return bcolors.OKGREEN + text + bcolors.ENDC

def blue(text):
    return bcolors.OKBLUE + text + bcolors.ENDC

def switchColour(colour):
    if colour == green:
        return blue
    return green

def find_thoughts(wanted_tags):

        colour = green

        just_print_the_tags = False
        if len(wanted_tags) == 0:
            just_print_the_tags = True

        things_path = os.path.dirname(os.path.realpath(__file__)) + "/thoughts"

        only_files = [f for f in os.listdir(things_path) if os.path.isfile(os.path.join(things_path, f))]

        demarcator = "-"*40
        unique_tags = {}

        for fl in only_files:

            with open(os.path.join(things_path, fl), "r") as f:

                match = False
                for line in f.readlines():

                    if line.split(" ")[0] == "tags:":
                        tags_in_file = [x.replace("\n", "") for x in line.split(" ")][1:]
                        if len([t for t in wanted_tags if t in tags_in_file]) == len(wanted_tags):

                            if just_print_the_tags:
                                for t in tags_in_file:
                                    if t in unique_tags:
                                        unique_tags[t]+=1
                                    else:
                                        unique_tags.update({t:1})
                            else:
                                match = True
                                tag_line = line

                    else:
                        if match == True:

                            if line.startswith("name:"):
                                print(colour(demarcator))
                                print(bcolors.HEADER + line.replace("\n", "") + bcolors.ENDC)
                                print(colour(tag_line.replace("\n", "")))
                            else:
                                print(colour(line.replace("\n", "")))

                if not just_print_the_tags:
                    print()

            colour = switchColour(colour)

        if just_print_the_tags:
            print("Usage: `brain <tag1> <tag2> etc...` for 1+ tags\n")
            print("Available tags:")
            print("---------------")
            for tag, count in unique_tags.items():
                print(count, " "*(2-len(str(count))), "|  ", tag)
            print()

if __name__ == "__main__":

    tags_provided = []
    for i in range(1, len(sys.argv)):
        tags_provided.append(sys.argv[i])
    print()

    find_thoughts(tags_provided)