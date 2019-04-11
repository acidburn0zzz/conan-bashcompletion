# conan-bashcompletion

A bash completion for conan
See https://github.com/conan-io/conan

This work is inspired by the docker bash completion script.

# Installation

To enable the completions either:
* place this file in 
    * /etc/bash_completion.d
    * /usr/share/bash-completion/completions

* Or you can copy this file to e.g. ~/.conan-completion and add the line
below to your .bashrc after bash completion features are loaded
. ~/.conan-bashcompletion


# Features

This script provides completion of:
  * commands and their options
  * references names
  * remotes
  * profiles
  * generators
  * filepaths
  * configuration items (.conan/conan.conf)
  * [TODO] settings
  * [TODO] packages id


This script also provides contextual completion
if the reference is defined, this script provides completion of:
  - receipie options and its values (if not 'ANY')
  - dependencies package for (--build=<packX>)
