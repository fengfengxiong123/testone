from django.test import TestCase
from UpDown.views import upScoreClientnum, checkRank
from django.test import RequestFactory
import json


# Create your tests here.
class TestupScoreClientnum(TestCase):
    def setUp(self):
        # super(TestupScoreClientnum, self).setUp()
        self.factory = RequestFactory()
        self.request = self.factory.post('upScoreClientnum/')

    def test_create_sucess(self):
        self.request.POST = {'client_num': '客户端1111', 'score': '11111'}
        context = json.loads(upScoreClientnum(self.request).content)['create']
        self.assertEqual(context, True)


class TestcheckRank(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_only_check_client_num(self):
        data = {'check_client_num': '客户端1', 'pre_num': '', 'next_num': ''}
        self.request = self.factory.post('checkRank/', HTTP_X_REQUESTED_WITH='XMLHttpRequest', data=data)
        client_num = json.loads(checkRank(self.request).content)
        self.assertEqual(client_num['ranks'], [])
        self.assertEqual(client_num['obj_one'], None)

    def test_all_none(self):
        data = {'check_client_num': '', 'pre_num': '', 'next_num': ''}
        self.request = self.factory.post('checkRank/', HTTP_X_REQUESTED_WITH='XMLHttpRequest', data=data)
        client_num = json.loads(checkRank(self.request).content)['ranks'][0]
        self.assertEqual(client_num['name']['client_num'], '输入客户端号和范围中的一项')
        self.assertEqual(client_num['name']['score'], '无')
        self.assertEqual(client_num['num'], '无')

    def test_pre_num_next_num_right(self):
        data = {'check_client_num': '', 'pre_num': '1', 'next_num': '2'}
        self.request = self.factory.post('checkRank/', HTTP_X_REQUESTED_WITH='XMLHttpRequest', data=data)
        client_num = json.loads(checkRank(self.request).content)
        self.assertEqual(client_num['ranks'], [])

    def test_pre_num_next_num_wrong(self):
        data = {'check_client_num': '', 'pre_num': '2', 'next_num': '1'}
        self.request = self.factory.post('checkRank/', HTTP_X_REQUESTED_WITH='XMLHttpRequest', data=data)
        client_num = json.loads(checkRank(self.request).content)
        self.assertEqual(client_num['ranks'][0]['name']['client_num'], '请按顺序输入正整数')
