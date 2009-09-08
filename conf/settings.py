# Disco settings
# You can use these settings to run Disco in your home directory.
# For system-wide installations, see settings.py.sys-* files.

import os

# DISCO_HOME will be guessed according to the path that disco is called from,
# however its value can be overridden here for non-standard installations.

# Lighttpd for master and nodes runs on this port. 
# disco://host URIs are mapped to http://host:DISCO_PORT.
DISCO_PORT = 8989

# Port for master <-> lighty communication.
DISCO_SCGI_PORT = 4444

# Root directory for Disco data.
DISCO_ROOT = os.path.join(DISCO_HOME, 'root')

# Root directory for Disco binaries.
# Binaries must be found under DISCO_MASTER_HOME/ebin.
DISCO_MASTER_HOME = os.path.join(DISCO_HOME, 'master')

# Root directory for Disco logs.
DISCO_LOG_DIR = os.path.join(DISCO_HOME, 'log')
DISCO_PID_DIR = os.path.join(DISCO_HOME, 'run')

# Miscellaneous flags:
# - nocurl: use httplib instead of pycurl even if pycurl is available
#DISCO_FLAGS = "nocurl"
