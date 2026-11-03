
##2. Progressive Electricity Billing

  ## 1. Problem Statement
Calculate household electricity bills using multiple consumption slabs, fixed charges, surcharges, and rebates.
Compare bills across months and identify unusual increases.

##2. Algorithm
1. Start.
2. Read the number of months.
3. For each month, read units consumed.
4. Calculate energy charges using the applicable slabs.
5. Add fixed charge and 5% surcharge; subtract ■20 rebate if units are below 100.
6. Store and display the bill.
7. From the second month onward, compare the bill with the previous month's bill.
8. If the increase is greater than 50%, report an unusual increase.
9. Stop
    
##3. Mermaid Flowchart Code

flowchart TD
1. N0(["START"])<br>
2.N1["Input number of months and monthly units"]<br>
 3.N0 --> N1<br>
 4.N2["Calculate slab-wise energy charge"]<br>
 5.N1 --> N2<br>
 6.N3["Add fixed charge and surcharge; apply rebate if eligible"]<br>
 7.N2 --> N3<br>
 8.N4["Calculate and store the monthly bill"]<br>
 9.N3 --> N4<br>
 10.N5{"Is this not the first month?"}<br>
 11.N4 --> N5<br>
 12.N6["If yes, compare with previous bill and flag increase > 50%"]<br>
 13.N5 -->|Yes / No as applicable| N6<br>
 14.N7["Display bill; repeat for remaining months"]<br>
 15.N6 --> N7<br>
 16.N8(["STOP"])<br>
 17.N7 --> N8<br>

##4. Pseudocode
1.START<br>
2.INPUT number_of_months<br>
3.bills = empty list<br>
4.FOR each month<br>
 5.INPUT units<br>
 6.IF units <= 100<br>
 7.energy = units * 2<br>
 8.ELSE IF units <= 200<br>
 9.energy = 100 * 2 + (units - 100) * 3<br>
 10.ELSE<br>
 11.energy = 100 * 2 + 100 * 3 + (units - 200) * 5<br>
 12.END IF<br>
 13.bill = energy + 50 + energy * 0.05<br>
 14.IF units < 100<br>
 15.bill = bill - 20<br>
 16.END IF<br>
 17.ADD bill TO bills<br>
 18.DISPLAY bill<br>
 19.IF this is not the first month<br>
 20.increase_percent = (current - previous) / previous * 100<br>
 21.IF increase_percent > 50<br>
 22.DISPLAY "Unusual increase"<br>
 23.END IF<br>
 24.END IF<br>
25.END FOR<br>
26.STOP<br>

##5. Sample Input:
1.Enter number of months: 3<br>
Enter units consumed: 80<br>
Enter units consumed: 150<br>
Enter units consumed: 250<br>
##6. Sample Output:
1.Month 1 Bill: Rs. 238.0<br>
Month 2 Bill: Rs. 523.0<br>
Unusual increase detected<br>
Month 3 Bill: Rs. 1039.5<br>
Unusual increase detected<br>


##7. Conclusion:
The program calculates monthly electricity bills using progressive slabs and additional charges. It also compares bills
and detects unusually large increases.
