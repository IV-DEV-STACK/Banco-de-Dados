#!/usr/bin/env python
import os

from project.cli import main


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    main()
