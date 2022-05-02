import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source(
            "The Guardian", 
            "Dispatch from Ukraine: Here's what CNN is seeing on the ground in Lviv",
            "https://amp.theguardian.com/lifeandstyle/2022/may/01/james-wong-on-gardening-ferns-arent-nearly-so-fickle-as-people-sometimes-fear",
            "They’re reputed to be immensely difficult to grow. That’s nonsenseThere are some pieces of received wisdom in horticulture that are so frequently repeated, it can seem as if they simply must be true.",
            "us",
            "https://i.guim.co.uk/img/media/19bd332853c3bc31f2ece9d2f7550266a631afca/0_412_5466_3280/master/5466.jpg?width=1200&height=630&quality=85&auto=format&fit=crop&overlay-align=bottom%2Cleft&overlay-width=100p&overlay-base64=L2ltZy9zdGF0aWMvb3ZlcmxheXMvdG8tZGVmYXVsdC5wbmc&enable=upscale&s=cf8cba3e23a95653583ffd81224c5c14"
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == "__main__":
    unittest.main()