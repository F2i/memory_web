from django.test import TestCase
from .models import Memory
from django.contrib.auth.models import User

class MemoryHubTest(TestCase):
    # def 

    def set_up(self):
        self.lst_expect = []
        self.user_0 = User.objects.create(username='anh_ban_a', password='giang_hoa')
        self.user_1 = User.objects.create(username='giang_hoa', password='anh_ban_a')
        self.item = Memory(
            location = 'Thanh pho Ho Chi Minh',
            comment = 'Hom nay thanh pho bi phong toa nua roi, them bun bo ghe',
            created_at = 'Oct. 8, 2021, 12:56 p.m.',
            user = self.user_0
        )
        self.item.save()
        self.lst_expect.append(self.item)
        self.item = Memory(
            location = 'Thanh pho Ho Chi Minh',
            comment = 'Hom nay thanh pho bi phong toa nua roi, them bun bo ghe',
            created_at = 'Oct. 8, 2021, 12:57 p.m.',
            user = self.user_0
        )
        self.item.save()
        self.lst_expect.append(self.item)
        self.item = Memory(
            location = 'Thanh pho Ho Chi Minh',
            comment = 'Hom nay thanh pho bi phong toa nua roi, them bun bo ghe',
            created_at = 'Oct. 8, 2021, 12:58 p.m.',
            user = self.user_1
        )
        self.item.save()
        self.lst_expect.append(self.item)

    def test_memory_creation(self):
        self.set_up()
        self.lst_observed = []
        self.record = Memory.objects.filter(user=self.user_0).get(pk=1)
        self.lst_observed.append(self.record)
        self.record = Memory.objects.filter(user=self.user_0).get(pk=2)
        self.lst_observed.append(self.record)
        self.record = Memory.objects.filter(user=self.user_1).get(pk=3)
        self.lst_observed.append(self.record)
        self.assertEqual( self.lst_expect, self.lst_observed)

