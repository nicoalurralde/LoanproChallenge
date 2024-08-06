from python_on_whales import docker, DockerException
from utils.python_calculation import PythonCalculation as pyc


class Calculator:

    def __init__(self, operation_type: str):
        """We don't do any operation string validation here
        That would stop us from doing negative tests
        """
        self.operation_type = operation_type
        self.container = "public.ecr.aws/l4q9w4c5/loanpro-calculator-cli"
        self.pull_container()

    def pull_container(self):
        docker.pull(self.container)

    def operation(self, number_a: float | str, number_b: float | str) -> str:
        """Takes any of the allowed operations and runs
         the Docker container with the parameters.
         returns string
        """
        if self.operation_type in ["add", "subtract", "multiply", "divide"]:
            output = docker.run(self.container, [self.operation_type, number_a, number_b], remove=True)
        else:
            raise ValueError("Operation not supported: " + self.operation_type)
        result = output.split(" ")[1]
        if result not in ("∞", "-∞"):
            result = pyc.format_float(float(result))
        return result

    def operation_raw(self, number_a: str, number_b: str) -> str:
        """Takes any operations and runs the Docker container with the parameters.
         Has no validations
         returns string
        """
        try:
            result = docker.run(self.container, [self.operation_type, number_a, number_b], remove=True)
            return result
        except DockerException as e:
            return str(e)


