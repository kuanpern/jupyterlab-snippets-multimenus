# jupyterlab-snippets-multimenu

Snippets extension with multiple menu support for JupyterLab.

This extension is composed of a Python package named `jupyterlab-snippets-multimenus`
for the server extension and a NPM package named `jupyterlab-snippets-multimenus`
for the frontend extension.

This repo is forked from the [jupyterlab-snippets](https://github.com/QuantStack/jupyterlab-snippets) project.


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


multimenus_snippets  multimenus_snippets_config

Add snippets in `[jupyter_data_dir]/multimenus_snippets`

To find the Jupyter data directory, run:
```bash
$ jupyter --path
```
Any path under data: will do. We recommend using the virtual environment shared directory (e.g. `$VENVDIR/share/jupyter/`) (please create the directory if not existed)

Snippets will be organized in menus following the structure of the directories. The directories directly under `multimenus_snippets/` will be used to create menus.

The order of menus and sub-menus can be specified using a JSON file. An example is given in `example_snippets/snippet_config.json`. This file should be put under `[jupyter_data_dir]/multimenus_snippets_config/` to take effect. If this config file is not provided, the menu will be created with all files in the directory with a default ordering.



In JupyterLab, use the "Snippets" menu to select the snippet:

<img width="570" alt="Schermafbeelding 2020-03-30 om 17 25 31" src="https://user-images.githubusercontent.com/46192475/77930697-8257fd00-72ab-11ea-8a77-36f45d6442d9.png">

## Convert snippets from jupyter-boilerplate format

See [jupyter-boilerplate-converter](jupyter-boilerplate-converter/README.md) on how to convert snippets from the
[jupyter-boilerplate](https://github.com/moble/jupyter_boilerplate) classic notebook extension (not available for
JupyterLab) to jupyterlab-snippets.

## Troubleshoot

If you are seeing the frontend extension but it is not working, check
that the server extension is enabled:

```bash
jupyter serverextension list
```

If the server extension is installed and enabled but you are not seeing
the frontend, check the frontend extension is installed and enabled:

```bash
jupyter labextension list
```

If it is installed, try:

```bash
jupyter lab clean
jupyter lab build
```

## Contributing

