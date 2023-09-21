'''
Exemplos de Unittest:
---------------------
'''


from datecalculator import parse_date_string
import unittest
import datetime as dt 

#Testando a função parse_date_string:

class TestParseDateString(unittest.TestCase):
    
    def year_zero(self):
        self.assertRaises(TypeError, parse_date_string, "25 de Abril de 0000")
    
    def negative_year(self):
        self.assertRaises(TypeError, parse_date_string, "25 de Abril de -1000")

    def invalid_day(self):
        self.assertRaises(TypeError, parse_date_string, "35 de Abril de 2004")
    
    def invalid_mouth(self):
        self.assertRaises(ValueError, parse_date_string, "20 de April de 2015")


if __name__ == "__main__":
    unittest.main()

#############################################################################################################################

from datecalculator import calculate_days_between_dates
import unittest
import datetime as date

#Testando a função calculate_days_between_dates:

class TestParsedateString(unittest.TestCase):
    def ano_negativo(self):
        self.assertRaises(TypeError, calculate_days_between_dates, "25 de Janeiro de -69 - 25 de Fevereiro de 49")

    def ano_zero(self):
        self.assertRaises(TypeError, calculate_days_between_dates, "25 de Janeiro de 00 - 25 de Fevereiro de 49")  

    def dia_falso(self):
        self.assertRaises(TypeError, calculate_days_between_dates, "40 de Janeiro de 69 - 25 de Fevereiro de 49")     

    def falta_data(self):
        self.assertRaises(TypeError, calculate_days_between_dates, "27 de janeiro de -69")    

    def mesmas_datas(self):
        self.assertEqual(calculate_days_between_dates("25 de Janeiro de 69 - 25 de Janeiro de 69"), 0)                 

unittest.main()    

if __name__ == "__main__":
    unittest.main()