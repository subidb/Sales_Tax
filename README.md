# Sales_Tax


To run the program:

git https://github.com/subidb/Sales_Tax.git

cd Sales_Tax

python sales_tax.py

## Problem: 

Basic sales tax is applicable at a rate of 10% on all goods, except books,
food, and medical products that are exempt. Import duty is an additional
sales tax
applicable on all imported goods at a rate of 5%, with no exemptions. When I
purchase items I receive a receipt which lists the name of all the items and
their price (including tax), finishing with the total cost of the items,
and the total amounts of sales taxes paid. The rounding rules for sales tax
are that for a tax rate of n%, a shelf price of p contains (np/100 rounded up
to the nearest 0.05) amount of sales tax.

Write an application that prints out the receipt details for these shopping
baskets...




Solution:


Assumptions:

1. Input list of goods are always in the same format :
    1 imported bottle of perfume at 27.99
   i.e * quantity is always at the first,
    *the word "imported" is present for imported goods.
    *price is always at the end with decimal points limited to 2 
   input is a string.
   In this program, the input is already stored in the program, as the input values are set in the problem question.
    However, it could easily adjusted to be user input or imported from a notepad file

2.   According to the question:
  Excempt goods. Imported goods. Tax
        False       False         10%
        False       True          15%
        True        False         0%
        True        True          5%

    I initially assumed that if a product was imported(and not excempt)
     5 % import tax would be applied to get a result and then 10% would be applied to that result
     (1.05x * 1.10) where x is the initial price
     However looking at the output directly doing(1.15x) looks like the required approach. hence that was applied
     
     
 An Item class was created to facilitate the creation of item objects with their values.
 A parser function was used with regex to parse the input and convert them into objects.
 Class functions were used to calculate sales tax, using the attributes of the instances.
