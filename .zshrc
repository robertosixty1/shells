# Customize PROMPT
PROMPT="%n@%m:.../%2~ %# "

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Enable zsh syntax highlighting
source $HOME/.zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Source .posixshellrc-personal
[[ -f ~/.posixshellrc-personal ]] && . ~/.posixshellrc-personal