from argparse import ArgumentParser
import os
from datetime import datetime, timedelta

class Main:

    def show_help(self):
        print('''    usage: test.py [-h] [-i] [-o]

        options:
            -h, --help show this help message and exit
            -i, --input Specify an input file
            -o, --output Specify an output file''')
    
    def validate_m(self, m):
        if not m:
            raise ValueError("required")
        if m != "0" and m != "1":
            raise ValueError("invalid value")
    
    def validate_p(self, m, p):
        if not p:
            raise ValueError("required")
        if m == "0":
            if p.endswith(".tar.gz"):
                raise ValueError("invalid value")
        else:
            if not p.endswith(".tar.gz"):
                raise ValueError("invalid value")
    
    def validate_s(self, s):
        if not s:
            raise ValueError("required")
    
    def validate_sd(self, sd):
        if (not sd):
            raise ValueError("required")
        try:
            datetime.strptime(sd, "%Y%m%d")
        except ValueError:
            raise ValueError("invalid value")

    def validate_d(self, m, d, d_sd):
        if m == "0": 
            if not d:
                raise ValueError("required")
            try:
                int(d)
            except Exception:
                raise ValueError("invalid value")
            if int(d) <= 0:
                raise ValueError("invalid value")
            added = d_sd + timedelta(days=int(d))
            if added.month > d_sd.month:
                raise ValueError("invalid value")
    
    def validate_t(self, m, t):
        if m == "1": 
            if not t:
                raise ValueError("required")
            try:
                int(t)
            except Exception:
                raise ValueError("invalid value")
            if int(d) <= 0:
                raise ValueError("invalid value")
            added = d_sd + timedelta(days=int(d))
            if added.month > d_sd.month:
                raise ValueError("invalid value")
    
    def get_end_date(self, start_date, end_date, times):
        diff = (end_date - start_date).days + 1 # 開始日含むため+1
        total_days = diff * times
        end_day = start_date + timedelta(days=total_days - 1) # 開始日含むため-1
        print(end_day)

    def main(self):

        arg_parser = ArgumentParser(add_help=False)

        arg_parser.add_argument("-m", required=False)
        arg_parser.add_argument("--mode", required=False)
        arg_parser.add_argument("-p", required=False)
        arg_parser.add_argument("--path", required=False)
        arg_parser.add_argument("-s", required=False)
        arg_parser.add_argument("--s-no", required=False)
        arg_parser.add_argument("-d", required=False)
        arg_parser.add_argument("--day", required=False)
        arg_parser.add_argument("-S", required=False)
        arg_parser.add_argument("--S-d", required=False)
        arg_parser.add_argument("-t", required=False)

        parsed_args, unknown = arg_parser.parse_known_args()

        if '-h' in unknown or '--help' in unknown:
            self.show_help()
        
        #print(parsed_args)

        m = parsed_args.m if parsed_args.m else parsed_args.mode
        p = parsed_args.p if parsed_args.p else parsed_args.path
        s = parsed_args.s if parsed_args.s else parsed_args.s_no
        d = parsed_args.d if parsed_args.d else parsed_args.day
        sd = parsed_args.S if parsed_args.S else parsed_args.S_d
        
        if m == "0" and not p:
            p = "/tmp"
        if m == "0" and not d:
            d = 1

        #self.validate_m(m)
        #self.validate_p(p)
        #self.validate_s(s)

        #self.validate_sd(sd)
        #d_sd = datetime.strptime(sd, "%Y%m%d")

        #self.validate_d(m, d, d_sd)
        
        self.get_end_date(datetime.strptime("20220101", "%Y%m%d"), datetime.strptime("20220103", "%Y%m%d"), 2)


Main().main()
