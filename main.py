import argparse

from src.RecommenderSystem import RecommenderSystem
from src.FileManager import FileManager

APPLICATION_NAME="recommender"
APPLICATION_DESCRIPTION="""
Sistema de Recomendação
"""

def main(args):
    ## deve ler as informações do arquivo
    fm = FileManager(args.arquivo)
    rs = RecommenderSystem(fm)
    
    ## - O número de itens avaliados pelo Usuário X
    print( rs.getUser(args.usuario).getReviewsLength() )

    ## - O número de usuários que avaliaram o Item Y
    print( rs.getItem(args.item).getReviewsLength() )
    
    ## - Se o Usuário X avaliou o Item Y
    ##      r<sub>x,y</sub>
    if rs.hasRating(args.usuario, args.item):
        print( rs.getRating(args.usuario, args.item) )
    ## - Se o Usuário X não avaliou o Item Y
    ##      pred(r<sub>x,y</sub>) usando abordagem baseada em usuários (Seção 2.1.1)
    ##      pred(r<sub>x,y</sub>) usando abordagem baseada em itens (Seção 2.2.1)
    else:
        print("Carregando informações para usuario " + str(args.usuario) + " e item " + str(args.item) )
        print( rs.getUserBasedPrediction(args.usuario, args.item) )
        # print( rs.getItemBasedPrediction(args.usuario, args.item) )
    

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