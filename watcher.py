from subprocess import getstatusoutput
import re


def get_output():
    status, output = getstatusoutput('/usr/bin/bbb-conf --status')
    return status, output


def check_output(output: str):
    for line in output.split('\n'):
        r = re.search('.+\[.+\-\s+(\w+)\]', line)
        #todo: check r.group(1)


def check_result(status, output):
    if status == 0:
        check_output(output)


if __name__ == '__main__':
    status, output = get_output()
    check_result(status, output)
