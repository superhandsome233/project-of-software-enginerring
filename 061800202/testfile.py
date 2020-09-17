import unittest
import testfile_main

class make_all_text(unittest.TestCase):
    def test_self(self):
        print("测试文本为orig.txt")
        testfile_main.test_main('orig.txt', 'orig.txt', 'ans.txt')
    def test_add(self):
        print("测试文本为orig_0.8_add.txt")
        testfile_main.test_main('orig.txt','orig_0.8_add.txt','ans.txt')
    def test_del(self):
        print("测试文本为orig_0.8_del.txt")
        testfile_main.test_main('orig.txt', 'orig_0.8_del.txt', 'ans.txt')
    def test_dis_1(self):
        print("测试文本为orig_0.8_dis_1.txt")
        testfile_main.test_main('orig.txt', 'orig_0.8_dis_1.txt', 'ans.txt')
    def test_dis_3(self):
        print("测试文本为orig_0.8_dis_3.txt")
        testfile_main.test_main('orig.txt', 'orig_0.8_dis_3.txt', 'ans.txt')
    def test_dis_7(self):
        print("测试文本为orig_0.8_dis_7.txt")
        testfile_main.test_main('orig.txt', 'orig_0.8_dis_7.txt', 'ans.txt')
    def test_dis_10(self):
        print("测试文本为orig_0.8_dis_10.txt")
        testfile_main.test_main('orig.txt', 'orig_0.8_dis_10.txt', 'ans.txt')
    def test_dis_15(self):
        print("测试文本为orig_0.8_dis_15.txt")
        testfile_main.test_main('orig.txt', 'orig_0.8_dis_15.txt', 'ans.txt')
    def test_mix(self):
        print("测试文本为orig_0.8_mix.txt")
        testfile_main.test_main('orig.txt', 'orig_0.8_mix.txt', 'ans.txt')
    def test_rep(self):
        print("测试文本为orig_0.8_rep.txt")
        testfile_main.test_main('orig.txt', 'orig_0.8_rep.txt', 'ans.txt')
    def test_empty(self):
        print("测试文本为empty.txt")
        testfile_main.test_main('orig.txt', 'empty.txt', 'ans.txt')


