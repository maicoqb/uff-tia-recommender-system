import unittest
import csv
import os
import sys

from src.FileManager import FileManager

class FileManagerTestCase(unittest.TestCase):

    test_arquivo_csv = 'test_arquivo.csv'

    def cria_arquivo(self, usuarios_x_avaliacoes):
        ## cria um arquivo com informações de items e usuarios
        with open(self.test_arquivo_csv, 'w', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerows(usuarios_x_avaliacoes)

    def tearDown(self):
        ## remove o arquivo quando terminar os testes
        os.remove(self.test_arquivo_csv)

    def test_deve_ler_as_informacoes_do_arquivo(self):
        """
        Dado um arquivo com 3 linhas
        E cada uma das linhas com 10 itens
        Quando processar o arquivo
        Deve gerar uma lista de 3 usuários
        E uma lista com 10 itens
        """
        usuarios_x_avaliacoes = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        ]
        self.cria_arquivo(usuarios_x_avaliacoes)

        fileManager = FileManager(self.test_arquivo_csv)
        users = fileManager.getUsers()
        items = fileManager.getItems()

        # Verifica a quantidade de usuários
        self.assertEqual(len(users), 3)

        # Verifica a quantidade de itens
        self.assertEqual(len(items), 10)

if __name__ == '__main__':
    unittest.main()
