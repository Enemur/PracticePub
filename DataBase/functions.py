def getFunctions(storedFunction):
    class Inner:
        @staticmethod
        @storedFunction
        def set_equation(equation: str, decision: str): pass

        @staticmethod
        @storedFunction
        def get_equation_by_id(equationId: int): pass

    return Inner
