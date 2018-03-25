# Shortcuts
alias ls='ls -lAtSrG'
alias python='python3'
alias pip='pip3'
alias dc='docker-compose -f docker-compose-prod.yml'
alias dcrm="dc stop -t 1 && dc rm -fv"
alias appm="docker-compose -f docker-compose-prod.yml run --rm app python manage.py"
