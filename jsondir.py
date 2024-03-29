import sys
import json
import os

# returns all directories at given path as a list of strings
def listdirs(path):
    dirs = [name for name in os.listdir(path)
            if os.path.isdir(os.path.join(path, name))]

    if len(dirs) > 0:
        for x in range(0, len(dirs)):
            dirs[x] = (path + "/" + dirs[x])

    return dirs

# returns all files at given path as a list of strings
def listfiles(path):
    files = [name for name in os.listdir(path)
             if os.path.isfile(os.path.join(path, name))]

    if len(files) > 0:
        for x in range(0, len(files)):
            files[x] = (path + "/" + files[x])

    return files

# returns a dictionary describing a file
def createFile(path):
    data = {}
    data["name"] = os.path.basename(path)
    data["type"] = "file"
    data["path"] = path
    return data

# recursive function that stores files and directories in dictionary
def createDirectory(path):
    data = {}
    data["name"] = os.path.basename(path)
    data["type"] = "directory"
    data["path"] = path
    data["files"] = []
    data["directories"] = []
    subFiles = listfiles(path)

    for fl in subFiles:
        data["files"].append(createFile(fl))

    subDirs = listdirs(path)
    for sub in subDirs:
        data["directories"].append(createDirectory(sub))

    return data


def main():
    for x in range(0, len(sys.argv)):
        if x != 0:
            print(sys.argv[x])

    cwd = os.getcwd()
    jsonData = createDirectory(cwd)

    with open("directory.json", "w") as write_file:
        json.dump(jsonData, write_file, separators=(',', ':'), indent=2)


if __name__ == "__main__":
    main()
