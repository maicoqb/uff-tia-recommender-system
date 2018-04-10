import unittest

from test.helper.UserBasedPredictioneerBuilder import UserBasedPredictioneerBuilder

class UserBasedPredictioneerTestCase(unittest.TestCase):

    def test_predicao_tudo_igual_deve_retornar_o_mesmo_valor(self):
        """
        Dado: um preditor baseado em usuário com 5 usuários
        O primeiro usuário com avaliação para os items 1..4 = n
        E os demais com avaliação para os items 1..5 = n
        Quando: eu pegar a predição do usuário 1 para o item 5
        Então: deve me retornar o valor n
        """
        ubp = UserBasedPredictioneerBuilder() \
                .withRatingNWithValue(5, 1) \
                .build()
        
        prediction = ubp.getPrediction(1,5)

        self.assertAlmostEqual(1, prediction)

        ubp = UserBasedPredictioneerBuilder() \
                .withRatingNWithValue(5, 2) \
                .build()
        
        prediction = ubp.getPrediction(1,5)

        self.assertAlmostEqual(2, prediction)

        ubp = UserBasedPredictioneerBuilder() \
                .withRatingNWithValue(5, 10) \
                .build()
        
        prediction = ubp.getPrediction(1,5)

        self.assertAlmostEqual(10, prediction)
        
    def test_predicao_tudo_igual_no_meio_da_lista_deve_retornar_o_mesmo_valor(self):
        """
        Dado: um preditor baseado em usuário com 5 usuários
        O usuário 3 com avaliação para os items 1..2,4..5 = n
        E os demais com avaliação para os items 1..5 = n
        Quando: eu pegar a predição do usuário 3 para o item 3
        Então: deve me retornar o valor n
        """
        ubp = UserBasedPredictioneerBuilder() \
                .withRatingInMiddleWithValue(1) \
                .build()
        
        prediction = ubp.getPrediction(3,3)

        self.assertAlmostEqual(1, prediction)

        ubp = UserBasedPredictioneerBuilder() \
                .withRatingInMiddleWithValue(2) \
                .build()
        
        prediction = ubp.getPrediction(3,3)

        self.assertAlmostEqual(2, prediction)

        ubp = UserBasedPredictioneerBuilder() \
                .withRatingInMiddleWithValue(10) \
                .build()
        
        prediction = ubp.getPrediction(3,3)

        self.assertAlmostEqual(10, prediction)

    def test_predicao_tudo_igual_deve_ignorar_os_itens_nao_avaliados(self):
        """
        Dado: um preditor baseado em usuário com 5 usuários
        O primeiro usuário com avaliação para os items 1..2,5 = n
        E os demais com avaliação para os items 1..5 = n
        Quando: eu pegar a predição do usuário 1 para os item 3 e 4
        Então: deve me retornar o valor n
        """
        n = 1
        ubp = UserBasedPredictioneerBuilder() \
                .withRatingIn3And4(n) \
                .build()
        
        p1 = ubp.getPrediction(1, 3)
        p2 = ubp.getPrediction(1, 4)
        self.assertAlmostEqual(n, p1)
        self.assertAlmostEqual(n, p2)

        n = 12
        ubp = UserBasedPredictioneerBuilder() \
                .withRatingIn3And4(n) \
                .build()
        
        p1 = ubp.getPrediction(1, 3)
        p2 = ubp.getPrediction(1, 4)
        self.assertAlmostEqual(n, p1)
        self.assertAlmostEqual(n, p2)

        n = 20
        n = 20
        ubp = UserBasedPredictioneerBuilder() \
                .withRatingIn3And4(n) \
                .build()
        
        p1 = ubp.getPrediction(1, 3)
        p2 = ubp.getPrediction(1, 4)
        self.assertAlmostEqual(n, p1)
        self.assertAlmostEqual(n, p2)
