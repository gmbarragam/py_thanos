import argparse
from thanos import Thanos
from loguru import logger

# argparse setup
PARSER = argparse.ArgumentParser()
PARSER.add_argument('--path', '-p', nargs=1,
                    metavar=('<path>'))

OPTIONS = PARSER.parse_args()

def main(path):
    thanos = Thanos(path)
    logger.critical("*finger snap*")
    thanos.snap_fingers()

if OPTIONS.path:
    main(*OPTIONS.path)
else:
    pass
