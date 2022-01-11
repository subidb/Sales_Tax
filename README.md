# Sales_Tax


To run the program:
*git https://github.com/subidb/Sales_Tax.git

*cd Sales_Tax

*python sales_tax.py

Problem:

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

### INPUT:
Input 1:
> 1 book at 12.49
> 1 music CD at 14.99
> 1 chocolate bar at 0.85
Input 2:
> 1 imported box of chocolates at 10.00
> 1 imported bottle of perfume at 47.50
Input 3:
> 1 imported bottle of perfume at 27.99
> 1 bottle of perfume at 18.99
> 1 packet of headache pills at 9.75
> 1 box of imported chocolates at 11.25
### OUTPUT
Output 1:
> 1 book: 12.49
> 1 music CD: 16.49
> 1 chocolate bar: 0.85
> Sales Taxes: 1.50
> Total: 29.83
Output 2:
> 1 imported box of chocolates: 10.50
> 1 imported bottle of perfume: 54.65
> Sales Taxes: 7.65
> Total: 65.15
Output 3:
> 1 imported bottle of perfume: 32.19
> 1 bottle of perfume: 20.89
> 1 packet of headache pills: 9.75
> 1 imported box of chocolates: 11.85
> Sales Taxes: 6.70
> Total: 74.68


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
