def divisible_by(number, divised_by):
    return number % divised_by == 0

def convert(number):
    divisible_by_3 = divisible_by(number, 3)
    divisible_by_5 = divisible_by(number, 5)
    divisible_by_7 = divisible_by(number, 7)
    result = []
    if divisible_by_3:
        result.append("Pling")
    if divisible_by_5:
        result.append("Plang")
    if divisible_by_7:
        result.append("Plong")
    if len(result):
        return "".join(result)
    return str(number)