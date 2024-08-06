list_positive_integer = [
    (0, 1),
    (23, 45),
    (123, 456789),
    (456789, 123),
    (90123, 45678)]

list_positive_big_integer = [
    (999, 1),
    (1, 999),
    (9999999999999999999999999999999, 0),
    (0, 9999999999999999999999999999999),
    (9999999999999999999999999999999, 1),
    (1, 9999999999999999999999999999999),
    (999999999999999, 999999999999999),
    (9999999999999999999999999999999, 9999999999999999999999999999999)]

list_negative_positive_integer = [(-1, 1),
                                  (23, -45),
                                  (-678, 901),
                                  (2345, -6789),
                                  (-10234, 56789)]

list_negative_negative_integer = [(-0, -1),
                                  (-23, -45),
                                  (-678, -910),
                                  (-1234, -5678),
                                  (-90123, -45678)]

list_negative_big_integer = [(-999, 1),
                             (1, -999),
                             (-9999999999999999999999999999999, 0),
                             (0, -9999999999999999999999999999999),
                             (-9999999999999999999999999999999, 1),
                             (1, -9999999999999999999999999999999),
                             (-999999999999999, 999999999999999),
                             (9999999999999999999999999999999, -9999999999999999999999999999999)]

list_positive_real_numbers = [(1.12345678, 1.12345678),
                              (0.0, 0.98765432),
                              (3.0, 0.456789),
                              (9.99999999, 0.00000001),
                              (0.00000001, 9.99999999)]

list_negative_real_numbers = [(-1.12345678, 1.12345678),
                              (0.12345678, -0.98765432),
                              (-0.98765432, 0.12345678),
                              (-9.99999999, 0.00000001),
                              (-9.99999999, -0.12345678),
                              (-0.00000001, 9.99999999)]

list_zero_positive_real_numbers = [
    (0, 0.0),
    (0, 1.234456),
    (0.98765432, 0.0),
    (0, 0.00000001),
    (0.00000001, 0)
]

list_zero_negative_real_numbers = [
    (0, -0.0),
    (0, -1.234456),
    (-0.98765432, 0.0),
    (0, -0.00000001),
    (-0.00000001, 0)
]

list_zero_division_real_numbers = [
    (0, -1.234456),
    (-0.98765432, 0.0),
    (0, -0.00000001),
    (-0.00000001, 0)
]

list_scientific_notation_positive = [
    ("1e1", "1e1",
     "2e34, 5e67")
]

list_infinity_positive = [
    ("1e234", "1e123"),
    ("-1e234", "-1e123")
]

list_infinity_negative = [
    ("1e234", "-1e123"),
    ("-1e234", "1e123")
]
