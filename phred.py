#!/usr/bin/env python

sanger_dict = {'!': 0}

illumina_dict = {'@': 0}

class PhredHelper:
    def __init__(self, offset=33):
        self.offset = offset
        if self.offset == 33:
            self.dictionary = sanger_dict
        elif self.offset == 64:
            self.dictionary = illumina_dict
        else:
            sys.stderr.write("Invalid offset value! Using default (Sanger 'Q+33')")
            self.offset = 33
            self.dictionary = sanger_dict

    def char_to_int(self, char):
        return(self.dictionary['!'])
