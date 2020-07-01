from random import randint, choice


class RandomUtil:

    def get_random_str(self, len:int):
        """
        Generate a specified length of random string
        :param len: Length of random string
        :return:
        """
        str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        ret = ''
        for i in range(len):
            ret += choice(str)
        return ret

    def get_random_num(self, len:int):
        """
        Generate a specified length of random number
        :param len: Length of random number
        :return:
        """
        min_num = 1
        max_num = 9
        for i in range(1, len):
            min_num += 1*(10**i)
            max_num += 9*(10**i)
        return randint(min_num, max_num)

    def get_random_str_num(self, str_len, num_len):
        """
        Randomly generates a string and number combination of specified length
        :param str_len: Length of random string
        :param num_len: Length of random number
        :return:
        """
        str = self.get_random_str(str_len)
        num = self.get_random_num(num_len)
        str_num = str + '%d' %num
        return str_num

    def get_random_num_str(self, num_len, str_len):
        """
        Randomly generates a combination of numbers and strings of specified length
        :param num_len: Length of random number
        :param str_len: Length of random string
        :return:
        """
        str = self.get_random_str(str_len)
        num = self.get_random_num(num_len)
        num_str = '%d' % num + str
        return num_str

