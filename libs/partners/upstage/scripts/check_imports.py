import sys
import traceback
from importlib.machinery import SourceFileLoader

if __name__ == "__main__":
    files = sys.argv[1:]
    has_failure = False
    for file in files:
        try:
            SourceFileLoader("x", file).load_module()
        except Exception:
            has_faillure = True
<<<<<<< HEAD
            print(file)  # noqa: T201
            traceback.print_exc()
            print()  # noqa: T201
=======
            print(file)
            traceback.print_exc()
            print()
>>>>>>> langchan/master

    sys.exit(1 if has_failure else 0)
