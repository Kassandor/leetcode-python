class Solution:
    @staticmethod
    def two_sum(nums_: list[int], target: int) -> list[int]:
        """
        Берем число из массива, если разница target и этого числа отсутствует в хеш-таблице
         - добавляем число в хеш-таблицу (ключ = число, значение = индекс числа из исходного массива) и идем дальше.
         Если нашли в хеш-таблице, возвращаем индексы (target - num).idx, num.idx
        :param nums_: list[int]
        :param target: int
        :return: list[int]
        """
        num_to_index = {}
        result = []
        for idx, num in enumerate(nums_):
            if target - num in num_to_index:
                result = [num_to_index[target - num], idx]
                break
            num_to_index[num] = idx
        return result

nums = [2, 7, 11, 15]

print(Solution.two_sum(nums, 9))
