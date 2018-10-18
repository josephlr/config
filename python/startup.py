import atexit
import os
import readline

# Support XDG specification for python_history

histfile = os.path.abspath(os.path.join(os.path.expanduser(os.environ['XDG_CACHE_HOME']), 'python', 'python_history'))
histdir, _ = os.path.split(histfile)

try:
    readline.read_history_file(histfile)
    h_len = readline.get_current_history_length()
except FileNotFoundError:
    os.makedirs(histdir, exist_ok=True)
    open(histfile, 'wb').close()
    h_len = 0


def save(prev_h_len, f):
    import readline

    new_h_len = readline.get_current_history_length()
    readline.set_history_length(1000)

    try:
        readline.append_history_file(new_h_len - prev_h_len, f)
    except:
        # Python2 doesn't support append_history_file
        readline.write_history_file(f)

    del readline

atexit.register(save, h_len, histfile)

del atexit
del os
del readline
