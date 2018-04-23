import unittest

import src.library as library
from test.helper.FileManagerBuilder import FileManagerBuilder

class libraryTestCase(unittest.TestCase):

    def test_pdFakeFile_verificando_se_drop_esta_correto(self):
        fm = FileManagerBuilder.fromList([
            ["User/Item","Item1","Item2"],
            ["User1","val1","val2"],
        ]).build()

        pdWithDrop = library.pdFakeFile(fm).drop("User/Item",axis=1)
        
        self.assertEqual(len(pdWithDrop.getRows()), 2)
        self.assertEqual(len(pdWithDrop.getColumns()), 2)
        self.assertListEqual(pdWithDrop.getRows(), [
            ["Item1","Item2"],
            ["val1","val2"],
        ])
    
    def test_pdFakeFile_iloc_linha_coluna(self):
        fm = FileManagerBuilder.fromList([
            ["val1_1","val1_2"],
            ["val2_1","val2_2"]
        ]).build()

        pd = library.pdFakeFile(fm)

        self.assertListEqual(pd.iloc[0].values, ["val1_1","val1_2"])
        self.assertListEqual(pd.iloc[1].values, ["val2_1","val2_2"])

        self.assertListEqual(pd.iloc[:,0].values, ["val1_1","val2_1"])
        self.assertListEqual(pd.iloc[:,1].values, ["val1_2","val2_2"])

        


