import logging
import core
import output
from parser import set_parser_arg
from utils import utils

def main():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    
    run_flag = True
    
    args = set_parser_arg()

    data = utils.get_csv_file(args.filename)

    if data == []:
        logging.info('Arquivo não encontrado!')

    # only filters if both were written
    if args.start != None and args.end != None:
        if utils.validate_date(args.start) and utils.validate_date(args.end) :
            if utils.validate_date_range(args.start, args.end):
                data = utils.get_items_in_date_range(data, args.start, args.end)
            else:
                logging.info("start deve ser antes de end!")
        else:
            logging.info("o formato de start e end deve ser YYYY-MM-DD!")
    
    # unify same item
    data = utils.unify_items(data)

    # get output info
    data, mais_vendido, total_em_vendas = core.get_total_sales(data)

    if args.format == 'json':
        logging.info(output.get_json(data, mais_vendido, total_em_vendas))
    else:
        output.get_table(data, mais_vendido, total_em_vendas)
    



if __name__ == "__main__":
    main()