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
  * settings (needs some improvements)
  * packages id


This script also provides contextual completion
if the reference is defined, this script provides completion of:
  - receipie options and its values (if not 'ANY')
  - package dependencies 

# FAQ

  - Is my version of conan is supported?

  This completion is tested with conan 1.14 and bash 4.4

    -----------------------------------------
   |  Supported versions    |  conan  1.14   |
   |  bash 4.4              |  X             | 
   -------------------------------------------

   Please bugtrack, if you find an issue

  - I can't complete references, profiles or layouts. What is the problem ?

You should check if your installation of conan is standard.
If it's not the case redefine the corresponding variables in the script to make available completions

   ----------------------------------------------------------------------------------------------------------------------
   |  locations                                         |  Default locations         | Variables                        | 
   |---------------------------------------------------|----------------------------|-----------------------------------|
   |  root configuration directory                     |  $HOME/.conan              |  CONAN_HOME                       |
   |  profile directories                              |  $HOME/.conan/profiles     |  CONAN_PROFILES_PATH              |
   |  layouts directories                              |  $HOME/.conan              |  CONAN_LAYOUTS_LOCATION           |
   |  data storage where packages are stored           |  $HOME/.conan/data         |  CONAN_STORAGE_PATH               |
   ----------------------------------------------------------------------------------------------------------------------

Check also known limitations about completions.

 - My custom generator is not suggested. Can I add it?

 Yes, you can extend the generator list by modifiying the function  '__conan_complete_generators'



# Known limitations

This script don't auto-complete : 
 * Remote packages or references. Only local ressources (profiles, remotes, ...) are used to perform completions for performance considerations 
 * full reference, ie reference:package_id (coming soon)
 * settings
 * elements of the current profile (only the default profile is parsed)

# License

Licence MIT can be found [here](LICENSE.md)

