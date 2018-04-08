import unittest

from test.helper.RecommenderSystemBuilder import RecommenderSystemBuilder

class RecommenderSystemTestCase(unittest.TestCase):

    def test_deve_exibir_um_lista_de_3_usuarios(self):
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
