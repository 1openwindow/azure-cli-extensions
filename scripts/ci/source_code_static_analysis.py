# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

import os
import sys
import multiprocessing

from pylint import lint
from flake8.main import application

from util import get_repo_root

from verify_codeowners import main as _verify_codeowners


SDK_FILE_MARKER = r"# Code generated by Microsoft (R) AutoRest Code Generator."


# build list of sdk files
def _get_sdk_module_list(root_dir):
    dir_paths = [os.path.join(root_dir, path) for path in os.listdir(root_dir)]
    sdk_files = []

    for path in dir_paths:
        if os.path.isdir(path):
            sdk_files.extend(_get_sdk_module_list(path))
        elif _is_sdk_file(path):
            sdk_files.append(os.path.dirname(path))

    return sdk_files


# check if the current file is a python sdk file
def _is_sdk_file(file_path):
    # don't bother opening non-python files. e.g pyc files.
    if not file_path.endswith(".py"):
        return False
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            if SDK_FILE_MARKER in line:
                return True
    return False


# build list of modules that start with prefix "azext_" in the src
def _get_azext_module_paths(root_dir):
    src_root = os.path.join(root_dir, "src")
    src_paths = [os.path.join(src_root, path) for path in os.listdir(src_root)]
    ext_modules = []
    for ext_root in src_paths:
        if os.path.isdir(ext_root):
            paths = [path for path in os.listdir(ext_root)]
            ext_modules.extend([os.path.join(ext_root, path) for path in paths if path.startswith("azext_")])
    return ext_modules


# build list of python ci scripts
def _get_ci_py_file_paths(directory):
    return [os.path.join(directory, path) for path in os.listdir(directory) if path.endswith(".py")]


def _run_pylint(module_paths, ignored_modules=None, rcfile=None, cpu_count=1):
    pylint_opts = []

    if ignored_modules:
        pylint_opts.append("--ignore={}".format(ignored_modules))
    if rcfile:
        pylint_opts.append("--rcfile={}".format(rcfile))

    pylint_opts.append("--jobs={}".format(cpu_count))
    pylint_opts.extend(module_paths)

    try:
        lint.Run(pylint_opts)
    except SystemExit as se:
        # 0:  everything is fine
        # 1:  Fatal message issued
        # 2:  Error message issued
        # 4:  Warning message issued
        # 8:  Refactor message issued
        # 16: Convention message issued
        # 32: Usage error
        if se.code != 0:
            sys.exit(se.code)


def _run_flake8(module_paths, config_file=None):
    flake8_opts = ["--statistics"]

    if config_file:
        flake8_opts.append("--append-config={}".format(config_file))

    flake8_opts.extend(module_paths)

    app = application.Application()
    app.run(flake8_opts)
    try:
        app.exit()
    except SystemExit:
        pass

    if app.result_count > 0 or app.catastrophic_failure:
        sys.exit(app.result_count or 1)


def main():
    cpu_count = multiprocessing.cpu_count()

    root_dir = get_repo_root()
    sdk_modules = _get_sdk_module_list(root_dir)
    sdk_modules.append("vendored_sdks")
    module_paths = _get_azext_module_paths(root_dir)

    scripts_dir = os.path.join(root_dir, "scripts")
    ci_files = _get_ci_py_file_paths(os.path.join(scripts_dir, "ci"))

    rc_file = os.path.join(root_dir, "pylintrc")
    config_file = os.path.join(root_dir, ".flake8")

    print("\nRunning pylint on extensions...")
    _run_pylint(module_paths, ",".join(sdk_modules), rc_file, cpu_count)
    print("Pylint OK.\n")

    print("Running flake8 on extensions...")
    _run_flake8(module_paths, config_file)
    print("Flake8 OK.\n")

    print("Running pylint on CI scripts...")
    _run_pylint(ci_files, rcfile=rc_file, cpu_count=cpu_count)
    print("Pylint OK.\n")

    print("Running flake8 on CI scripts...")
    _run_flake8(ci_files, config_file=config_file)
    print("Pylint OK.\n")

    print("Other Static checks...")

    _verify_codeowners()

    print("All static checks successful!")


if __name__ == "__main__":
    main()
