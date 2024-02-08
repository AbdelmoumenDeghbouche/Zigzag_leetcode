class Solution:
    def create_dynamic_array(self, n, m):
        # Create an empty list to hold the rows
        dynamic_array = []

        # Create each row and append it to the dynamic array
        for i in range(n):
            row = [0] * m  # Initialize each row with zeros, you can modify as needed
            dynamic_array.append(row)

        return dynamic_array


    def countNumRows(self, s: str, numRows: int) -> int:
        numOfColoms = 1
        numberOfcharUsed = numRows + 1
        while numberOfcharUsed < len(s):
            if numberOfcharUsed % numRows == 0:
                numberOfcharUsed += numRows
                numOfColoms += 1
            else:
                numOfColoms += 1
                numberOfcharUsed += 1
        numOfColoms += 1
        return numOfColoms

    def final_convert_zigzag(self,new_matrix) -> str:
        s = ""
        for i in range(len(new_matrix)):
            for j in range(len(new_matrix[i])):
                if new_matrix[i][j] != 0:
                    s += new_matrix[i][j]
                    print(s)
        return s

    def convert(self, s: str, numRows: int) -> str:
        charsDone = False
        i = 0
        consumed_chars = 0
        arr_res = self.create_dynamic_array(numRows, self.countNumRows(s, numRows))
        while not charsDone:
            temp_holdre_of_consumed_chars = consumed_chars
            for j in range(numRows):
                if consumed_chars == len(s):
                    break
                arr_res[j][i] = s[j + temp_holdre_of_consumed_chars]
                consumed_chars += 1
            for k in range(numRows - 2):
                if consumed_chars == len(s):
                    break
                arr_res[numRows - (k + 2)][k + i + 1] = s[
                    temp_holdre_of_consumed_chars + k + numRows
                ]
                consumed_chars += 1
            print(arr_res)

            i = i + numRows - 1

            if consumed_chars == len(s):
                charsDone = True
        return self.final_convert_zigzag(arr_res)