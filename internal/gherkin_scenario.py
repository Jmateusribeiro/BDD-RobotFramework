

class GherkinScenario:

    def __init__(self, gherkin_string):
        self.gherkin_block = gherkin_string.splitlines()
        self.scenario_name = ''
        self.scenario_specification = []
        self.examples = []
        self.examples_dict = []

    def get_gherkin_keywords(self):
        try:
            for line in self.gherkin_block:
                if line.strip().startswith(('Scenario:', 'Scenario Outline:', 'Example:', 'Scenario Template:')):
                    self.scenario_name = line.strip()
                elif line.strip().startswith(('Given', 'When', 'Then', 'And', 'But')):
                    self.scenario_specification.append(line.strip())
                elif line.strip().startswith('|'):
                    example = line.strip()
                    self.examples.append(example[1:-1].strip())
        except Exception as e:
            raise Exception(e.args[0])

        self.validate_scenario_name()
        self.validate_scenario_specification()
        if self.scenario_name.startswith(('Scenario Outline:', 'Scenario Template:')):
            self.validate_examples()
            self.convert_examples_list_to_dict()

    def validate_scenario_name(self):
        if self.scenario_name == '':
            raise Exception("Error parsing scenario name."
                            " Should start with: 'Scenario:', 'Scenario Outline:', 'Example:', 'Scenario Template:'")

    def validate_scenario_specification(self):
        if self.scenario_specification == []:
            raise Exception("Error parsing scenario specification. Specification steps should start with "
                            "the following words: 'Given', 'When', 'Then', 'And', ' But'")

    def validate_examples(self):
        if len(self.examples) < 2:
            raise Exception("Error parsing scenario examples. Example table should have the following example: "
                            "Examples:\n| arg 1 | arg 2|\n| exemplo 1| exemplo 2 |")

    def convert_examples_list_to_dict(self):
        # get headers names
        try:
            header_names = self.examples[0].split('|')  # get headers names
            header_names = [i.strip() for i in header_names]

            self.examples.pop(0)

            for line in self.examples:
                values = line.rsplit('|')
                values = [i.strip() for i in values]
                self.examples_dict.append(dict(zip(header_names, values)))
        except Exception as e:
            raise Exception(e.args[0])
