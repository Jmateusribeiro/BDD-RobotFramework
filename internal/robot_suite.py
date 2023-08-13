from robot.api import TestSuite
from internal.utils import find_variables, get_robot_files
import re
from settings import feature_files_dir, keywords_dir, delimiters, scenario_outline_chars
from internal.gherkin_scenario import GherkinScenario


class RobotSuite(TestSuite):

    def create_suite(self, feature_name):
        self.name = feature_name.strip()

    def add_test(self, test_case):

        scenario_name = test_case.scenario_name
        scenario_specification = test_case.scenario_specification
        examples = test_case.examples_dict

        try:

            robot_files = get_robot_files()

            for file in robot_files:
                keywords_file = (keywords_dir+file).replace("\\", "/")
                self.resource.imports.resource(keywords_file)

            if scenario_name.startswith(('Scenario Outline:', 'Scenario Template:')):
                for example in examples:
                    test_name = scenario_name.split(':', 1)[1].strip()
                    test = self.tests.create(test_name)
                    for keyword in scenario_specification:
                        arguments = find_variables(keyword)
                        for agr in arguments:
                            variable = "<" + agr + ">"
                            keyword = keyword.replace(variable, example[agr])
                        test.body.create_keyword(keyword)
            else:
                test_name = scenario_name.split(':', 1)[1].strip()
                test = self.tests.create(test_name)
                for keyword in scenario_specification:
                    test.body.create_keyword(keyword)

        except Exception as e:
            raise Exception(e.args[0])


def generate_suites(feature_files):
    suites = []
    try:
        for file in feature_files:
            with open(feature_files_dir + file, encoding="utf-8") as feature_file:
                gherkin_string = feature_file.read()

            test_scenarios, feature_name = find_scenarios(gherkin_string, delimiters)

            suite = RobotSuite()
            suite.create_suite(feature_name)

            for test in test_scenarios:
                test_case = GherkinScenario(test)
                test_case.get_gherkin_keywords()

                suite.add_test(test_case)

            suites.append(suite)
    except Exception as e:
        raise Exception(e.args[0])

    return suites


def find_scenarios(gherkin_string, separators):

    try:
        test_scenarios = re.split(separators, gherkin_string)

        if test_scenarios[0].startswith('Feature'):
            feature_name = test_scenarios[0].splitlines()[0] #get first line, ignore comments
            test_scenarios.pop(0)
            for i in range(len(test_scenarios)):
                if all(x in test_scenarios[i] for x in scenario_outline_chars):
                    separator = 'Scenario Outline:'
                else:
                    separator = 'Scenario:'
                test_scenarios[i] = separator + test_scenarios[i]
        else:
            raise Exception("Feature file should start with Feature Name")

    except Exception as e:
        raise Exception(e.args[0])

    return test_scenarios, feature_name
