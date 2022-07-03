from robot.api import ResultWriter
from internal.utils import create_folder, remove_warnings


class SuiteRunner:
    def __init__(self, *suites):
        self.suites = suites
        self.files = []

    def run_suites(self, reports_dir):

        report_folder = create_folder(reports_dir)

        try:
            for index, suite in enumerate(self.suites):
                suite.run(output=report_folder + "/output{}.xml".format(index))
                remove_warnings(report_folder + "/output{}.xml".format(index))

                self.files.append(report_folder + "/output{}.xml".format(index))
        except Exception as e:
            print(e.message, e.args)

        if len(self.suites) > 1:
            suite_name = 'Features'
        else:
            suite_name = self.suites[0].name

        ResultWriter(*self.files).write_results(
            report=report_folder + '/output.html',
            log=report_folder + '/log.html',
            logtitle='Report',
            reporttitle='Report Detail',
            name=suite_name
        )
