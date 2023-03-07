def in_a_but_not_in_b(a: list, b: list, case_sensitive = False) -> list:
    if case_sensitive:
        return [x for x in a if x not in b]
    else:
        not_in_b = []
        for x in a:
            in_b = False
            for y in b:
                if x.upper() == y.upper():
                    in_b = True
            if not in_b:
                not_in_b.append(x)
        return not_in_b