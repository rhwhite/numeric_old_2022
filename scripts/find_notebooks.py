#!/usr/bin/env python
"""
find all notebooks and write a json file
that that gives the notebooks and their rendered
destination

example:  python scripts/find_notebooks.py docs/doc_notebooks notebook_docs_filelist.json
"""
from pathlib import Path
import click
import json
from jupytext.cli import jupytext
import datetime
import tzlocal
import os
import stat
import pytz

def find_modtime(the_file):
    """
       remove the .py or .ipynb extenstion from the file name
       to get the head, and return that name, plus the modification
       date in UTC.  
    """
    the_file = str(Path(the_file).resolve())
    #
    #  see os.stat docs for the format of the stat function.  It returns
    #  multiple fields (owner, date created, size, etc.) that are indexed by the stat object
    #
    the_date = datetime.datetime.fromtimestamp(os.stat(the_file)[stat.ST_MTIME])
    #
    # finding the local timezone is suprisingly hard -- need to install a
    # special module called tzlocal using pip install tzlocal
    #
    local_tz = tzlocal.get_localzone()
    the_date = local_tz.localize(the_date)
    #
    # convert every date to UTC
    #
    the_date = the_date.astimezone(pytz.utc)
    #
    # remove everything but the root filename
    #
    return the_date

def checkpoint_filter(item):
    """
    return True if checkpoints is not in name
    """
    return str(item).find("checkpoints") == -1


def true_if_older(file1, file2):
    """
    return True if file1 is older than file2
    or if file2 doesn't exist
    """
    if not file2.is_file():
        return True
    file1 = Path(file1)
    file2 = Path(file2)
    file1_date = find_modtime(file1)
    file2_date = find_modtime(file2)
    return file2_date > file1_date




def print_files(file_glob):
    good_files = [item for item in file_glob if str(item).find("checkpoints") == -1]
    return good_files


@click.command()
@click.argument("notebook_path", type=str, nargs=1)
@click.argument("json_file", type=click.File("w"), nargs=1)
@click.option('--initial/--no-initial', default=False,
              help="set --initial if no ipynb files present (initial checkout)")
def main(notebook_path, json_file,initial):
    """
    \b
    descend a folder with ipynb files and create a jupytext py:percent file
    if one doesn't exist, or if an existing py:percent file is older than
    the ipynb file.  Write the py:percent file paths to an ipynb json_file
    \b
    notebook_path is folder containing notebooks
    json_file is the path to a json_file to write info to
    """
    header_strings = (
            r'{"jupytext":{"notebook_metadata_filter": "all,-language_info,-toc,-latex_envs"}}',
            r'{"jupytext":{"formats":"ipynb,py:percent"}}'

        )

    notebook_path = Path(notebook_path).resolve()
    print(f"looking for notebooks in {notebook_path}")
    ipynb_files = [
        item
        for item in notebook_path.glob("**/*.ipynb")
        if checkpoint_filter(item)
    ]
    #
    # if fresh git checkout, need to generate all ipynb files
    #
    if initial:
        if len(ipynb_files) > 0:
            raise ValueError(f"--initial flag is set but see {ipynb_files}")
        py_files = [
            item
            for item in notebook_path.glob("**/*.py")
        ]
        for the_file in py_files:
            print(f"creating {the_file.with_suffix('.ipynb')}")
            jupytext(['--to','notebook',str(the_file)])
            ipynb_files = [
               item
               for item in notebook_path.glob("**/*.ipynb")
               if checkpoint_filter(item)
            ]

    py_files = [item.with_suffix(".py") for item in ipynb_files]
    for py_file, ipynb_file in zip(py_files, ipynb_files):
        #
        # generate a py:percent file if it doesn't exist and
        # make sure it's paired and synced
        #
        if not py_file.is_file() or true_if_older(py_file, ipynb_file):
           jupytext([str(ipynb_file), "--to", "py:percent"])
           for format_string in header_strings:
               jupytext([str(py_file), "--update-metadata", format_string])
           jupytext([str(py_file),"--sync"])

    the_dict = dict(
        notebook_path=str(notebook_path),
        file_list=[str(item) for item in py_files]
    )
    json.dump(the_dict, json_file, indent=4)
    print(f"wrote json file: {json_file.name}")


if __name__ == "__main__":
    main()
