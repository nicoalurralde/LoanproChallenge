import numpy as np


class PythonCalculation:

    @staticmethod
    def format_float(num) -> str:
        formatted_num = np.format_float_positional(num, precision=8, trim="-")
        if formatted_num == "-0":
            return "0"
        return formatted_num
