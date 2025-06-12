import logging
import argparse




def main():
    # set logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    parser = argparse.ArgumentParser()

    parser.add_argument('filename', help='Nome do arquivo a ser lido')

    args = parser.parse_args()

    logging.info(args.filename)

    get_csv_file("vendasexemplo-python.csv")

if __name__ == "__main__":
    main()