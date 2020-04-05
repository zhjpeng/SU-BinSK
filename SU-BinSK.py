#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import gzip


# assign primary parameters
argparser = argparse.ArgumentParser(description = 'A Suit of Utilities for Bioinformatic Skills')

commands = argparser.add_subparsers(dest = 'command', title = 'Commands')

sort_chromosome_ID = commands.add_parser('sort_chr', help = 'sort messy chromosomes as specified')

sort_chromosome_ID.add_argument('-i', type = str, required = True, dest = 'chr_name', help = 'File contained specified order of chromosomes rank')
sort_chromosome_ID.add_argument('-f', type = str, required = True, dest = 'ref_seq', help = 'Name of the input fasta file')
sort_chromosome_ID.add_argument('-w', type = int, required = False, dest = 'line_width', default = 80, help = 'the wideth of output file, default is 80')

args = argparser.parse_args()

# define function to load fasta file into dict

def multi_genes_dict(fasta_a):

    seq_line = ""
    seq_name = ""
    seq_dict = {}

    if fasta_a.endswith(".gz"):
        opener = gzip.open
    else:
        opener = open

    for item1 in opener(fasta_a):
        item2 = item1.strip()

        if item2[0] == ">" and seq_line == "":
            seq_name = item2.split('>')[1]

        elif item2[0] == ">" and seq_line != "":
            seq_dict[seq_name] = seq_line
            seq_line = ""

            seq_name = item2.split('>')[1]

        elif item2[0] != ">":
            seq_line = seq_line + item2

        else:
            print("Error: unexpected condition")

    seq_dict[seq_name] = seq_line

    return seq_dict


# define function to load single-column data into list

def rank_single_list(txt_a):

    record_single = []

    for item1 in open(txt_a):
        item2 = item1.strip()

        if item2[0] == "#":
            next

        else:
            record_single.append(item2)

    return record_single


## Task 1: sort messy chromosomes as specified order

ci = args.chr_name
rs = args.ref_seq
lw = args.line_width

for item1 in rank_single_list(ci):
    item2 = multi_genes_dict(rs)[item1]

    print(">",item1,sep="")

    i = 0
    while i < len(item2):
        print(item2[i:i + lw])
        i += lw
