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
  * commands, subcommands and its options
  * references names (local only)
  * remotes
  * profiles
  * generators
  * filepaths
  * configuration items (.conan/conan.conf and profiles content)
	* conan config get <tab><tab>
	* conan profile get <tab><tab>
  * settings (needs some improvements)
  * packages id


This script also provides contextual completion
if the reference is defined, this script provides completion of:
  - receipie options and its values (if not 'ANY')
  - dependencies package for (--build=<packX>)

# Known limitations

This script is tested with conan 1.14. 

This script don't auto-complete : 
 * Remote packages or recipes. 
 * full reference, ie reference:package_id (coming soon)
 * Non standard installation of conan. The installation of conan should follow this layout
	* The localation of root configuration directory should be at "$HOME/.conan".
	if not, change the variable "CONAN_HOME" 
	* profiles should be located at $CONAN_HOME/profiles
	You can change the default location by setting CONAN_PROFILES_PATH
	* remotes must be described by this file : $CONAN_HOME/registry.txt
	* storage path should be equal to "$CONAN_HOME/data". 
	if not, you can change the location by redefining the variable "CONAN_STORAGE_PATH"
	* layouts should be located at $CONAN_HOME/layouts
	if not, you can change the location by setting this variable "CONAN_LAYOUTS_LOCATION"	

# License

Licence MIT can be found [here|LICENSE.md]

