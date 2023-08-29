def arithmetic_arranger(problems, show_results=False):
    allowed_problems = 5
    allowed_operand_length = 4
    allowed_operators = ["+", "-"]
    underline = "-"
    alignment_space = " "
    max_grids = 6

    top_row, bottom_row, underline_row, result_row = list(), list(), list(), list()

    def valid_num_of_problems(problems) -> bool:
        """
        Accepts a list as input
        Returns True or an Error
        """
        if len(problems) > allowed_problems:
            return "Error: Too many problems."
        else:
            return True

    def valid_problem_components(problem_components) -> list:
        """
        Accepts a list as input
        Returns a list of strings or an error.
        """
        # check cases where: more than or less than 2 operands are provided
        if len(problem_components) != 3:
            return ValueError("Invalid number of operands")
        else:
            # separate the components of the problem and check if operands are digits
            try:
                firstOperand = int(problem_components[0])
                secondOperand = int(problem_components[2])
            except ValueError:
                return "Error: Numbers must only contain digits."
            else:
                operator = problem_components[1]
                # check if operator is '+' or '-'
                if operator not in allowed_operators:
                    return "Error: Operator must be '+' or '-'."
                else:
                    # check length of operands against allowed operand length
                    if (
                        len(str(firstOperand)) > allowed_operand_length
                        or len(str(secondOperand)) > allowed_operand_length
                    ):
                        return "Error: Numbers cannot be more than four digits."

                return [firstOperand, secondOperand, operator]

    def appender(
        firstOperand_display, secondOperand_display, underline_display, result_display
    ):
        top_row.append(firstOperand_display)
        bottom_row.append(secondOperand_display)
        underline_row.append(underline_display)
        result_row.append(result_display)

    if valid_num_of_problems(problems=problems) == True:
        for problem in problems:
            # break problem into a list
            problem_components = problem.split()
            processed_components = valid_problem_components(
                problem_components=problem_components
            )
            if type(processed_components) != list:
                return valid_problem_components(problem_components=problem_components)
            else:
                firstOperand = processed_components[0]
                secondOperand = processed_components[1]
                operator = processed_components[2]

                # calculate the result of the problem
                if operator == "+":
                    result = firstOperand + secondOperand
                else:
                    result = firstOperand - secondOperand

            # configure display
            # one of both or both operands are equal to 4
            if (
                len(str(firstOperand)) == allowed_operand_length
                or len(str(secondOperand)) == allowed_operand_length
            ):
                firstOperand_padding = alignment_space * (
                    max_grids - len(str(firstOperand))
                )
                secondOperand_padding = alignment_space * (
                    (max_grids - len(str(secondOperand))) - 1
                )
                firstOperand_display = firstOperand_padding + str(firstOperand)
                secondOperand_display = (
                    operator + secondOperand_padding + str(secondOperand)
                )
                underline_display = underline * len(secondOperand_display)
                result_padding = alignment_space * (
                    len(secondOperand_display) - len(str(result))
                )
                result_display = result_padding + str(result)
                appender(
                    firstOperand_display,
                    secondOperand_display,
                    underline_display,
                    result_display,
                )

            # less than 4 and both operands are equal in length
            elif len(str(firstOperand)) == len(str(secondOperand)):
                firstOperand_padding = alignment_space * 2
                secondOperand_padding = alignment_space
                firstOperand_display = firstOperand_padding + str(firstOperand)
                secondOperand_display = (
                    operator + secondOperand_padding + str(secondOperand)
                )
                underline_display = underline * len(secondOperand_display)
                result_padding = alignment_space * (
                    len(secondOperand_display) - len(str(result))
                )
                result_display = result_padding + str(result)
                appender(
                    firstOperand_display,
                    secondOperand_display,
                    underline_display,
                    result_display,
                )

            # top operand is longer than bottom operand
            elif len(str(firstOperand)) > len(str(secondOperand)):
                firstOperand_padding = alignment_space * 2
                secondOperand_padding = alignment_space * (
                    (len(str(firstOperand)) - len(str(secondOperand))) + 1
                )
                firstOperand_display = firstOperand_padding + str(firstOperand)
                secondOperand_display = (
                    operator + secondOperand_padding + str(secondOperand)
                )
                underline_display = underline * len(secondOperand_display)
                result_padding = alignment_space * (
                    len(secondOperand_display) - len(str(result))
                )
                result_display = result_padding + str(result)
                appender(
                    firstOperand_display,
                    secondOperand_display,
                    underline_display,
                    result_display,
                )

            # bottom operand is longer than top operand
            elif len(str(firstOperand)) < len(str(secondOperand)):
                secondOperand_padding = alignment_space
                firstOperand_padding = alignment_space * (
                    (len(str(secondOperand)) - len(str(firstOperand))) + 2
                )
                firstOperand_display = firstOperand_padding + str(firstOperand)
                secondOperand_display = (
                    operator + secondOperand_padding + str(secondOperand)
                )
                underline_display = underline * len(secondOperand_display)
                result_padding = alignment_space * (
                    len(secondOperand_display) - len(str(result))
                )
                result_display = result_padding + str(result)
                appender(
                    firstOperand_display,
                    secondOperand_display,
                    underline_display,
                    result_display,
                )
            else:
                print("Error")
    else:
        return valid_num_of_problems(problems=problems)

    if show_results:
        output = [top_row, bottom_row, underline_row, result_row]
    else:
        output = [top_row, bottom_row, underline_row]

    result_string = ""
    for row in output:
        result_string += "    ".join(row) + "\n"

    return result_string.rstrip()
