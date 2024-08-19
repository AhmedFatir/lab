export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="robbyrussell"

plugins=(git)

source $ZSH/oh-my-zsh.sh


alias zshup='source /root/.zshrc'
alias rmf='rm -rf'
alias py='python3.9'
alias pym='python3.9 manage.py'
alias pymm='python3.9 manage.py migrate'
alias pymr='python3.9 manage.py runserver'
alias spro='django-admin startproject'
alias sapp='python3.9 manage.py startapp'
