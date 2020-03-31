function loading_display(){
  CMD=$1
  COUNT=1
  if [ "$VERBOSE" != "true" ]; then
    exec 4<&2
    exec 2>/dev/null
  fi

  set -o pipefail
  ${CMD} | while read LINE; do
    # give some feedback that we're running without spamming
    # the operator with nonsense
    if [ "$VERBOSE" = "true" ]; then
      echo "${LINE}"
    else
      if [ $COUNT -gt 4 ]; then
        echo -n '.'
        COUNT=1
      fi
    fi
    ((COUNT++))
  done

  echo
  if [ "$VERBOSE" != "true" ]; then
    exec 2<&4
  fi
}

function check_env(){
  if ! type -p python3 >/dev/null; then
    echo "*** FATAL: python3 not installed. Maybe try 'brew install python'?"
    exit 1
  fi

  if ! type -p virtualenv >/dev/null; then
    echo "*** FATAL: virtualenv not installed. Maybe try 'pip install virtualenv'?"
    exit 1
  fi
}

function setup_venv(){
  if ! [ -f venv/bin/activate ]; then
    PY3=$(which python3)
    echo "*** Setting up runtime environment"
    loading_display "virtualenv -p ${PY3} venv"
    echo "*** Updating pip and setuptools"
    loading_display "./venv/bin/pip install -U pip setuptools"
  fi
}
