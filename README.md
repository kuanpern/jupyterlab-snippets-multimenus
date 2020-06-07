# jupyterlab-snippets-multimenu

Snippets extension with multiple menu support for JupyterLab.

This extension is composed of a Python package named `jupyterlab-snippets-multimenus`
for the server extension and a NPM package named `jupyterlab-snippets-multimenus`
for the frontend extension.

This repo is forked from the [jupyterlab-snippets](https://github.com/QuantStack/jupyterlab-snippets) project.

<img src="images/screenshot_01.png"></img>


## Requirements
- JupyterLab >= 2.0
- Node.js

## Install

```bash
pip install jupyterlab-snippets-multimenus
```

Rebuild JupyterLab:

```bash
jupyter lab build
```

## Usage
Add snippets in `[jupyter_data_dir]/multimenus_snippets`

To find the Jupyter data directory, run:
```bash
$ jupyter --path
```
Any path under data: will do. We recommend using the virtual environment shared directory (e.g. `$VENVDIR/share/jupyter/`) (please create the directory if not existed)

Snippets will be organized in menus following the structure of the directories. The directories directly under `multimenus_snippets/` will be used to create menus.

The order of menus and sub-menus can be specified using a JSON file. An example is given in `example_snippets/multimenus_snippets_config/snippet_config.json`. This file should be put under `[jupyter_data_dir]/multimenus_snippets_config/` to take effect. If this config file is not provided, the menu will be created with all files in the directory with a default ordering.

## Quick start with examples
Example snippets directories are provided in `example_snippets/`. 

To test with automatically generated order configuration, do 
```bash
cp -r example_snippets/multimenus_snippets $VENVDIR/share/jupyter/
```
and start/refresh jupyter-lab

To test configurable ordering, do
```bash
cp -r example_snippets/multimenus_snippets_config $VENVDIR/share/jupyter/
```
and start/refresh jupyter-lab


