## Installation

Recommended method:

N.B This has been tested on linux, and WSL. Python packages may be harder to install directly via windows.

1. Create a virtualenv

```sh
python -m pip install virtualenv #( if necessary )
python -m venv fictiongen_env
```

2. Activate virtualenv

Linux/WSL:
```sh
source ./fictiongen_env/bin/activate
```
Windows (CMD)
```cmd
./fictiongen_env/Scripts/activate.bat
```
Windows (PS1)
```ps1
./fictiongen_env/Scripts/activate.ps1
```

3. Navigate to fictiongen base directory, and install required python modules

```
python -m pip install -r requirements.txt
```

4. Run the local development environment but executing the following command on the base directory

```
python manage.py runserver
```

This should run the development server on a local device. A rough WSGI configuration is also included but will likely need tweaking.

A sample local_settings.py is included, but you may need to change some installation specific information, particularly if it is publically accessible
