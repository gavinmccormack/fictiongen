# Just a quick script to run the webpack instance and the django test server
# This doesn't automated the virtualenvironment step, and you will need to be inside of a session already.

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
echo "Executing in ${SCRIPTPATH}"
node "${SCRIPTPATH}/"

NODEMODULES = "${SCRIPTPATH}/node_modules/" # Not sure this should be throwing an error
if ! [ -d "${NODEMODULES}" ]; then
    npm install
fi

if command -v "npm" >/dev/null; then
    npm run watch &
fi

python3 ./fictiongen_app/manage.py runserver &