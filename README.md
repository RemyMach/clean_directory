# clean_directory

## What do you need
- Python 3 at least
- A Path python3 on your shell to execute a file as a binary

## What the project do
- take all the files that are in the Source Directory
- the name of the files have to correspond to the regex args
- create a directory to class all the files in a directory that matches with the
extension (refer to extensions.py)
- you can specify 3 args
    - Source directory | regex for the name file | [Destination directory]
    
## How to specify the args
```
arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        directory where the files are, path from ~
  -r REGEX, --regex REGEX
                        name regex file
  -d DESTINATION, --destination DESTINATION
                        directory where the file are going, path from ~
```
- if you don't specify Destination the Destination is going to be the current directory where the files are, the source directory
- --destination is the only optionnal argument
- if you want to match all the files you can use `""`has the regex arg

## Examples
```
# move all the file with a name Screenshot from ~/Downloads into ~/Downloads/{file Specify For The Extension File In extensions.py}
./cleanDirectory.py -s Downloads -r "Screenshot"
```

```
# move all the files from ~/Downloads/exemple into ~/Downloads/otherDestination/{file Specify For The Extension File In extensions.py}
./cleanDirectory.py -s Downloads/exemple -r "" -d Downloads/otherDestination
```