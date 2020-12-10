import shutil
from pathlib import Path
import sys, argparse
import re
from extensions import extension_paths

def moveFile(source_directory, args):
    files_in_dir = getFilesInDir(source_directory)
    files_in_dir_match_regex = getFileInDirThatMatchRegexArg(args, files_in_dir)
    files_in_dir_match_regex_and_extensions = getFileThatHaveValidExtension(files_in_dir_match_regex)
    for file in files_in_dir_match_regex_and_extensions:
        destination_directory = getDirectoryFromArgDestinationIfExists(file, source_directory, args)
        destination_file = destination_directory / file.name
        createSystemDirectoryIfNotExists(destination_directory)
        moveFileFromSourceToDestinationPath(file, destination_file)

def getFilesInDir(directory):
    return [file_in_dir for file_in_dir in directory.iterdir() if file_in_dir.is_file()]

def getFileInDirThatMatchRegexArg(args, files_in_dir):
    valid_files = []
    for file_in_dir in files_in_dir:
        if (re.search(args.regex, str(file_in_dir))):
            valid_files.append(file_in_dir)

    return valid_files

def getFileThatHaveValidExtension(valid_files):
    valid_file_match_extension = []
    for valid_file in valid_files:
        if valid_file.suffix.lower() in extension_paths:
            valid_file_match_extension.append(valid_file)

    return valid_file_match_extension

def getDirectoryFromArgDestinationIfExists(valid_file, source_directory, args):
    if args.destination is not None:
        directory_without_extension = Path.home() / args.destination
    else:
        directory_without_extension = Path.home() / source_directory

    return directory_without_extension / extension_paths[valid_file.suffix.lower()]

def createSystemDirectoryIfNotExists(directory):
    directory.mkdir(parents=True, exist_ok=True)

def moveFileFromSourceToDestinationPath(source_file, destination_file):
    shutil.move(source_file, destination_file)