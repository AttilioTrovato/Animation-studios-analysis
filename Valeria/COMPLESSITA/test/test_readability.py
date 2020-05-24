import unittest
from readability import Readability


class ReadabilityTest(unittest.TestCase):
    def setUp(self):
        text = """
        “On a June day sometime in the early 1990s, encouraged by his friend and fellow economist Jörgen Weibull, Abhijit went swimming in the Baltic. He leaped in and instantly jumped out—he claims that his teeth continued to chatter for the next three days. In 2018, also in June, we went to the Baltic in Stockholm, several hundred miles farther north than the previous encounter. This time it was literally child’s play; our children frolicked in the water.
        Wherever we went in Sweden, the unusually warm weather was a topic of conversation. It was probably a portent of something everyone felt, but for the moment it was hard not to be quite delighted with the new opportunities for outdoor life it offered.”. 
        """
        self.readability = Readability(text)

    def test_ari(self):
        r = self.readability.ari()
        print(r)
        self.assertEqual(9.551245421245422, r.score)
        self.assertEqual(['10'], r.grade_levels)
        self.assertEqual([15, 16], r.ages)

    def test_coleman_liau(self):
        r = self.readability.coleman_liau()
        print(r)
        self.assertEqual(10.673162393162393, r.score)
        self.assertEqual('11', r.grade_level)

    def test_dale_chall(self):
        r = self.readability.dale_chall()
        print(r)
        self.assertEqual(9.32399010989011, r.score)
        self.assertEqual(['college'], r.grade_levels)

    def test_flesch(self):
        r = self.readability.flesch()
        print(r)
        self.assertEqual(51.039230769230784, r.score)
        self.assertEqual(['10', '11', '12'], r.grade_levels)
        self.assertEqual('fairly_difficult', r.ease)

    def test_flesch_kincaid(self):
        r = self.readability.flesch_kincaid()
        print(r)
        self.assertEqual(10.125531135531137, r.score)
        self.assertEqual('10', r.grade_level)

    def test_gunning_fog(self):
        r = self.readability.gunning_fog()
        print(r)
        self.assertEqual(12.4976800976801, r.score)
        self.assertEqual('12', r.grade_level)

    def test_linsear_write(self):
        r = self.readability.linsear_write()
        print(r)
        self.assertEqual(11.214285714285714, r.score)
        self.assertEqual('11', r.grade_level)

    def test_smog(self):
        text = """
        “On a June day sometime in the early 1990s, encouraged by his friend and fellow economist Jörgen Weibull, Abhijit went swimming in the Baltic. He leaped in and instantly jumped out—he claims that his teeth continued to chatter for the next three days. In 2018, also in June, we went to the Baltic in Stockholm, several hundred miles farther north than the previous encounter. This time it was literally child’s play; our children frolicked in the water.
        Wherever we went in Sweden, the unusually warm weather was a topic of conversation. It was probably a portent of something everyone felt, but for the moment it was hard not to be quite delighted with the new opportunities for outdoor life it offered.”. 
        """
        text = ' '.join(text for i in range(0, 5))

        readability = Readability(text)

        #Test SMOG with 30 sentences
        r1 = readability.smog()
        
        #Test SMOG with all sentences
        r2 = readability.smog(all_sentences=True)


        print("all_sentences=False: %s ; all_sentences=True: %s" % (r1,r2))
        self.assertEqual(12.516099999999998, r1.score)
        self.assertEqual('13', r1.grade_level)

        self.assertEqual(12.785403640627713, r2.score)
        self.assertEqual('13', r2.grade_level)


    def test_spache(self):
        r = self.readability.spache()
        print(r)
        self.assertEqual(7.164945054945054, r.score)
        self.assertEqual('7', r.grade_level)

    def test_print_stats(self):
        stats = self.readability.statistics()
        self.assertEqual(562, stats['num_letters'])
        self.assertEqual(117, stats['num_words'])
        self.assertEqual(7, stats['num_sentences'])
        self.assertEqual(20, stats['num_polysyllabic_words'])
