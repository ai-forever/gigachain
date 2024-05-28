# `langchain`

**Usage**:

```console
$ langchain [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.
* `-v, --version`: Print current CLI version.

**Commands**:

* `app`: Manage LangChain apps
* `serve`: Start the LangServe app, whether it's a...
* `template`: Develop installable templates.

## `langchain app`

Manage LangChain apps

**Usage**:

```console
<<<<<<< HEAD
$ gigachain app [OPTIONS] COMMAND [ARGS]...
=======
$ langchain app [OPTIONS] COMMAND [ARGS]...
>>>>>>> langchan/master
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `add`: Adds the specified template to the current...
* `new`: Create a new LangServe application.
* `remove`: Removes the specified package from the...
* `serve`: Starts the LangServe app.

<<<<<<< HEAD
### `gigachain app add`
=======
### `langchain app add`
>>>>>>> langchan/master

Adds the specified template to the current LangServe app.

e.g.:
<<<<<<< HEAD
gigachain app add extraction-openai-functions
gigachain app add git+ssh://git@github.com/efriis/simple-pirate.git
=======
langchain app add extraction-openai-functions
langchain app add git+ssh://git@github.com/efriis/simple-pirate.git
>>>>>>> langchan/master

**Usage**:

```console
<<<<<<< HEAD
$ gigachain app add [OPTIONS] [DEPENDENCIES]...
=======
$ langchain app add [OPTIONS] [DEPENDENCIES]...
>>>>>>> langchan/master
```

**Arguments**:

* `[DEPENDENCIES]...`: The dependency to add

**Options**:

* `--api-path TEXT`: API paths to add
* `--project-dir PATH`: The project directory
* `--repo TEXT`: Install templates from a specific github repo instead
* `--branch TEXT`: Install templates from a specific branch
* `--help`: Show this message and exit.

<<<<<<< HEAD
### `gigachain app new`
=======
### `langchain app new`
>>>>>>> langchan/master

Create a new LangServe application.

**Usage**:

```console
<<<<<<< HEAD
$ gigachain app new [OPTIONS] NAME
=======
$ langchain app new [OPTIONS] NAME
>>>>>>> langchan/master
```

**Arguments**:

* `NAME`: The name of the folder to create  [required]

**Options**:

* `--package TEXT`: Packages to seed the project with
* `--help`: Show this message and exit.

<<<<<<< HEAD
### `gigachain app remove`
=======
### `langchain app remove`
>>>>>>> langchan/master

Removes the specified package from the current LangServe app.

**Usage**:

```console
<<<<<<< HEAD
$ gigachain app remove [OPTIONS] API_PATHS...
=======
$ langchain app remove [OPTIONS] API_PATHS...
>>>>>>> langchan/master
```

**Arguments**:

* `API_PATHS...`: The API paths to remove  [required]

**Options**:

* `--help`: Show this message and exit.

<<<<<<< HEAD
### `gigachain app serve`
=======
### `langchain app serve`
>>>>>>> langchan/master

Starts the LangServe app.

**Usage**:

```console
<<<<<<< HEAD
$ gigachain app serve [OPTIONS]
=======
$ langchain app serve [OPTIONS]
>>>>>>> langchan/master
```

**Options**:

* `--port INTEGER`: The port to run the server on
* `--host TEXT`: The host to run the server on
* `--app TEXT`: The app to run, e.g. `app.server:app`
* `--help`: Show this message and exit.

<<<<<<< HEAD
## `gigachain serve`
=======
## `langchain serve`
>>>>>>> langchan/master

Start the LangServe app, whether it's a template or an app.

**Usage**:

```console
<<<<<<< HEAD
$ gigachain serve [OPTIONS]
=======
$ langchain serve [OPTIONS]
>>>>>>> langchan/master
```

**Options**:

* `--port INTEGER`: The port to run the server on
* `--host TEXT`: The host to run the server on
* `--help`: Show this message and exit.

<<<<<<< HEAD
## `gigachain template`
=======
## `langchain template`
>>>>>>> langchan/master

Develop installable templates.

**Usage**:

```console
<<<<<<< HEAD
$ gigachain template [OPTIONS] COMMAND [ARGS]...
=======
$ langchain template [OPTIONS] COMMAND [ARGS]...
>>>>>>> langchan/master
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `new`: Creates a new template package.
* `serve`: Starts a demo app for this template.

<<<<<<< HEAD
### `gigachain template new`
=======
### `langchain template new`
>>>>>>> langchan/master

Creates a new template package.

**Usage**:

```console
<<<<<<< HEAD
$ gigachain template new [OPTIONS] NAME
=======
$ langchain template new [OPTIONS] NAME
>>>>>>> langchan/master
```

**Arguments**:

* `NAME`: The name of the folder to create  [required]

**Options**:

* `--with-poetry / --no-poetry`: Don't run poetry install  [default: no-poetry]
* `--help`: Show this message and exit.

<<<<<<< HEAD
### `gigachain template serve`
=======
### `langchain template serve`
>>>>>>> langchan/master

Starts a demo app for this template.

**Usage**:

```console
<<<<<<< HEAD
$ gigachain template serve [OPTIONS]
=======
$ langchain template serve [OPTIONS]
>>>>>>> langchan/master
```

**Options**:

* `--port INTEGER`: The port to run the server on
* `--host TEXT`: The host to run the server on
* `--help`: Show this message and exit.
