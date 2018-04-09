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
                .with3ItemsEach() \
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

    def test_verifica_se_ha_analises(self):
        """
        Dado: um sistema de recomendações com 3 usuários
        E cada usuário com 3 itens
        Quando: eu verificar se existe análise
        Então: deve haver correlação para todos usuários e itens
        """
        rs = RecommenderSystemBuilder() \
                .aRecommenderSystem() \
                .with3Users() \
                .with3ItemsEach() \
                .build()
        
        hasRatings = []
        for user in range(0,3):
            for item in range(0,3):
                hasRatings.append( rs.hasRating(user, item) )
        
        for hasRating in hasRatings:
            self.assertTrue(hasRating)

    def test_verifica_se_ha_analises_quando_estiver_fora_da_colecao(self):
        """
        Dado: um sistema de recomendações com 1 usuário
        E este usuário possuir apenas 1 recomendação
        Quando: eu verificar se existe recomendação para um usuário que não exista
        Ou eu verificar se existe recomendação para um item que não exista
        Então: não deve haver recomendação para estes casos
        """
        rs = RecommenderSystemBuilder() \
                .aRecommenderSystem() \
                .with1User() \
                .with1ItemEach() \
                .build()
        
        hasRatingUsuario2 = rs.hasRating(2, 1)
        hasRatingItem2 = rs.hasRating(1, 2)

        self.assertFalse(hasRatingUsuario2)
        self.assertFalse(hasRatingItem2)
    
    def test_verifica_se_ha_analises_quando_nao_houver(self):
        """
        Dado: um sistema de recomendações com 1 usuário
        E este usuário com recomendações apenas para os items 1 e 3
        Quando: eu verificar se existe recomendação para o item 2
        Então: não deve haver recomendação para este item
        """
        rs = RecommenderSystemBuilder() \
                .aRecommenderSystem() \
                .with1User() \
                .withOnlyItem1And3() \
                .build()
        
        hasRatingItem2 = rs.hasRating(1,2)

        self.assertFalse(hasRatingItem2)