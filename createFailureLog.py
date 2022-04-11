 #!/usr/bin/python
#import json
import datetime
import sys
import getopt
import csv


def createFailureLog(_dimensioner: str, _erroredFile: str, _epoch_time: str, output_file: str):
    csv_columns = ['dimensioner', 'file', 'timestamp']
    result_list = []
    with open(input_file) as f:
        result_list.append({
            'dimensioner': _dimensioner,
            'file': _erroredFile,
            'timestamp': datetime.datetime.fromtimestamp( _epoch_time ) 
        })
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
        opts, args = getopt.getopt(argv, "hd:e:t:o:", ["ddimensioner=", "efile=", "ttime=", "ofile="])
    except getopt.GetoptError:
        print('transform.py -d <dimensioner> -e <errorFile> -t <ttime> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -d <dimensioner> -e <errorFile> -t <ttime> -o <outputfile>')
            sys.exit()
        elif opt in ("-d", "--ddimensioner"):
            dimensioner = arg
        elif opt in ("-e", "--efile"):
            erroredFile = arg
        elif opt in ("-t", "--ttime"):
            epoch_time = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
    print('dimensioner is "', dimensioner)
    print('erroredFile is "', erroredFile)
    print('epoch_time is "', epoch_time)
    print('Output file is "', output_file)
    createFailureLog(dimensioner, erroredFile, epoch_time, output_file)


if __name__ == "__main__":
    main(sys.argv[1:])
