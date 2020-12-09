#!/usr/bin/env python
## 
## @file    readSBML.py
## @brief   Similar to validateSBML, but without the validation
## @author  Sarah Keating
## @author  Ben Bornstein
## 
## 
## This file is part of libSBML.  Please visit http://sbml.org for more
## information about SBML, and the latest version of libSBML.
## 

import sys
import time
import os
import os.path
from libsbml import *

def main (args):
  """Usage: network filename
  """
  
  if (len(args) != 2):
      print("Usage: network filename");
      return 1;
  
  filename = args[1];
  ignore_filter = False;# True; 
  ignore_reversibility = False;#True;
  filter_filename = "test/sif_core/allfilters_con_c.dat";
  
  #open filter list file
  filter_file = open(filter_filename, "r");
  #create a list of elements to filter
  filter_list = filter_file.read().lower().splitlines();
  current = time.clock();
  document = readSBML(filename);
  
  errors = document.getNumErrors();
   
  document.printErrors();
  
  model = document.getModel();
  listOfReactions = model.getListOfReactions();
  numreactions = model.getNumReactions();
  for reaction1 in listOfReactions:
	  
	  #get list of Products (and Reactants if the reaction is reversible)
	  listOfReactantsAndProducts = reaction1.getListOfProducts().clone();
	  if ignore_reversibility or reaction1.getReversible():
		listOfReactantsAndProducts.appendFrom(reaction1.getListOfReactants());

	  isolated = 1;
	  for element1 in listOfReactantsAndProducts:
		  elem1_species = element1.getSpecies();		  	  		  
		  if (ignore_filter or (decode_sbml(elem1_species).lower() not in filter_list)):
			  listOfReactions2 = listOfReactions.clone();
			  listOfReactions2.remove(reaction1.id); #remove reaction1 to avoid checking against itself
			  for reaction2 in listOfReactions2:
				  #get list of Reactants (and Products if the reaction is reversible)
				  listOfReactantsAndProducts2 = reaction2.getListOfReactants().clone();
				  if ignore_reversibility or reaction2.getReversible():
					listOfReactantsAndProducts2.appendFrom(reaction2.getListOfProducts());
				  linked = 0;
				  for element2 in listOfReactantsAndProducts2:
					  elem2_species = element2.getSpecies();
					  if ignore_filter or (decode_sbml(elem2_species).lower() not in filter_list):
						  if element1.species == element2.species:
							  linked = 1;
				  if linked == 1:
					  isolated = 0;
					  link = reaction1.id+"\tlinkedWith\t"+reaction2.id;
					  print decode_sbml(link);
	  if isolated == 1:
		  print decode_sbml(reaction1.id);

  return errors;

def decode_sbml(texto):
	return texto.replace("__45__", "-").replace("__46__", ".").replace("__43__", "+").replace("_1","1").replace("_2","2").replace("_3","3").replace("_4","4").replace("_5","5").replace("_6","6").replace("_7","7").replace("_8","8").replace("_9","9");


if __name__ == '__main__':
  main(sys.argv)  
