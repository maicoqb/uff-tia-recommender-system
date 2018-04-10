import unittest

from test.helper.ItemBasedPredictioneerBuilder import ItemBasedPredictioneerBuilder

class ItemBasedPredictioneerTestCase(unittest.TestCase):

    def test_predicao_tudo_igual_deve_retornar_o_mesmo_valor(self):
        """
        Dado: um preditor baseado em item com 5 usuários
        O primeiro usuário com avaliação para os items 1..4 = n
        E os demais com avaliação para os items 1..5 = n
        Quando: eu pegar a predição do usuário 1 para o item 5
        Então: deve me retornar o valor n
        """
        ibp = ItemBasedPredictioneerBuilder() \
                .with5x5RatingValue(1) \
                .build()
        
        prediction = ibp.getPrediction(1,5)

        self.assertAlmostEqual(1, prediction)

        ibp = ItemBasedPredictioneerBuilder() \
                .with5x5RatingValue(2) \
                .build()
        
        prediction = ibp.getPrediction(1,5)

        self.assertAlmostEqual(2, prediction)

        ibp = ItemBasedPredictioneerBuilder() \
                .with5x5RatingValue(10) \
                .build()
        
        prediction = ibp.getPrediction(1,5)

        self.assertAlmostEqual(10, prediction)
    

    def test_predicao_tudo_igual_no_meio_da_lista_deve_retornar_o_mesmo_valor(self):
        """
        Dado: um preditor baseado em item com 5 usuários
        O usuário 3 com avaliação para os items 1..2,4..5 = n
        E os demais com avaliação para os items 1..5 = n
        Quando: eu pegar a predição do usuário 3 para o item 3
        Então: deve me retornar o valor n
        """
        ibp = ItemBasedPredictioneerBuilder() \
                .with5x5RatingInMiddle(1) \
                .build()
        
        prediction = ibp.getPrediction(3,3)

        self.assertAlmostEqual(1, prediction)

        ibp = ItemBasedPredictioneerBuilder() \
                .with5x5RatingInMiddle(2) \
                .build()
        
        prediction = ibp.getPrediction(3,3)

        self.assertAlmostEqual(2, prediction)

        ibp = ItemBasedPredictioneerBuilder() \
                .with5x5RatingInMiddle(10) \
                .build()
        
        prediction = ibp.getPrediction(3,3)

        self.assertAlmostEqual(10, prediction)

    def test_predicao_tudo_igual_deve_ignorar_os_itens_nao_avaliados(self):
        """
        Dado: um preditor baseado em usuário com 5 usuários
        Quando: eu pegar a predição do usuário 1 para os item 3 e 4
        Então: deve me retornar o valor n
        """
        n = 1
        ibp = ItemBasedPredictioneerBuilder() \
                .with5x5RatingsWithoutValuesIn([[1, 4],[3, 2]],n) \
                .build()
        
        p1 = ibp.getPrediction(1, 3)
        p2 = ibp.getPrediction(1, 4)
        self.assertAlmostEqual(n, p1)
        self.assertAlmostEqual(n, p2)

        n = 8
        ibp = ItemBasedPredictioneerBuilder() \
                .with5x5RatingsWithoutValuesIn([[1, 4],[3, 2]],n) \
                .build()
        
        p1 = ibp.getPrediction(1, 3)
        p2 = ibp.getPrediction(1, 4)
        self.assertAlmostEqual(n, p1)
        self.assertAlmostEqual(n, p2)
