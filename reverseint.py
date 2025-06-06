class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = 1
        if x < 0:
            negative = -1
            x *= -1
        x = str(x)
        x = x[::-1]
        x = int(x) * negative
        if x >= -2 ** 31 and x <= 2 ** 31 -1:
            return x
        else:
            return 0

        