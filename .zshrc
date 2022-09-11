# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Customize PROMPT
PROMPT="%n@%m:.../%2~ %# "

# Enable zsh syntax highlighting
source ~/.zshsh/zsh-syntax-highlighting.zsh
source ~/.powerlevel10k/powerlevel10k.zsh-theme

# Source .posixshellrc-personal
[[ -f ~/.posixshellrc-personal ]] && . ~/.posixshellrc-personal

# Init powerlevel 10k
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh