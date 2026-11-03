###3. Hospital Billing and Patient Classification

###1. Problem Statement
Process consultation, diagnostic, and treatment charges, apply concessions, validate billing constraints, and classify
patients according to a supplied payment policy.

##2. Algorithm
1. Start.
2. Read patient name, age, and insurance status.
3. Set consultation, diagnostic, and treatment charges.
4. Calculate the total bill.
5. If insurance is valid, apply 20% discount; otherwise, if age is at least 60, apply 10%; otherwise, no discount.
6. Calculate final bill and classify the patient.
7. Display the bill.
8. Stop.

###3. Mermaid Flowchart Code
flowchart TD
1. N0(["START"])<br>
 N1["Input patient name, age, and insurance status"]<br>
 N0 --> N1<br>
 N2["Add consultation, diagnostic, and treatment charges"]<br>
 N1 --> N2<br>
 N3{"Is insurance valid?"}<br>
 N2 --> N3<br>
 N4["Yes → Apply 20% discount; No → Check age"]<br>
 N3 -->|Yes / No as applicable| N4<br>
 N5{"Is age 60 or above?"}<br>
 N4 --> N5<br>
 N6["Yes → Apply 10%; No → No discount"]<br>
 N5 -->|Yes / No as applicable| N6<br>
 N7["Calculate final bill and display patient category"]<br>
 N6 --> N7<br>
 N8(["STOP"])<br>
 N7 --> N8<br>

 
###4. Pseudocode


START<br>
INPUT name, age, insurance_status<br>
consultation = 500<br>
diagnostic = 1000<br>
treatment = 3000<br>
total = consultation + diagnostic + treatment<br>
IF insurance_status is "yes"<br>
 discount = total * 0.20<br>
 category = "Insured Patient"<br>
ELSE IF age >= 60<br>
 discount = total * 0.10<br>
 category = "Senior Citizen"<br>
ELSE<br>
 discount = 0<br>
 category = "Normal Patient"<br>
END IF<br>
final_bill = total - discount<br>
DISPLAY name, category, total, discount, final_bill<br>
STOP<br>
##5. Sample Input:

Enter patient name: Ravi<br>
Enter patient age: 65<br>
Valid insurance? (yes/no): no<br>
##7. Sample Output:


Hospital Bill<br>
Patient: Ravi<br>
Category: Senior Citizen<br>
Total: 4500<br>
Discount: 450.0<br>
Final Bill: 4050.0<br>
##8. Conclusion
The program calculates hospital charges, applies the correct concession based on insurance or age, and displays the
patient's final payable amount.
