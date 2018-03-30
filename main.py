import argparse

APPLICATION_NAME="recommender"
APPLICATION_DESCRIPTION="""
Sistema de Recomendação
"""

def main(args):
    ## deve ler as informações do arquivo
    ## deve pegar as informações do usuário
    ## deve pegar as informações do item
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog=APPLICATION_NAME, description=APPLICATION_DESCRIPTION)
    parser.add_argument('arquivo', metavar="ARQUIVO", type=str, 
                        help="Arquivo csv processado para gerar as recomendações")
    parser.add_argument('usuario', metavar="USUARIO", type=int, 
                        help="Indice do usuário que se deseja a avaliação do ITEM")
    parser.add_argument('item',    metavar="ITEM",    type=int, 
                        help="Indice do item que se deseja a avaliação do USUARIO")
    args = parser.parse_args()
    
    main(args)