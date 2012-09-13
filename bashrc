# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                    ..__...__.........._____.
#                    _/  |_|__|._______/  ___\
#                    \   __\  |/  ___/\   __\.
#                    .|  |.|  |\___ \..|  |...
#                    .|__|.|__/____  >.|__|...
#                    ..............\/.........
#
#                     Useful Bashrc Template
#
#     For all functions to be operational you need to get
#   elinks, wikipedia2tex and macchanger using apt-get. Create  
#    a backup of your ~/.bashrc and then replace it with 
#     this script to add a bit for functionality.
#
#
#       Build by Yuval (tisf) Nativ from See-Security Group
#                  http://www.see-security.com
#                 https://avtacha.wordpress.com
#
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Initializing Colors
    DULL=0
    BRIGHT=1
    FG_BLACK=30
    FG_RED=31
    FG_GREEN=32
    FG_YELLOW=33
    FG_BLUE=34
    FG_VIOLET=35
    FG_CYAN=36
    FG_WHITE=37
    FG_NULL=00
    BG_BLACK=40
    BG_RED=41
    BG_GREEN=42
    BG_YELLOW=43
    BG_BLUE=44
    BG_VIOLET=45
    BG_CYAN=46
    BG_WHITE=47
    BG_NULL=00
    ESC="\033"
    NORMAL="\[$ESC[m\]"
    RESET="\[$ESC[${DULL};${FG_WHITE};${BG_NULL}m\]"
    BLACK="\[$ESC[${DULL};${FG_BLACK}m\]"
    RED="\[$ESC[${DULL};${FG_RED}m\]"
    GREEN="\[$ESC[${DULL};${FG_GREEN}m\]"
    YELLOW="\[$ESC[${DULL};${FG_YELLOW}m\]"
    BLUE="\[$ESC[${DULL};${FG_BLUE}m\]"
    VIOLET="\[$ESC[${DULL};${FG_VIOLET}m\]"
    CYAN="\[$ESC[${DULL};${FG_CYAN}m\]"
    WHITE="\[$ESC[${DULL};${FG_WHITE}m\]"
    BRIGHT_BLACK="\[$ESC[${BRIGHT};${FG_BLACK}m\]"
    BRIGHT_RED="\[$ESC[${BRIGHT};${FG_RED}m\]"
    BRIGHT_GREEN="\[$ESC[${BRIGHT};${FG_GREEN}m\]"
    BRIGHT_YELLOW="\[$ESC[${BRIGHT};${FG_YELLOW}m\]"
    BRIGHT_BLUE="\[$ESC[${BRIGHT};${FG_BLUE}m\]"
    BRIGHT_VIOLET="\[$ESC[${BRIGHT};${FG_VIOLET}m\]"
    BRIGHT_CYAN="\[$ESC[${BRIGHT};${FG_CYAN}m\]"
    BRIGHT_WHITE="\[$ESC[${BRIGHT};${FG_WHITE}m\]"
    REV_CYAN="\[$ESC[${DULL};${BG_WHITE};${BG_CYAN}m\]"
    REV_RED="\[$ESC[${DULL};${FG_YELLOW}; ${BG_RED}m\]"
    PROMPT_COMMAND='export ERR=$?'


# Configuring Basic Settings
# Touch only if you understand

    [ -z "$PS1" ] && return
    HISTCONTROL=ignoreboth
    shopt -s histappend
    HISTSIZE=1000
    HISTFILESIZE=2000
    shopt -s checkwinsize
    [ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

    if [ -z "$debian_chroot" ] && [ -r /etc/debian_chroot ]; then
        debian_chroot=$(cat /etc/debian_chroot)
    fi

    case "$TERM" in
        xterm-color) color_prompt=yes;;
    esac

    if [ -n "$force_color_prompt" ]; then
        if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
        color_prompt=yes
        else
        color_prompt=
        fi
    fi

    if [ -f ~/.bash_aliases ]; then
        . ~/.bash_aliases
    fi

    if [ -f /etc/bash_completion ] && ! shopt -oq posix; then
        . /etc/bash_completion
    fi

PATH=$PATH:$HOME/.rvm/bin

# Configure PS1
    
    if [ "$color_prompt" = yes ]; then
        PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
    else
        PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
    fi
    unset color_prompt force_color_prompt

    case "$TERM" in
    xterm*|rxvt*)
        PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
        ;;
    *)
        ;;
    esac

# Fun aliases

    if [ -x /usr/bin/dircolors ]; then
        test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
        alias ls='ls --color=auto'
        alias grep='grep --color=auto'
        alias fgrep='fgrep --color=auto'
        alias egrep='egrep --color=auto'
    fi

    alias ll='ls -alF'
    alias la='ls -A'
    alias l='ls -CF'
    alias wifires='sudo /etc/init.d/network-manager restart'
    alias ps='ps auxf'
    alias home='cd ~'
    alias openports='netstat -nape --inet'
    alias ns='netstat -alnp --protocol=inet | grep -v CLOSE_WAIT | cut -c-6,21-94 '
    alias expdb='echo "cat  //title/text()" | xmllint --shell http://www.exploit-db.com/rss.xml'
    alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# A bit more complex aliases
    events ()
    {
        echo ""
        echo "--------------- Events on this day ---------------"
        mon=`date +%B` 
        day=`date +%d`
        wikipedia2text -b elinks "$day $mon" | grep -A 30 "^Events"
        echo "---------------------------------------------------"
        echo ""
    }

    deaths ()
    {
        echo ""
        echo "--------------- Deaths on this day ---------------"
        mon=`date +%B` 
        day=`date +%d`
        wikipedia2text -b elinks "$day $mon" | grep -A 30 "^Deaths"
        echo "---------------------------------------------------"
        echo ""
    }

    births ()
    {
        echo ""
        echo "--------------- Births on this day ---------------"
        mon=`date +%B` 
        day=`date +%d`
        wikipedia2text -b elinks "$day $mon" | grep -A 30 "^Births"
        echo "---------------------------------------------------"
        echo ""
    }

    netinfo ()
    {
        echo ""
        echo "--------------- Network Information ---------------"
        /sbin/ifconfig | awk /'inet addr/ {print $2}'
        /sbin/ifconfig | awk /'Bcast/ {print $3}'
        /sbin/ifconfig | awk /'inet addr/ {print $4}'
        /sbin/ifconfig | awk /'HWaddr/ {print $4,$5}'
        echo "---------------------------------------------------"
        echo ""
    }
 
    hideme ()
    {
        echo ""
        echo "--------------- Network Information ---------------"
        /sbin/ifconfig eth0 | awk /'HWaddr/ {print "eth0 MAC:",$5}'
        /sbin/ifconfig wlan0 | awk /'HWaddr/ {print "wlan0 MAC:",$5}'
        sudo ifconfig eth0 down
        sudo ifconfig wlan0 down
        sudo macchanger -r eth0
        sudo macchanger -r wlan0
        /sbin/ifconfig eth0 | awk /'HWaddr/ {print "eth0 New MAC:",$5}'
        /sbin/ifconfig wlan0 | awk /'HWaddr/ {print "wlan0 New MAC:",$5}'
        echo "---------------------------------------------------"
        echo ""
    }
    
	extip ()
	{
		mkdir blabla
		cd blabla
		wget -q http://www.showmemyip.com/
		cat index.html | grep '<span id="IPAddress"' | awk '{print $2}' | sed "s/.......$//" | cut -c16-99
		rm index.html
		cd ..
		rmdir blabla
	}
