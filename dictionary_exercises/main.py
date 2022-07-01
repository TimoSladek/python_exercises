d = {k: v for (k, v) in [("name", "Elie"), ("job", "Instructor")]}

new_d = {k: v for (k, v) in tuple(zip(["CA", "NJ", "RI"], ["California", "New Jersey", "Rhode Island"]))}

vowels = {k: 0 for k in ["a", "e", "i", "o", "u"]}

alphabet = {k: chr(k+64) for k in range(1, 27)}