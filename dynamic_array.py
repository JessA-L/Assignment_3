# Name: Jessica Allman-LaPorte
# OSU Email: allmanlj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 10/24/2022
# Description: Implement various methods of the Dynamic array and the Bag ADT


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Method that changes the capacity of the underlying storage
        for the elements in the dynamic array. It does not change the values
        or the order of any elements currently stored in the array.
        """
        # Check for positive integers or whether new_capacity <= _size:
        if new_capacity <= 0 or new_capacity < self._size:
            return

        _new_data = StaticArray(new_capacity)

        # copy data from _data to _new_data
        for index in range(0, self._size):
            _new_data[index] = self._data[index]

        # _new_data replaces original _data array
        self._data = _new_data
        self._capacity = new_capacity

    def append(self, value: object) -> None:
        """
        This method adds a new value at the end of the dynamic array.
        """

        # if size >= capacity: resize array doubling the capacity
        if self._size >= self._capacity:
            self.resize(self._capacity * 2)

        self._data[self._size] = value
        self._size = self._size + 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at the specified index in the dynamic array.
        """
        # If the provided index is invalid, raise “DynamicArrayException”
        if index < 0 or index > self._size:
            raise DynamicArrayException

        # If array is empty or the index is the end of current array, append value
        if index == self._size or (index == 0 and self._size == 0):
            self.append(value)
            return

        # double capacity if more space needed
        if self._size == self._capacity:
            self.resize(self._capacity*2)

        _new_data = StaticArray(self._capacity)

        i = 0
        while i < self._size:
            # Copy data until index
            if i < index:
                _new_data[i] = self._data[i]
            # insert at index
            elif i == index:
                _new_data[index] = value
                self._size += 1
            # copy the rest
            else:
                _new_data[i] = self._data[i - 1]

            i += 1

        # Reassign array
        self._data = _new_data

    def remove_at_index(self, index: int) -> None:
        """
        Removes the element at the specified index in the dynamic array. Index 0
        refers to the beginning of the array. If the provided index is invalid, the method raises a
        custom “DynamicArrayException”. Code for the exception is provided in the skeleton file. If
        the array contains N elements, valid indices for this method are [0, N - 1] inclusive.
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException

        #   If the number of elements stored in the array (size) is < ¼ of its current capacity
        #       AND the current capacity is greater than 10:
        if self._capacity > 10 and self._size < self._capacity/4:

        # the capacity must be reduced to TWICE the number of current elements;
            if self._size*2 < 10:  # the reduced capacity cannot become less than 10 elements.
                self.resize(10)
            else:
                self.resize(self._size*2)

        _new_data = StaticArray(self._capacity)

        self._size -= 1
        i = 0
        while i < self._size:
            # copy data before index into new array
            if i < index:
                _new_data[i] = self._data[i]
            # copy data after index into new array (index is skipped and not copied)
            else:
                _new_data[i] = self._data[i+1]
            i += 1

        self._data = _new_data

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Returns a new DynamicArray object that contains the requested number of
        elements from the original array, starting with the element located at the requested start
        index. If the array contains N elements, a valid start_index is in range [0, N - 1] inclusive.
        A valid size is a non-negative integer.

        If the provided start index or size is invalid, or if there are not enough elements between
        the start index and the end of the array to make the slice of the requested size, this method
        raises a custom “DynamicArrayException”.
        """
        if start_index < 0 or start_index > self._size-1 or size < 0:
            raise DynamicArrayException

        _new_array = DynamicArray([])

        for element in range(start_index, start_index+size):
            _new_array.append(self[element])

        return _new_array

    def merge(self, second_da: "DynamicArray") -> None:
        """
        Takes another DynamicArray object as a parameter, and appends all elements
        from this array onto the current one, in the same order in which they are stored in the input
        array.
        """
        if self._size + second_da._size > self._capacity:
            self.resize(self._capacity*2)

        for element in range(0, second_da._size):
            self.append(second_da[element])

    def map(self, map_func) -> "DynamicArray":
        """
        This method creates a new dynamic array where the value of each element is derived by
        applying a given map_func to the corresponding value from the original array.
        """
        _map_array = DynamicArray([])

        for element in range(0, self._size):
            _map_array.append(map_func(self[element]))

        return _map_array

    def filter(self, filter_func) -> "DynamicArray":
        """
        This method creates a new dynamic array populated only with those elements from the
        original array for which filter_func returns True.
        """
        _filter_array = DynamicArray([])

        for element in range(0, self._size):
            if filter_func(self[element]) is True:
                _filter_array.append(self[element])

        return _filter_array

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        This method sequentially applies the reduce_func to all elements of the dynamic array and
        returns the resulting value. It takes an optional initializer parameter. If this parameter is not
        provided, the first value in the array is used as the initializer. If the dynamic array is empty,
        the method returns the value of the initializer (or None, if one was not provided).
        """
        if self._size == 0:
            return initializer

        i = 0
        if initializer == None:
            initializer = self[0]
            i += 1

        val = initializer

        while i < self._size:
            val = reduce_func(val, self[i])
            i += 1

        return val


def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    Will return a tuple containing (in this order) a dynamic array comprising the mode (most-occurring)
    value/s of the array, and an integer that represents the highest frequency (how many times
    they appear).

    If there is more than one value that has the highest frequency, all values at that frequency
    should be included in the array being returned in the order in which they appear in the input
    array. If there is only one mode, only that value should be included.

    Assumptions:
     - receives a dynamic array already in sorted order, either non-descending or non-ascending.
     - the input array will contain at least one element,
     - values stored in the array are all of the same type (either all numbers, or strings, or custom
        objects, but never a mix of these).
    """
    mode_array = DynamicArray([arr[0]])

    arr_len = arr.length()
    final_freq = 1
    temp_freq = 1

    i = 0
    while i < arr_len - 1:
        # If next el is the same, add 1 to temp_freq
        if arr[i] == arr[i + 1]:
            temp_freq += 1
            if temp_freq == final_freq:
                mode_array.append(arr[i])

            # If temp_freq is greater than final_freq, this is the new mode, reset mode array
            if temp_freq > final_freq:
                # clear array
                for index in range(0, mode_array._size):
                    mode_array.remove_at_index(0)
                mode_array.resize(4)
                mode_array.append(arr[i])
                final_freq = temp_freq

        elif temp_freq == final_freq and arr[i] != mode_array[mode_array.length()-1]:
            mode_array.append(arr[i])

        # Else, reset counter
        else:
            temp_freq = 1

        i += 1

    if temp_freq == final_freq and arr[i] != mode_array[mode_array.length()-1]:
        mode_array.append(arr[i])

    return mode_array, final_freq

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    # print("\n# resize - example 1")
    # da = DynamicArray()
    #
    # # print dynamic array's size, capacity and the contents
    # # of the underlying static array (data)
    # da.print_da_variables()
    # da.resize(8)
    # da.print_da_variables()
    # da.resize(2)
    # da.print_da_variables()
    # da.resize(0)
    # da.print_da_variables()
    #
    # print("\n# resize - example 2")
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    # print(da)
    # da.resize(20)
    # print(da)
    # da.resize(4)
    # print(da)

    # print("\n# append - example 1")
    # da = DynamicArray()
    # da.print_da_variables()
    # da.append(1)
    # da.print_da_variables()
    # print(da)
    #
    # print("\n# append - example 2")
    # da = DynamicArray()
    # for i in range(9):
    #     da.append(i + 101)
    #     print(da)
    #
    # print("\n# append - example 3")
    # da = DynamicArray()
    # for i in range(600):
    #     da.append(i)
    # print(da.length())
    # print(da.get_capacity())

    # print("\n# insert_at_index - example 1")
    # da = DynamicArray([100])
    # print(da)
    # da.insert_at_index(0, 200)
    # da.insert_at_index(0, 300)
    # da.insert_at_index(0, 400)
    # print(da)
    # da.insert_at_index(3, 500)
    # print(da)
    # da.insert_at_index(1, 600)
    # print(da)

    # print("\n# insert_at_index example 2")
    # da = DynamicArray()
    # try:
    #     da.insert_at_index(-1, 100)
    # except Exception as e:
    #     print("Exception raised:", type(e))
    # da.insert_at_index(0, 200)
    # try:
    #     da.insert_at_index(2, 300)
    # except Exception as e:
    #     print("Exception raised:", type(e))
    # print(da)
    #
    # print("\n# insert at index example 3")
    # da = DynamicArray()
    # for i in range(1, 10):
    #     index, value = i - 4, i * 10
    #     try:
    #         da.insert_at_index(index, value)
    #     except Exception as e:
    #         print("Cannot insert value", value, "at index", index)
    # print(da)
    #
    # print("\n# insert_at_index - example 4")
    # da = DynamicArray([100])
    # print(da)
    # da.insert_at_index(0, 200)
    # print(da)
    # da.insert_at_index(0, 300)
    # print(da)
    # da.insert_at_index(0, 400)
    # print(da)
    # # da.insert_at_index(3, 500)
    # # print(da)
    # da.insert_at_index(1, 600)
    # print(da)

    # print("\n# remove_at_index - example 1")
    # da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    # print(da)
    # da.remove_at_index(0)
    # print(da)
    # da.remove_at_index(6)
    # print(da)
    # da.remove_at_index(2)
    # print(da)
    #
    # print("\n# remove_at_index - example 2")
    # da = DynamicArray([1024])
    # print(da)
    # for i in range(17):
    #     da.insert_at_index(i, i)
    # print(da.length(), da.get_capacity())
    # for i in range(16, -1, -1):
    #     da.remove_at_index(0)
    # print(da)
    #
    # print("\n# remove_at_index - example 3")
    # da = DynamicArray()
    # print(da.length(), da.get_capacity())
    # [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    # print(da.length(), da.get_capacity())
    # [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    # print(da.length(), da.get_capacity())
    # da.remove_at_index(0)  # step 3 - remove 1 element
    # print(da.length(), da.get_capacity())
    # da.remove_at_index(0)  # step 4 - remove 1 element
    # print(da.length(), da.get_capacity())
    # [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    # print(da.length(), da.get_capacity())
    # da.remove_at_index(0)  # step 6 - remove 1 element
    # print(da.length(), da.get_capacity())
    # da.remove_at_index(0)  # step 7 - remove 1 element
    # print(da.length(), da.get_capacity())
    #
    # for i in range(14):
    #     print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
    #     da.remove_at_index(0)
    #     print(" After remove_at_index(): ", da.length(), da.get_capacity())
    #
    # print("\n# remove at index - example 4")
    # da = DynamicArray([1, 2, 3, 4, 5])
    # print(da)
    # for _ in range(5):
    #     da.remove_at_index(0)
    #     print(da)
    #
    # print("\n# remove at index - example 5")
    # da = DynamicArray([33295, 21046, 44445, -59849, -50676, -43755, -2305])
    # print(da)
    # try:
    #     da.remove_at_index(7)
    # except Exception as e:
    #     print("Exception sucessful")
    # print(da)

    # print("\n# slice example 1")
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # da_slice = da.slice(1, 3)
    # print(da, da_slice, sep="\n")
    # da_slice.remove_at_index(0)
    # print(da, da_slice, sep="\n")
    #
    # print("\n# slice example 2")
    # da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    # print("SOURCE:", da)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    # for i, cnt in slices:
    #     print("Slice", i, "/", cnt, end="")
    #     try:
    #         print(" --- OK: ", da.slice(i, cnt))
    #     except:
    #         print(" --- exception occurred.")
    # print("\n# merge example 1")
    # da = DynamicArray([1, 2, 3, 4, 5])
    # da2 = DynamicArray([10, 11, 12, 13])
    # print(da)
    # da.merge(da2)
    # print(da)
    #
    # print("\n# merge example 2")
    # da = DynamicArray([1, 2, 3])
    # da2 = DynamicArray()
    # da3 = DynamicArray()
    # da.merge(da2)
    # print(da)
    # da2.merge(da3)
    # print(da2)
    # da3.merge(da)
    # print(da3)

    # print("\n# map example 1")
    # da = DynamicArray([1, 5, 10, 15, 20, 25])
    # print(da)
    # print(da.map(lambda x: x ** 2))
    #
    # print("\n# map example 2")
    #
    #
    # def double(value):
    #     return value * 2
    #
    #
    # def square(value):
    #     return value ** 2
    #
    #
    # def cube(value):
    #     return value ** 3
    #
    #
    # def plus_one(value):
    #     return value + 1
    #
    #
    # da = DynamicArray([plus_one, double, square, cube])
    # for value in [1, 10, 20]:
    #     print(da.map(lambda x: x(value)))
    # print("\n# filter example 1")
    #
    #
    # def filter_a(e):
    #     return e > 10
    #
    #
    # da = DynamicArray([1, 5, 10, 15, 20, 25])
    # print(da)
    # result = da.filter(filter_a)
    # print(result)
    # print(da.filter(lambda x: (10 <= x <= 20)))
    #
    # print("\n# filter example 2")
    #
    #
    # def is_long_word(word, length):
    #     return len(word) > length
    #
    #
    # da = DynamicArray("This is a sentence with some long words".split())
    # print(da)
    # for length in [3, 4, 7]:
    #     print(da.filter(lambda word: is_long_word(word, length)))
    # print("\n# reduce example 1")
    # values = [100, 5, 10, 15, 20, 25]
    # da = DynamicArray(values)
    # print(da)
    # print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    # print(da.reduce(lambda x, y: (x + y ** 2), -1))
    #
    # print("\n# reduce example 2")
    # da = DynamicArray([100])
    # print(da.reduce(lambda x, y: x + y ** 2))
    # print(da.reduce(lambda x, y: x + y ** 2, -1))
    # da.remove_at_index(0)
    # print(da.reduce(lambda x, y: x + y ** 2))
    # print(da.reduce(lambda x, y: x + y ** 2, -1))
    #
    # print("\n# reduce example 3")
    # da = DynamicArray([])
    # print(da.reduce(lambda x, y: x, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
