class Calculation:
    @staticmethod
    def get_probability(*odds: float) -> float:
        return sum(
            [1/x for x in odds if x is not None]
        )

    @staticmethod
    def check(*odds: float) -> bool:
        return __class__.get_probability(*odds) < 1

    @staticmethod
    def distribution(amount: float, *odds: float, rounding: int=2, probability: float=None):
        if not probability:
            probability = __class__.get_probability(*odds)
        return [round(((1/x/probability) * amount), rounding) for x in odds if x is not None]

    @staticmethod
    def calculation(amount: float, *odds: float, rounding: int=2) -> dict:
        prob = __class__.get_probability(*odds)
        distrib = __class__.distribution(amount, *odds, rounding=rounding, probability=prob)
        profits = [
            (
                money * odds[i],
                round((((money * odds[i]) * 100 /amount)-100), 1),
            )
            for i, money in enumerate(distrib)
        ]
        return {
            'profitable': True if prob < 1 else False,
            'probability': prob,
            'distribution': distrib,
            'profits': profits,
        }
