 #!/usr/bin/python
import json
import sys
import getopt
import csv


def createFailureLog(input_data: str, output_file: str):
#    csv_columns = ['dimensioner', 'file', 'timestamp']
    result_list = []
    with open(input_file) as f:
        data = json.load(f)
        for result in data.get('results'):
            result_list.append({
                'serialnbr': data.get('serial'),
                'vdom': data.get('vdom'),
                'policyid': result.get('policyid'),
                'srcintf': ','.join([val.get('name') for val in result.get('srcintf')]),
                'dstintf': ','.join([val.get('name') for val in result.get('dstintf')]),
                'srcaddr': ','.join([val.get('name') for val in result.get('srcaddr')]),
                'dstaddr': ','.join([val.get('name') for val in result.get('dstaddr')])
            }
            )
    try:
        with open(output_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in result_list:
                writer.writerow(data)
    except IOError:
        print("I/O error")


def main(argv):
    input_file = ''
    output_file = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('transform.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
    print('Input file is "', input_file)
    print('Output file is "', output_file)
    transform(input_file, output_file)


if __name__ == "__main__":
    main(sys.argv[1:])
