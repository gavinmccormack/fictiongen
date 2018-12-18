## Installation

Recommended method:

N.B This has been tested on linux, and WSL. Python packages may be harder to instlal directly via windows.

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

4. Configure local_settings.py ( copy local_settings.example, which should be fine for local development )