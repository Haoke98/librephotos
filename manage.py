#!/usr/bin/env python
import os
import sys
from api.im2txt.build_vocab import Vocabulary

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ownphotos.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise
    execute_from_command_line(sys.argv)
