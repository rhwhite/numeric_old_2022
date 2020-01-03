"""
collection of scripts related to manipulating jupyter notebooks
"""

import json
from pathlib import Path
from nbgrader.preprocessors.execute import Execute as Execute_ignore_errors
from nbconvert.preprocessors import ExecutePreprocessor as Execute_error_out
from nbformat import read, write
from nbconvert import HTMLExporter
import click
from tabulate import tabulate
import shutil
from jupytext.cli import jupytext

def make_suffix_list(py_list,suffix):
    """
    make a new file list with  suffixes changed from .py to .html
    """
    new_list = [Path(item).with_suffix(suffix) for item in py_list]
    return new_list

def exec_nb(filelist, executor):
    """
    run all ipynb files in filelist
    given an nbconvert executor
    """
    for nbfile in filelist:
        print(f"working on {nbfile}")
        with open(nbfile, "rb") as fh:
            orig_nb = read(fh, 4)
            the_dir = str(Path(nbfile).resolve().parent)
            resources = {"metadata": {"path": the_dir}}
            new_nb, resources = executor.preprocess(orig_nb, resources)
            print(type(new_nb), len(new_nb))
        with open(nbfile, "w") as outfile:
            write(new_nb, outfile)

def make_html(ipynb_list):
    """
    convert a list of ipynb files into html files,
    running in the directory containing the ipynb file
    """
    html_exporter = HTMLExporter()
    for nbfile in ipynb_list:
        html_file = Path(nbfile).with_suffix(".html")
        print(f"working on {nbfile}")
        with open(nbfile, "rb") as fh:
            the_nb = read(fh, 4)
            the_dir = str(Path(nbfile).resolve().parent)
            resources = {"metadata": {"path": the_dir}}
            html_body, resources = html_exporter.from_notebook_node(the_nb, resources)
        with open(html_file, "w") as fh:
            fh.write(html_body)


@click.group()
def main():
    """
    \b
    collection of scripts to manage notebooks:
    py2ipynb -- py to ipynb, no execution
    exec_noerrors_nb -- execute ipynb, ignore errors
    make_table -- build an markdown table with notebooks
    """
    pass


@main.command()
@click.argument("filenames_json", type=click.File("r"), nargs=1)
def py2ipynb(filenames_json):
    """
    convert a list of jupytext files in filenames.json to ipynb files
    """
    file_dict = json.load(filenames_json)
    py_list = [item for item in file_dict["file_list"]]
    for pyfile in py_list:
        print(f"working on {pyfile}")
        jupytext([pyfile, "--to", "notebook"])


@main.command()
@click.argument("filenames_json", type=click.File("r"), nargs=1)
def exec_noerrors_nb(filenames_json):
    """
    \b
    run all ipynb files in filenames.jsonn
    ignoring exceptions
    """
    file_dict = json.load(filenames_json)
    py_list = [Path(item) for item in file_dict["file_list"]]
    ipynb_list = make_suffix_list(py_list,'.ipynb')
    pp = Execute_ignore_errors()
    exec_nb(ipynb_list,pp)


@main.command()
@click.argument("filenames_json", type=click.File("r"), nargs=1)
def ipynb2html(filenames_json):
    """
    \b
    convert a list of ipynb files in filenames.json 
    to html
    """
    file_dict = json.load(filenames_json)
    py_list = [Path(item) for item in file_dict["file_list"]]
    ipynb_list = make_suffix_list(py_list,'.ipynb')
    make_html(ipynb_list)


@main.command()
@click.argument("filenames_json", type=click.File("r"), nargs=1)
def find_images(filenames_json):
    """
    \b
    find all images associated with a notebook
    and add to filenames.json
    """


@main.command()
@click.argument("filenames_json", type=click.File("r"), nargs=1)
def make_table(filenames_json):
    header_strings = (
            r'{"jupytext":{"notebook_metadata_filter": "all,-language_info,-toc,-latex_envs"}}',
            r'{"jupytext":{"formats":"ipynb,md"}}'

        )
    def make_link(filename):
        str_name = filename.name
        return f"[{str_name}]({str(filename)})"

    def move_file(outdir, filenames):
        for the_file in filenames:
            old_path = Path(the_file).resolve()
            filename = old_path.name
            new_path = outdir / filename
            shutil.copyfile(old_path, new_path)

    out_dir = Path("viewtable")
    out_dir.mkdir(parents=True, exist_ok=True)
    file_dict = json.load(filenames_json)
    py_list = [Path(item) for item in file_dict["file_list"]]
    html_list = make_suffix_list(py_list, '.html')
    py_links = [make_link(item) for item in py_list]
    html_links = [make_link(item) for item in html_list]
    the_dict = dict(python=py_links, html=html_links)
    md_page = tabulate(the_dict, headers="keys", tablefmt="github")
    tablefile = out_dir / "notebook_table.md"
    with open(tablefile, "w") as tablefd:
        tablefd.write(md_page)
    jupytext([str(tablefile),"--set-kernel","-"])
    for format_string in header_strings:
        jupytext([str(tablefile), "--update-metadata", format_string])
    jupytext([str(tablefile),"--sync"])
    table_ipynb = tablefile.with_suffix('.ipynb')
    make_html([table_ipynb])
    

    for html_file, py_file in zip(html_list, py_list):
        new_html = out_dir / html_file.name
        shutil.copyfile(html_file, new_html)
        new_py = out_dir / py_file.name
        shutil.copyfile(py_file, new_py)


if __name__ == "__main__":
    main()
