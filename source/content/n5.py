import random
UNITS = []

UNITS.append(dict(id="N10", part="National", title="Real Estate Math (Formula Sheet & Drills)",
 objectives=["Memorize the core formulas","Solve percentage, commission, loan, proration, area and appraisal problems","Use the built-in drills until you can solve each type in under 90 seconds"],
 drill=True,
 lessons=[
 dict(title="The percent triangle and commission math",
  body=["Almost every real estate math problem reduces to **Part = Whole × Rate**. Draw the triangle: **Part** on top, **Whole** and **Rate** on the bottom. Cover what you want: Part = Whole × Rate; Whole = Part ÷ Rate; Rate = Part ÷ Whole. Convert percents to decimals (6% = 0.06; 2.5% = 0.025).",
  "**Commission** = sale price × commission rate. **Split**: broker's share and salesperson's share (e.g., 60/40 split of the commission). **Net to seller** = sale price − commission − payoff − closing costs. To find the **price needed to net a target**: Price = (target net + costs and payoff) ÷ (1 − commission rate).",
  "**Profit/loss and appreciation**: Percent change = (new − old) ÷ old.",
  "**Worked**: House sells for $240,000; commission 6%; listing side gets 50%; salesperson gets 60% of the listing side. Commission = 14,400; listing side = 7,200; salesperson = 4,320."],
  key=["Part = Whole × Rate","Price to net a target = (net + costs) ÷ (1 − commission rate)","Percent change = (new − old) ÷ old"],
  example="Seller wants to net $190,000 after a 6% commission and $5,000 of costs/payoff beyond that: price = (190,000 + 5,000) ÷ 0.94 = $207,446.81 (rounded)."),
 dict(title="Loans, interest, points, LTV and ratios",
  body=["**Simple interest** = principal × rate × time (years). Monthly interest on a balance = balance × annual rate ÷ 12. **First-month payment split**: interest = balance × rate ÷ 12; principal = payment − interest; new balance = balance − principal.",
  "**LTV** = loan ÷ lesser of price or appraised value. **Down payment** = price − loan. **Points** = loan × (points ÷ 100). **PITI** = principal + interest + taxes + insurance; monthly taxes = annual ÷ 12.",
  "**Front-end ratio** = PITI ÷ gross monthly income; **back-end ratio** = (PITI + other monthly debts) ÷ gross monthly income. **Maximum payment** = income × ratio.",
  "**Amortization factors**: exams often give a payment factor per $1,000 (e.g., $6.00 per $1,000 at a given rate and term). Monthly P&I = (loan ÷ 1,000) × factor. The factor depends on rate and term; use the one given.",
  "**Debt service coverage** = NOI ÷ annual debt service. **Cash-on-cash** = annual pre-tax cash flow ÷ cash invested."],
  key=["Monthly interest = balance × annual rate ÷ 12","LTV uses the lesser of price or appraisal","Monthly P&I = (loan ÷ 1,000) × factor"],
  example="$180,000 loan at 5%: first-month interest = 180,000 × 0.05 ÷ 12 = $750. If the payment is $966.28, principal = $216.28 and the new balance is $179,783.72."),
 dict(title="Prorations, area, appraisal and tax math",
  body=["**Prorations**: daily rate = annual amount ÷ 360 (statutory year, 30-day months) or ÷ 365 (calendar year) — use the one the problem states. Multiply by the number of days owed. Taxes in arrears → seller owes; prepaid items (insurance, HOA dues paid ahead) → buyer reimburses the seller. If the buyer owns the closing day, count seller days through the day before.",
  "**Area**: rectangle = length × width; triangle = ½ × base × height; circle = π r². **Acres**: 1 acre = **43,560 sq ft**; section = 640 acres; 1 mile = 5,280 ft; volume = L × W × H (cubic feet ÷ 27 = cubic yards). Break irregular shapes into rectangles and triangles.",
  "**Appraisal**: Value = NOI ÷ cap rate; Cap rate = NOI ÷ value; **GRM** = price ÷ monthly rent; **Depreciated cost** = replacement cost − depreciation + land; **annual straight-line depreciation** = cost ÷ useful life. **Comparable adjustments**: add to the comp if the comp is inferior; subtract if superior.",
  "**Property tax**: assessed value = market value × ratio; tax = assessed value × millage ÷ 1,000. Mississippi Class I = 10%, Class II = 15%.",
  "**Documentary/transfer tax and survey problems** appear on some exams; read units carefully."],
  key=["43,560 sq ft per acre","Statutory year = 360 days; calendar year = 365","Comp inferior → add; comp superior → subtract"],
  example="Tax bill $3,600 for the calendar year; closing is March 31 and the buyer owns the closing day; taxes unpaid. Seller days = Jan 1–Mar 30 = 89 days (365-day year): 3,600 ÷ 365 × 89 = $877.81 credit to the buyer."),
 ],
 quiz=[]))

# ---------- Python-verified math quiz ----------
def _mk():
    q=[]
    def add(text,correct,wrongs,why): q.append((text,correct,wrongs,why))
    # 1 commission
    price=240000; add("A home sells for $240,000 at a 6% commission. The commission is:", f"${price*0.06:,.0f}", [f"${price*0.06/2:,.0f}", f"${price*0.006:,.0f}", f"${price*0.16:,.0f}"], "240,000 × 0.06 = 14,400.")
    # 2 split
    add("A $14,400 commission is split 50/50 between listing and selling brokers; the listing salesperson gets 60% of the listing side. The salesperson earns:", f"${14400*0.5*0.6:,.0f}", [f"${14400*0.6:,.0f}", f"${14400*0.5*0.4:,.0f}", f"${14400*0.5:,.0f}"], "14,400 × .5 × .6 = 4,320.")
    # 3 net price
    p=(190000+5000)/0.94; add("A seller wants to net $190,000 after a 6% commission and $5,000 in other costs. The sale price must be about:", f"${p:,.0f}", [f"${190000*1.06+5000:,.0f}", f"${190000*1.11:,.0f}", f"${(190000+5000)*0.94:,.0f}"], "(190,000 + 5,000) ÷ 0.94.")
    # 4 LTV
    add("A buyer buys at $250,000, appraisal $240,000, and borrows $216,000. The LTV is:", f"{216000/240000:.0%}", [f"{216000/250000:.1%}", "80%", "95%"], "Use the lesser of price or value: 216/240 = 90%.")
    # 5 interest
    add("Monthly interest on a $180,000 balance at 5.25% is:", f"${180000*0.0525/12:,.2f}", [f"${180000*0.0525:,.2f}", f"${180000*0.0525/52:,.2f}", f"${180000*0.0525/360:,.2f}"], "Balance × rate ÷ 12.")
    # 6 points
    add("Three discount points on a $275,000 loan cost:", f"${275000*0.03:,.0f}", [f"${275000*0.003:,.0f}", f"${275000*0.3:,.0f}", f"${275000*0.03/12:,.0f}"], "1 point = 1% of the loan.")
    # 7 front end
    pi=1850; inc=6500; add("PITI of $1,850 on gross monthly income of $6,500 gives a front-end ratio of about:", f"{pi/inc:.1%}", [f"{(pi+400)/inc:.1%}", f"{pi/(inc*12):.1%}", "40.0%"], "1,850 ÷ 6,500.")
    # 8 back end
    add("PITI $1,850 plus $450 of other debts on $6,500 income gives a back-end ratio of about:", f"{(1850+450)/6500:.1%}", [f"{1850/6500:.1%}", f"{450/6500:.1%}", f"{(1850+450)/(6500*12):.1%}"], "(1,850 + 450) ÷ 6,500.")
    # 9 acres
    add("A lot measures 200 ft by 435.6 ft. Its area in acres is:", f"{200*435.6/43560:.0f}", ["1","0.5","5"], "87,120 sq ft ÷ 43,560 = 2 acres.")
    # 10 NE
    add("The S½ of the NW¼ of the SE¼ of a section contains how many acres?", "20", ["40","80","10"], "640 → 160 → 40 → 20.")
    # 11 cap value
    noi=84000; cap=0.08; add("An income property has NOI of $84,000 and a market cap rate of 8%. Its value is:", f"${noi/cap:,.0f}", [f"${noi*cap:,.0f}", f"${noi/0.09:,.0f}", f"${noi*12:,.0f}"], "84,000 ÷ 0.08.")
    # 12 cap rate
    add("A building sold for $1,200,000 and produces NOI of $102,000. The cap rate is:", f"{102000/1200000:.1%}", ["10.2%","12.0%","8.5%".replace("8.5","11.8")], "102,000 ÷ 1,200,000 = 8.5%.")
    # 13 GRM
    add("A rental sells for $135,000 and rents for $1,125 per month. The GRM is:", f"{135000/1125:.0f}", ["100","12","144"], "135,000 ÷ 1,125 = 120.")
    # 14 proration
    t=3600; d=89; add("Annual taxes of $3,600 are unpaid at closing; the seller owes 89 days using a 365-day year. The credit to the buyer is about:", f"${t/365*d:,.2f}", [f"${t/360*d:,.2f}", f"${t/12*3:,.2f}", f"${t/365*90:,.2f}"], "3,600 ÷ 365 × 89.")
    # 15 MS tax
    add("A Mississippi owner-occupied home (Class I) is worth $180,000 and the millage is 90. The tax is:", f"${180000*0.10*0.090:,.0f}", [f"${180000*0.15*0.090:,.0f}", f"${180000*0.090:,.0f}", f"${180000*0.010:,.0f}"], "180,000 × 10% = 18,000; × 0.090.")
    # 16 appreciation
    add("A home bought at $200,000 is now worth $230,000. The appreciation rate is:", f"{30000/200000:.0%}", ["13%","30%","23%"], "30,000 ÷ 200,000.")
    # 17 comp adjust
    add("A comparable with a $14,000 pool sold for $310,000. The subject has no pool. The adjusted comparable price is:", f"${310000-14000:,.0f}", [f"${310000+14000:,.0f}", "$310,000", f"${310000-28000:,.0f}"], "Comp is superior → subtract.")
    # 18 depreciation
    add("A building costs $450,000 to replace, has depreciated 30% and the land is worth $90,000. The cost-approach value is:", f"${450000*0.7+90000:,.0f}", [f"${450000*0.3+90000:,.0f}", f"${450000*0.7:,.0f}", f"${450000-90000:,.0f}"], "315,000 + 90,000.")
    # 19 DSCR
    add("NOI of $60,000 and annual debt service of $48,000 gives a DSCR of:", f"{60000/48000:.2f}", ["0.80","1.00","1.50"], "60,000 ÷ 48,000.")
    # 20 first-month principal
    interest=180000*0.05/12; add("A $180,000 loan at 5% has a $966.28 payment. The principal paid in the first month is:", f"${966.28-interest:,.2f}", [f"${interest:,.2f}", "$966.28", "$1,716.28"], "Payment minus interest 750.")
    return q
UNITS[0]['quiz']=_mk()

UNITS.append(dict(id="N11", part="National", title="Exam Strategy & Path to Licensure",
 objectives=["Plan your study and test-day approach","Follow the Mississippi licensure steps","Know where to verify rules that change"],
 lessons=[
 dict(title="How to prepare and what to do on exam day",
  body=["**Study cycle**: learn a unit → take its quiz → review every miss → re-take after 24 hours → use the drills for math → finish with timed full-length practice. Aim for **85%+ on practice** before the real exam, because the real wording is harder than most practice questions.",
  "**Test tactics**: read the *last sentence first* to know what is asked; underline key words (**NOT, EXCEPT, FIRST, MOST, ALWAYS**); eliminate two answers; for math, **estimate** the answer first and check units (monthly vs annual); mark and return to unsure items; **never leave blanks**.",
  "**Common traps**: confusing *agent vs. customer*, *voidable vs. void*, *debit vs. credit*, *assessed vs. market value*, *gross vs. net*, *monthly vs. annual*, *principal vs. interest*; confusing federal and state rules (when the question says 'in Mississippi' pick the state rule).",
  "**Calculator**: bring the permitted type; practice with it. Know the formulas by heart.",
  "**State-specific law**: Mississippi law changes (2023 agency/PCDS changes; July 2026 revisions). When two sources disagree, rely on the **current MREC license law** and PSI's current candidate bulletin."],
  key=["Practice until you reliably score 85%+","Watch NOT/EXCEPT/ALWAYS/NEVER","Rely on the current MREC law and PSI bulletin"],
  example="Question: 'Which is NOT a duty of a seller's agent?' The answer is the item that is not obedience, loyalty, confidentiality, disclosure, accounting or reasonable care."),
 dict(title="Steps to a Mississippi license",
  body=["1. **Confirm eligibility** (age 18 for salesperson, Mississippi residency, background clearance).",
  "2. **Complete the 60-hour pre-license course** from an MREC-approved provider.",
  "3. **Apply** to MREC and register for the **PSI** exam; pass the **national (80 questions, 70%)** and **state (40 questions, 75%)** portions.",
  "4. **Choose a principal broker** to sponsor you; your license designates that broker.",
  "5. **Receive the temporary license** and complete the **30-hour post-license** course to earn the permanent license.",
  "6. **Renew** on time, complete **16 hours of CE** per renewal cycle (2 license law, 2 contract law, 4 agency, plus electives).",
  "**Always verify with**: MREC (mrec.ms.gov), the current PSI candidate bulletin, and your pre-license school. This course is a study aid, not legal advice or an official source."],
  key=["60 hours → exam → principal broker → 30-hour post-license","Verify fees, forms and dates on MREC and PSI","This course is not legal advice"],
  example="You pass the national portion but fail the state portion. Because both parts must be passed within the testing window, check PSI's current retake rules immediately."),
 ],
 quiz=[
 ("When a question says 'EXCEPT', you should look for:", "the one choice that is false or does not apply", ["the first correct choice","the longest answer","the answer that repeats the question"], "Read for the odd one out."),
 ("A good target before booking the exam is to score about:", "85% or higher on practice exams", ["50%","60%","you cannot predict"], "Margin for harder wording."),
 ("After a new licensee's temporary license, the permanent license requires:", "the 30-hour post-license course", ["a second exam","a 2-year wait","nothing further"], "§73-35-14.5."),
 ("The best source to resolve conflicting rule summaries is:", "the current MREC law and PSI bulletin", ["a blog post","the oldest textbook","a forum"], "Primary sources."),
 ("When a stem says 'in Mississippi', choose the:", "state rule", ["federal rule always","national average","most common rule elsewhere"], "State-specific."),
 ]))
