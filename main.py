import logging
from parser import set_parser_arg

def main():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    args = set_parser_arg()
    logging.info(args.filename)
    logging.info(args.start)
    logging.info(args.end)
    logging.info(args.format)


if __name__ == "__main__":
    main()