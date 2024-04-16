#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:52:01 2023

Rosalind GC counter exercise

1. read in fasta file and parse into a suitable data type

2. calculate GC, import the function to do this 
from your rosalind utils

3. write a find max GC function

4. section that ties this together and prints out your result

@author: yin
"""
from rosalind_utils import gc_calculator

def fasta_parse_to_dict(fastafile):
    """
    Function that takes in a fastafile and parses it
    into a dictionary of form {header: seq}
    
    :param fastafile: str, name of your input file
    
    :returns seqdict: dict, dictionary of form {header: seq}
    """
    seqdict = {}
    with open(fastafile, 'r') as infile:
        for line in infile:
            line = line.strip()
            if line.startswith('>'):
                header = line[1:]
                seqdict[header] = ''
            else:
                seqdict[header] += line 
    return seqdict


def gcdict_from_seqdict(sequencedict):
    """
    Function calculates GC content of each sequence
    Saves to a dictionary

    :param sequencedict: dict, dict with sequences

    :returns gcdict: dict, of form {header:GC content}
    """
    gcdict = {}
    for header, seq in sequencedict.items():
        gcdict[header] = gc_calculator(seq)
    return gcdict


def get_key_of_max_gc(gcdict):
    """
    Returns the key corresponding to the sequence with
    maximum GC content 
    
    :param sequencedict: dict
    
    :returns maxheader: str
    """
    maxkey = max(gcdict, key=gcdict.get)
    return maxkey


def get_key_of_max_gc_long(gcdict):
    """
    Returns the key corresponding to the sequence with
    maximum GC content 
    
    :param sequencedict: dict
    
    :returns maxkey: str
    """
    maxval = 0
    maxkey = ''
    
    for key, val in gcdict.items():
        if val > maxval:
            maxval = val
            maxkey = key
            
    return maxkey

if __name__ == "__main__":
    
    inputfile = 'seqs.fasta'
    
    fasta_dict = fasta_parse_to_dict(inputfile)
    gc_dict = gcdict_from_seqdict(fasta_dict)
    maxkey = get_key_of_max_gc(gc_dict)
    
    print(f'{maxkey}\n{gc_dict[maxkey]}')
    
    
    

