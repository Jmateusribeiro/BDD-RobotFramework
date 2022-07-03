from settings import reports_dir
from internal.utils import get_feature_files
from internal.suite_runner import SuiteRunner
from internal.robot_suite import generate_suites


def main():

    feature_files = get_feature_files()

    suites = generate_suites(feature_files)

    runner = SuiteRunner(*suites)
    runner.run_suites(reports_dir)


if __name__ == '__main__':
    main()
