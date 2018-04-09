import unittest

from test.helper.RecommenderSystemBuilder import RecommenderSystemBuilder

class RecommenderSystemTestCase(unittest.TestCase):

    def test_exibicao_de_lista_de_usuario(self):
        """
        Dado: um sistema de recomendação com 3 usuários
        E cada usuário com 1 item
        Quando: eu pegar a informação dos 3 usuários
        Então: cada usuário deverá ter apenas 1 review
        """
        rs = RecommenderSystemBuilder() \
                .aRecommenderSystem() \
                .with3Users() \
                .with1ItemEach() \
                .build()

        user1Items = rs.getUser(1).getReviewsLength()
        user2Items = rs.getUser(2).getReviewsLength()
        user3Items = rs.getUser(3).getReviewsLength()

        self.assertEqual(1, user1Items)
        self.assertEqual(1, user2Items)
        self.assertEqual(1, user3Items)

    def test_exibicao_de_lista_de_usuario_com_mais_de_um_item(self):
        """
        Dado: um sistema de recomendação com 5 usuários
        E cada usuário com 3 item
        Quando: eu pegar a informação dos usuários
        Então: deve haver um usuário 5 com 3 itens
        """
        rs = RecommenderSystemBuilder() \
                .aRecommenderSystem() \
                .with5Users() \
                .with3ItemEach() \
                .build()

        user5Items = rs.getUser(5).getReviewsLength()

        self.assertEqual(3, user5Items)

    def test_exibicao_de_lista_de_itens(self):
        """
        Dado: um sistema de recomendação com 3 usuários
        E cada usuário com 1 item
        Quando: eu pegar a informação do item
        Então: deve haver 3 reviews para este item
        """
        rs = RecommenderSystemBuilder() \
                .aRecommenderSystem() \
                .with3Users() \
                .with1ItemEach() \
                .build()
        
        item1users = rs.getItem(1).getReviewsLength()

        self.assertEqual(3, item1users)