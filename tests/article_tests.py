import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article(
            "Block aims to simplify Bitcoin investing with new Cash App services", 
            "Block's Jack Dorsey announced three new services at the Bitcoin 2022 conference aimed at streamlining Bitcoin investing and purchasing.", 
            "https://i.insider.com/62542f5ba2956a0018d7e86d?width=1200&format=jpeg",
            "2022-04-11T13:27:59Z", 
            "insider@insider.com (Adriana Nunez)",
            "https://www.businessinsider.com/block-announces-three-cash-app-services-to-ease-bitcoin-investing-2022-4"
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

if __name__ == "__main__":
    unittest.main()