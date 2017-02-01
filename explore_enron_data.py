#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print "How many data points (people) are in the dataset?(146) ", \
        len(enron_data.keys())


print "For each person, how many features are available?(21) ", \
        len(enron_data[enron_data.keys()[0]].keys())

poi_count = 0
for k in enron_data:
    if enron_data[k]["poi"] == 1:
        poi_count += 1
print "How many POIs are there in the E+F dataset?(18) ", \
        poi_count

print "What is the total value of the stock belonging to James Prentice?", \
   enron_data['PRENTICE JAMES']['total_stock_value']

print "How many email messages do we have from Wesley Colwell to persons of interest?", \
   enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print "What’s the value of stock options exercised by Jeffrey K Skilling?", \
   enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print "How much money did that person get? Lay, Skilling and Fastow", \
   enron_data['SKILLING JEFFREY K']['total_payments']

print "How much money did that person get? FASTOW ANDREW S", \
   enron_data['FASTOW ANDREW S']['total_payments']

print "How much money did that person get? KILLING JEFFREY K", \
   enron_data['SKILLING JEFFREY K']['total_payments']

print "How much money did that person get? LAY KENNETH L", \
   enron_data['LAY KENNETH L']['total_payments']


countSalary =0
for i in enron_data:
    if enron_data[i]["salary"]!='NaN':
        countSalary+=1
print "how many people have a quantified salary",\
      countSalary

countemail =0
for j in enron_data:
    if enron_data[j]["email_address"]!='NaN':
         countemail+=1
print "how many email_address have a quantified salary",\
     countemail

count_total_payments =0
for j in enron_data:
    if enron_data[j]["total_payments"]=='NaN':
         count_total_payments+=1
print "how many people have a total_payments",\
     count_total_payments

print   count_total_payments/146.0


countpoi =0
for m in enron_data:
    if enron_data[m]["poi"]=='NaN':
         countpoi+=1
print "How many POIs in the E+F dataset have “NaN” for their total payments?",\
         countpoi
print "What percentage of POI’s as a whole is this?",\
      countpoi/146.0

print 31/156.0
   
