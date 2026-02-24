class Solution:
    @staticmethod
    def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Элементы будут вставляться с конца массива insert_pos = m + n - 1, цикл вставки идет до тех пор,
        пока есть элементы во второстепенном массиве.
        Каждую итерацию, берутся nums1[m] и nums2[n], тот, что больше, вставляется в insert_pos,
         затем идет смещение влево

        :param nums1: Исходный массив
        :param m: Количество значимых элементов в исходном массиве
        :param nums2: Массив, который необходимо вмержить в исходный
        :param n: Количество значимых элементов во второстепенном массиве
        :return: None
        """
        insert_pos = m + n - 1
        m -= 1
        n -= 1

        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[insert_pos] = nums1[m]
                m -= 1
            else:
                nums1[insert_pos] = nums2[n]
                n -= 1
            insert_pos -= 1


nums_1 = [1, 2, 3, 0, 0, 0]
m_ = 3  # Три значимых элемента, остальное - нули заполнители
nums_2 = [2, 5, 6]  # Все элементы - значимые (их три)
n_ = 3

print('before_merge')
print(nums_1)
Solution.merge(nums_1, m_, nums_1, n_)
print('after_merge')
print(nums_1)
