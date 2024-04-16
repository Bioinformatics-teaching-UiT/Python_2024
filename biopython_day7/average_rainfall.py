#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 10:52:18 2023

Average rainfall exercise

@author: yin
"""

# function to read in rainfall and output to dict

def read_rainfall_to_dict(inputfile):
    """
    Reads in a text file with rainfall data.
    Outputs data as a dictionary.

    Parameters
    ----------
    inputfile : str
        name of file with rainfall data

    Returns
    -------
    rainfall_dict : dict
        contains rainfall data of form {month:rainfall}

    """
    rainfall_dict = {} # initialise dict container
    
    with open(inputfile, 'r') as infile:
        for line in infile:
            if not line.startswith("Average"):
                data = line.split() # ['Jan', '81.2']
                rainfall_dict[data[0]] = float(data[1])
    return rainfall_dict


def write_rainfall_dict_to_file(outputfile, data_dict):
    """
    Function takes in new file name and rainfall dict,
    writes the data in rainfall dict as sentences into
    your new file.

    Parameters
    ----------
    outputfile : str
        file to write rainfall sentences in
    data_dict : dict
        contains rainfall data of form {month:rainfall}

    Returns
    -------
    None.
    """
    with open(outputfile, 'w') as outfile:
        # loop over your data dictionary
        for key, val in data_dict.items():
            sentence = f'The avg. rainfall in {key} was {val}.\n'
            outfile.write(sentence)

### actual doing part
if __name__ == '__main__':
    original_file = 'rainfall.txt'
    sentence_file = 'rainfall_sentences.txt'

    rainfall_data_dict = read_rainfall_to_dict(original_file)

    write_rainfall_dict_to_file(sentence_file, rainfall_data_dict)
      






