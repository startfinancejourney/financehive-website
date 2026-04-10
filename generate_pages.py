import os
import re

template = """<!DOCTYPE html>

<html class="light" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Learn Finance - FinanceHive</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Epilogue:wght@800;900&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "secondary-dim": "#b10e1e",
                        "on-tertiary-container": "#3f008e",
                        "tertiary-fixed-dim": "#b48fff",
                        "primary-fixed": "#fdd400",
                        "outline": "#81817a",
                        "on-tertiary": "#ffffff",
                        "secondary": "#c31f29",
                        "on-surface-variant": "#65655f",
                        "secondary-container": "#ffc3be",
                        "on-primary-fixed-variant": "#645300",
                        "on-primary-fixed": "#433700",
                        "inverse-surface": "#0e0f0a",
                        "error": "#be2d06",
                        "on-error": "#ffffff",
                        "on-tertiary-fixed-variant": "#4a00a4",
                        "inverse-primary": "#fdd400",
                        "error-container": "#f95630",
                        "surface-container-highest": "#e9e9de",
                        "tertiary-fixed": "#c0a0ff",
                        "on-secondary": "#ffffff",
                        "surface-variant": "#e9e9de",
                        "on-secondary-fixed": "#70000d",
                        "surface": "#fefcf4",
                        "on-secondary-fixed-variant": "#a60018",
                        "primary-fixed-dim": "#edc600",
                        "on-tertiary-fixed": "#200051",
                        "background": "#fefcf4",
                        "surface-container-low": "#fbf9f1",
                        "surface-container": "#f5f4eb",
                        "on-background": "#383833",
                        "surface-container-high": "#efeee5",
                        "tertiary": "#7a37eb",
                        "on-error-container": "#520c00",
                        "surface-bright": "#fefcf4",
                        "primary-container": "#fdd400",
                        "surface-dim": "#e4e3d8",
                        "on-surface": "#383833",
                        "error-dim": "#b92902",
                        "tertiary-container": "#c0a0ff",
                        "outline-variant": "#bab9b2",
                        "on-secondary-container": "#940014",
                        "secondary-fixed": "#ffc3be",
                        "on-primary": "#ffffff",
                        "secondary-fixed-dim": "#ffafaa",
                        "on-primary-container": "#594a00"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "fontFamily": {
                        "headline": ["Epilogue"],
                        "body": ["Plus Jakarta Sans"],
                        "label": ["Plus Jakarta Sans"]
                    }
                },
            },
        }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        .sketch-border {
            border: 2px solid #383833;
            box-shadow: 4px 4px 0px 0px #383833;
        }
        .scribble-underline {
            background-image: url("data:image/svg+xml,%3Csvg width='200' height='20' viewBox='0 0 200 20' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M2 15C20 12 180 12 198 15' stroke='%23FFD600' stroke-width='4' stroke-linecap='round'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: bottom;
            padding-bottom: 8px;
        }
        .doodle-bg {
            background-image: url("data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M10 10L20 20M20 10L10 20' stroke='%23383833' stroke-opacity='0.02'/%3E%3C/svg%3E");
        }
        .footer-doodle-line {
            height: 4px;
            background-image: url("data:image/svg+xml,%3Csvg width='400' height='10' viewBox='0 0 400 10' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 5C50 2 100 8 150 5C200 2 250 8 300 5C350 2 400 8 450 5' stroke='%23383833' stroke-width='2' stroke-linecap='round' opacity='0.2'/%3E%3C/svg%3E");
            background-repeat: repeat-x;
        }
        .doodle-icon {
            filter: drop-shadow(1px 1px 0px rgba(0,0,0,0.1));
        }
        .sketch-texture {
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.05'/%3E%3C/svg%3E");
        }
    
        .tilt-1 { transform: rotate(1.2deg); }
        .tilt-2 { transform: rotate(-1.5deg); }
        .tilt-3 { transform: rotate(0.8deg); }
        .tilt-4 { transform: rotate(-1.1deg); }
        .card-fuchsia { background-color: rgba(255, 214, 0, 0.12); } /* Electric Yellow */
        .card-purple { background-color: rgba(255, 77, 77, 0.12); } /* Coral Red */
        .card-lime { background-color: rgba(124, 58, 237, 0.12); } /* Violet */
        .card-orange { background-color: rgba(34, 197, 94, 0.12); } /* Lime Green */
    </style>
</head>
<body class="bg-surface font-body text-on-surface doodle-bg min-h-screen flex flex-col">
<!-- TopNavBar -->
<nav class="bg-surface border-b-4 border-stone-800 flex justify-between items-center w-full px-6 py-4 max-w-7xl mx-auto sticky top-0 z-50 gap-8">
<a href="index.html" class="text-3xl font-black text-[#383833] tracking-tighter font-marker">FinanceHive</a>
<div class="hidden md:flex gap-6 items-center">
<a class="text-on-surface hover:text-secondary font-marker font-black text-base transition-all duration-200" href="learn-finance.html">Learn Finance</a>
<a class="text-on-surface hover:text-secondary font-marker font-black text-base transition-all duration-200" href="sectors.html">Sectors</a>
<a class="text-on-surface hover:text-secondary font-marker font-black text-base transition-all duration-200" href="request-topic.html">Request a Topic</a>
<a class="text-on-surface hover:text-secondary font-marker font-black text-base transition-all duration-200" href="about.html">About</a>
</div>
<div class="flex items-center gap-4 lg:gap-6">
<div class="relative group flex items-center">
<input class="bg-white sketch-border px-4 py-2 pr-10 font-marker font-bold focus:outline-none focus:ring-2 focus:ring-primary w-48 md:w-64 transition-all" placeholder="Search concepts..." type="text"/>
<span class="material-symbols-outlined absolute right-3 text-on-surface font-black">search</span>
</div>
<button class="p-2 hover:bg-primary-container rounded-full transition-colors flex items-center justify-center">
<span class="material-symbols-outlined text-2xl font-black">notifications</span>
</button>
<button class="p-2 hover:bg-primary-container rounded-full transition-colors flex items-center justify-center">
<span class="material-symbols-outlined text-2xl font-black">account_circle</span>
</button>
<a href="learn-finance.html" class="bg-primary-container text-on-primary-container px-6 py-2 sketch-border font-black hover:translate-x-1 hover:translate-y-1 transition-all">
    Start Learning
  </a>
</div>
</nav>
<main class="flex-grow max-w-screen-md mx-auto px-6 py-12 w-full">
    <div class="mb-12">
        <a href="learn-finance.html" class="inline-block text-[#383833] font-bold font-marker hover:text-secondary transition-colors text-lg">
            &larr; Back to All Concepts
        </a>
    </div>
    
    <header class="mb-12 text-center">
        <h1 class="text-5xl md:text-7xl font-black font-headline text-on-surface mb-6 tracking-tighter capitalize"><span class="scribble-underline">{HEADING}</span></h1>
        <p class="text-xl font-medium text-on-surface/60 max-w-2xl mx-auto">{ONE_LINE}</p>
    </header>

    <section class="bg-white p-8 sketch-border sketch-texture mb-16 rounded-xl">
        <div class="flex flex-wrap gap-4 mb-8 justify-center border-b-2 border-stone-800/10 pb-8">
            <button onclick="switchTab('beg')" id="tab-beg" class="px-8 py-3 bg-primary-container sketch-border font-headline font-black uppercase tracking-widest transition-all hover:translate-y-[-2px] hover:translate-x-[-2px]">Beginner</button>
            <button onclick="switchTab('int')" id="tab-int" class="px-8 py-3 bg-surface-container-high border-2 border-on-surface/20 font-headline font-black uppercase tracking-widest transition-all hover:bg-secondary-container">Intermediate</button>
            <button onclick="switchTab('adv')" id="tab-adv" class="px-8 py-3 bg-surface-container-high border-2 border-on-surface/20 font-headline font-black uppercase tracking-widest transition-all hover:bg-tertiary-container">Advanced</button>
        </div>

        <div id="content-beg" class="concept-content text-lg text-on-surface/90 leading-relaxed font-body">
            <h3 class='font-black text-xl mb-2'>{BEG_TITLE}</h3><p>{BEG_CONTENT}</p>
        </div>
        <div id="content-int" class="concept-content hidden text-lg text-on-surface/90 leading-relaxed font-body">
            <h3 class='font-black text-xl mb-4'>A little deeper</h3>{INT_CONTENT}
        </div>
        <div id="content-adv" class="concept-content hidden text-lg text-on-surface/90 leading-relaxed font-body">
            <h3 class='font-black text-xl mb-4'>How people making money from this</h3>{ADV_CONTENT}
        </div>
    </section>
</main>
<!-- Footer -->
<footer class="bg-stone-900 text-white border-t-8 border-stone-800 flex flex-col md:flex-row justify-between items-center w-full px-8 py-16 gap-8">
<div class="max-w-7xl mx-auto w-full flex flex-col md:flex-row justify-between items-baseline gap-8">
<div class="flex flex-col items-start">
<a href="index.html" class="text-3xl font-black text-white font-marker tracking-tighter">FinanceHive</a>
<p class="text-stone-400 font-medium text-xs">Hand-drawn for Indian minds. ✏️</p>
</div>
<div class="flex flex-wrap justify-center gap-6 md:gap-8 font-marker font-black text-base">
<a class="hover:text-primary transition-colors" href="#">Privacy</a>
<span class="text-stone-700 hidden md:inline">|</span>
<a class="hover:text-primary transition-colors" href="#">Terms</a>
<span class="text-stone-700 hidden md:inline">|</span>
<a class="hover:text-primary transition-colors" href="disclaimer.html">Disclaimer</a>
<span class="text-stone-700 hidden md:inline">|</span>
<a class="hover:text-primary transition-colors" href="about.html">Contact</a>
</div>
<div class="text-stone-500 font-bold text-sm whitespace-nowrap">© 2026 FinanceHive. All rights reserved.</div>
</div>
</footer>
<!-- Decorative Doodles Background Overlay (Reduced noise) -->
<div class="fixed inset-0 pointer-events-none opacity-[0.015] z-[-1] overflow-hidden">
<span class="material-symbols-outlined absolute top-20 left-10 text-[120px]">currency_rupee</span>
<span class="material-symbols-outlined absolute bottom-40 right-10 text-[150px]">lightbulb</span>
</div>



</body>

<script>
function switchTab(level) {
    document.querySelectorAll('.concept-content').forEach(el => el.classList.add('hidden'));
    
    const inactiveClass = 'px-8 py-3 bg-surface-container-high border-2 border-on-surface/20 font-headline font-black uppercase tracking-widest transition-all';
    
    document.getElementById('tab-beg').className = inactiveClass + ' hover:bg-primary-container hover:translate-y-[-2px] hover:translate-x-[-2px]';
    document.getElementById('tab-int').className = inactiveClass + ' hover:bg-secondary-container';
    document.getElementById('tab-adv').className = inactiveClass + ' hover:bg-tertiary-container';
    
    document.getElementById('content-' + level).classList.remove('hidden');
    
    const activeClass = 'px-8 py-3 bg-primary-container sketch-border font-headline font-black uppercase tracking-widest transition-all hover:translate-y-[-2px] hover:translate-x-[-2px]';
    document.getElementById('tab-' + level).className = activeClass;
}
</script>
</body>
</html>"""

def get_html_sub(text):
    # Parse lines to bold topics followed by paragraphs
    lines = [x.strip() for x in text.strip().split('\\n') if x.strip()]
    if len(lines) == 1:
        return f"<p>{lines[0]}</p>"
    
    # We expect format like:
    # Topic Name
    # Content
    # Topic Name
    # Content
    out = ""
    for i in range(0, len(lines), 2):
        if i+1 < len(lines):
            out += f"<strong class='block mt-4 mb-1 text-secondary'>{lines[i]}</strong><p>{lines[i+1]}</p>"
        else:
            out += f"<p>{lines[i]}</p>"
    return out

pages = [
    {
        "file": "concept-networth.html",
        "Heading": "Net worth",
        "One-line": "The true measure of your wealth — what you truly own after subtracting what you owe",
        "BegTitle": "Net Worth in one minute",
        "BegContent": "Imagine you own a house worth ₹50 lakh but have a ₹30 lakh loan on it. Your net worth from the house is ₹20 lakh. Add your savings, investments, and other assets. Subtract all loans and debts. What remains is your NET WORTH.",
        "IntContent": "Simple formula\\nNet Worth = All Assets − All Liabilities. If positive, you have more than you owe. If negative, you owe more than you own.\\nWhy it matters\\nNet worth is the real scorecard of financial health. Income alone does not tell the full picture.\\nGrowing net worth\\nEarn more. Save more. Invest in appreciating assets. Reduce debts. This is the path to higher net worth.\\nTrack it yearly\\nCalculate your net worth every year. Watching it grow is very motivating.",
        "AdvContent": "High income ≠ high net worth\\nDoctors earning ₹30 lakh/year but spending all of it have zero net worth. A teacher investing ₹10,000/month for 20 years can build massive net worth.\\nInvestment return\\nEvery rupee invested in equity or real estate can multiply over time — fast-tracking net worth growth.\\nRisk\\nMarket crashes can temporarily reduce net worth. Do not panic. Long-term it recovers."
    },
    {
        "file": "concept-interestrate.html",
        "Heading": "Interest Rate",
        "One-line": "The price you pay to borrow money — or the reward you earn for lending it",
        "BegTitle": "Interest Rate in one minute",
        "BegContent": "When a bank gives you a loan, it charges extra. That extra charge is interest. If you borrow ₹1 lakh at 10% per year, you pay ₹10,000 extra as interest. On the flip side, if you deposit money in a bank, the bank pays YOU interest.",
        "IntContent": "Borrower\\'s view\\nHigher interest = more expensive loan. Lower interest = cheaper to borrow.\\nSaver\\'s view\\nHigher interest rate on FD = more returns. Lower rate = less earning on savings.\\nRBI controls rates\\nReserve Bank of India sets the repo rate. Banks use this as a base to set their own loan and deposit rates.\\nImpact on markets\\nWhen interest rates rise, stocks often fall. Why? Loans get costly, companies earn less, investors prefer safe bonds.",
        "AdvContent": "Compare before borrowing\\nAlways compare interest rates across banks. Even 1% difference on ₹30 lakh home loan = savings of lakhs.\\nEffect on investment\\nRising rates = bond prices fall. Falling rates = bond prices rise. Important for debt mutual fund investors.\\nRisk\\nVariable interest rate loans can jump in cost if RBI hikes rates. Fixed rate = predictable. Variable = risky."
    },
    {
        "file": "concept-sip.html",
        "Heading": "SIP",
        "One-line": "Invest a fixed small amount every month — the most beginner-friendly way to build wealth.",
        "BegTitle": "SIP in one minute",
        "BegContent": "Imagine you save ₹1,000 every month from your pocket money. Instead of keeping it idle, you invest it in a mutual fund every month. Some months you buy units cheap. Some months expensive. Over time it averages out. That automatic monthly investment is called a SIP (Systematic Investment Plan).",
        "IntContent": "How SIP works\\nYou authorise your bank to send a fixed amount to a mutual fund on a chosen date every month. It is fully automatic.\\nRupee Cost Averaging\\nWhen markets fall, your ₹1,000 buys MORE units. When markets rise, it buys fewer. Over time, your average cost stays low.\\nNo timing needed\\nYou do not need to predict market highs and lows. You invest every month no matter what.\\nStart small\\nSIPs start from as low as ₹100 per month on many platforms. There is no excuse to not start.",
        "AdvContent": "Power of habit\\n₹5,000/month for 20 years at 12% return = over ₹50 lakh. You invested ₹12 lakh. The rest is the magic of compounding.\\nEasy to change\\nYou can pause, increase, or stop your SIP anytime. Full flexibility.\\nRisks\\nSIP does not eliminate risk — markets can still fall. But regular investing over long term greatly reduces the chance of losing."
    },
    {
        "file": "concept-fixeddeposit.html",
        "Heading": "Fixed Deposit",
        "One-line": "Lock your money in the bank for a fixed time and earn a guaranteed interest",
        "BegTitle": "Fixed Deposit in one minute",
        "BegContent": "You keep ₹1 lakh in the bank for 1 year at 7%. After 1 year the bank gives you back ₹1,07,000. You did nothing. The bank used your money, paid you interest, everyone is happy. That is an FD.",
        "IntContent": "Tenure options\\n7 days to 10 years. The longer the tenure, generally higher the rate.\\nSafety\\nDeposits up to ₹5 lakh per bank are insured by DICGC. Among the safest investments.\\nSenior citizen benefit\\nBanks offer 0.25-0.50% extra interest rate for senior citizens on FDs.\\nPremature withdrawal\\nBreaking FD early = penalty (usually 0.5-1% reduction in interest rate).",
        "AdvContent": "Tax on FD\\nInterest earned is added to income and taxed as per your slab. Not tax-efficient for high earners.\\nTax-saving FD\\n5-year FD under Section 80C gives tax deduction on ₹1.5 lakh. But lock-in for 5 years, no premature withdrawal.\\nRisk\\nMain risk is inflation. If FD gives 7% but inflation is 6%, real return is just 1%. Not ideal for long-term wealth building."
    },
    {
        "file": "concept-savingsaccount.html",
        "Heading": "Savings Account",
        "One-line": "Your basic bank account that keeps money safe and gives small interest daily",
        "BegTitle": "Savings Account in one minute",
        "BegContent": "A savings account is like a safe. You put money in, take it out anytime. The bank gives you 2.5-4% interest per year just for keeping money there. It is not to build wealth — it is to keep your spending money safe and accessible.",
        "IntContent": "Interest rates\\nMost banks give 2.5-4%. Small finance banks give 5-7%. Still barely keeps up with inflation.\\nInstant access\\nATM, UPI, NEFT, IMPS — your money is accessible 24/7. Maximum liquidity.\\nMinimum balance\\nMost banks require ₹1,000-₹10,000 minimum balance. Penalty for going below.\\nDICGC insurance\\nUp to ₹5 lakh insured. Even if bank fails, you get ₹5 lakh back.",
        "AdvContent": "Emergency fund home\\nKeep 1-3 months expenses in savings account. Rest should be in better-yielding investments.\\nSweep-in FD\\nMany banks offer sweep-in facility — excess savings auto-converted to FD for higher interest.\\nRisk\\nKeeping large amounts in savings account means losing to inflation. Only keep what you need for immediate use."
    },
    {
        "file": "concept-creditscore.html",
        "Heading": "Credit Score",
        "One-line": "Your financial report card — a number that shows how trustworthy you are as a borrower.",
        "BegTitle": "Credit Score in one minute",
        "BegContent": "You always repay your loans on time. The bank notices. Your credit score goes up (closer to 900). Next time you want a loan, banks fight to give it to you at the best rates. Miss payments? Score drops. Banks get cautious. You pay higher interest or get rejected.",
        "IntContent": "Range\\nIn India (CIBIL): 300 to 900. Above 750 = excellent. 650-749 = fair. Below 650 = poor.\\nWhat affects score\\nPayment history (35%), credit utilisation (30%), credit age, types of credit, new applications.\\nWho checks it\\nBanks, NBFCs, credit card companies, sometimes even employers check credit score.\\nFree check\\nCheck your CIBIL score free once a year on CIBIL website or anytime on apps like Paisabazaar.",
        "AdvContent": "Better score = better deals\\n750+ score can get home loan at 8.5% while a 650 scorer pays 10.5%. On ₹50L, that difference is massive.\\nBuild score early\\nGet a credit card. Use less than 30% of limit. Pay full bill on due date. Score rises steadily.\\nRisk\\nDefaulting on even small EMI hits your score badly. Recover can take 2-3 years. Protect your score carefully."
    },
    {
        "file": "concept-loan.html",
        "Heading": "Loan",
        "One-line": "Borrowed money that you promise to repay with interest over time.",
        "BegTitle": "Loan in one minute",
        "BegContent": "You need ₹5 lakh for a car but only have ₹1 lakh. The bank lends ₹4 lakh. You repay in monthly instalments (EMI) over 5 years with interest. You got the car now. The bank gets interest income. Both sides get what they need. That is a loan.",
        "IntContent": "Secured vs Unsecured\\nSecured loan backed by collateral (home, car). Bank can seize collateral if you default. Lower interest. Unsecured loan (personal loan) = higher interest = more risk for bank.\\nTenure\\nHome loan: up to 30 years. Car loan: 3-7 years. Personal loan: 1-5 years. Longer tenure = lower EMI but more total interest.\\nInterest rate types\\nFixed rate stays same throughout. Floating rate changes with market conditions (RBI rate changes).\\nPrepayment\\nPaying loan early saves interest. Most banks allow it after some lock-in period, sometimes with penalty.",
        "AdvContent": "Good debt\\nHome loan for appreciating property = good debt. It builds an asset. Personal loan for vacation = bad debt.\\nTotal cost of loan\\nCalculate total repayment = EMI × months. Compare to original loan. You will be surprised how much interest you pay.\\nRisk\\nOver-leverage (too many loans) = financial trap. EMIs consuming more than 40% of income = danger zone."
    },
    {
        "file": "concept-emi.html",
        "Heading": "EMI",
        "One-line": "Your fixed monthly payment to repay a loan — part goes to principal, part to interest.",
        "BegTitle": "EMI in one minute",
        "BegContent": "You borrow ₹6 lakh for a car. Bank says: pay ₹12,000 every month for 5 years. That ₹12,000 is your EMI. Every month part of it repays the loan amount. Part is the bank's interest. Every month the loan balance reduces.",
        "IntContent": "EMI formula\\nEMI = P × r × (1+r)^n / ((1+r)^n - 1). Where P = principal, r = monthly rate, n = months. Use an online EMI calculator — much easier.\\nAmortization\\nIn early months, most of EMI = interest. As loan reduces, more goes to principal. By last EMI, almost all is principal.\\nPrepay early\\nPaying extra early reduces outstanding principal — interest in future months drops significantly.\\nNACH mandate\\nBanks auto-debit EMI from your account on due date. Ensure sufficient balance to avoid bounce charges.",
        "AdvContent": "EMI affordability\\nRule: Total EMIs should not exceed 40% of monthly take-home income.\\nLower interest saves big\\nEven 1% rate difference on ₹30 lakh home loan over 20 years = saving of ₹4-5 lakh in total payments.\\nRisk\\nMissed EMIs damage credit score, attract penalties, and can lead to loan default. Auto-debit helps avoid mistakes."
    },
    {
        "file": "concept-insurance.html",
        "Heading": "Insurance",
        "One-line": "Pay a small amount now to be protected against a huge financial loss later.",
        "BegTitle": "Insurance in one minute",
        "BegContent": "You and 1,000 people pay ₹5,000/year to an insurance company. Out of 1,000, only 2 people fall seriously ill and need ₹5 lakh each = ₹10 lakh total. Insurance company collected ₹50 lakh from everyone, pays ₹10 lakh in claims, keeps rest as profit. Everyone sleeps peacefully knowing they are covered.",
        "IntContent": "Types of insurance\\nLife insurance (income replacement), health insurance (medical bills), motor (vehicle damage), home insurance (property).\\nTerm insurance\\nCheapest, purest life insurance. Pay small premium. Family gets large sum if you die. No return if you survive. That is the point — protection, not investment.\\nHealth insurance\\nMedical emergencies can wipe out years of savings in days. Health insurance is non-negotiable for every family.\\nPremium\\nThe amount you pay to the insurance company regularly (monthly, quarterly, annually) to stay covered.",
        "AdvContent": "Priority order\\n1. Term life insurance. 2. Health insurance. 3. Then start investing. Never skip first two.\\nSum assured\\nMinimum term cover = 10-15× annual income. If you earn ₹8L/year, cover should be ₹80L-₹1.2 crore.\\nRisk of underinsurance\\nBeing under-insured is as dangerous as no insurance. A ₹5L health cover is insufficient for a family in a metro today."
    },
    {
        "file": "concept-diversification.html",
        "Heading": "Diversification",
        "One-line": "Do not put all eggs in one basket — spread your investments to reduce risk.",
        "BegTitle": "Diversification in one minute",
        "BegContent": "Imagine you have ₹1 lakh. If you put all of it in one company and it goes bankrupt, you lose everything. But if you spread it across 10 companies, even if 2 fail, the rest can still grow. That spreading is diversification",
        "IntContent": "Why it works\\nDifferent investments react differently to the same event. Gold rises when markets fall. Bonds steady when stocks are volatile.\\nAcross sectors\\nDo not invest only in tech or only in banking. Spread across healthcare, FMCG, auto, IT, etc.\\nAcross asset classes\\nSpread across equity, debt, gold, real estate. Each behaves differently.\\nOver-diversification\\nHolding 100 stocks is not useful. 15-25 carefully chosen stocks is enough for good diversification.",
        "AdvContent": "Mutual fund advantage\\nA single mutual fund unit gives you exposure to 50-100 companies instantly. Built-in diversification.\\nCorrelation\\nMix assets with low correlation. When equity falls, gold often rises — that is a good combination.\\nRisk\\nOver-diversification reduces potential returns. Diversify smartly, not randomly."
    },
    {
        "file": "concept-riskreturn.html",
        "Heading": "Risk & Return",
        "One-line": "Higher the risk, higher the potential reward — this is the core trade-off of all investing.",
        "BegTitle": "Risk & Return in one minute",
        "BegContent": "Would you lend ₹1,000 to your most reliable friend or to a stranger? You might lend to the stranger too — but you would want higher interest to compensate for the extra risk. Same logic applies everywhere in finance.",
        "IntContent": "Risk defined\\nRisk = chance that your actual return is different from expected return. Could be higher OR lower.\\nReturn defined\\nReturn = what you earn. Fixed deposit = 6-7%. Equity = historically 12-15% long term. Higher return = accepted more risk.\\nTypes of risk\\nMarket risk, inflation risk, liquidity risk, credit risk (borrower default), currency risk for foreign investments.\\nRisk tolerance\\nYoung person with stable income = can take more risk. Retired person = should take less risk.",
        "AdvContent": "Risk-reward matrix\\nSavings: low risk, low return. FD: slightly more. Mutual funds: medium. Stocks: higher. Crypto: very high risk, very high potential.\\nManage risk\\nDiversify. Invest long term. Do not invest borrowed money in risky assets.\\nKey insight\\nRisk is not the enemy. Unmanaged risk is. Understand your risk, plan around it."
    },
    {
        "file": "concept-liquidity.html",
        "Heading": "Liquidity",
        "One-line": "How quickly and easily you can convert an investment into cash without losing value.",
        "BegTitle": "Liquidity in one minute",
        "BegContent": "Water flows easily. That is liquid. A rock does not flow. Savings account = water (can withdraw instantly). Your house = rock (takes months to sell). In finance, liquidity = how fast you can turn something into cash.",
        "IntContent": "High liquidity\\nSavings accounts, liquid mutual funds — access money in seconds to 24 hours.\\nLow liquidity\\nReal estate, fixed deposits with lock-in, private equity — selling takes time.\\nMarket liquidity\\nA stock with millions of daily trades = highly liquid. A small company with few buyers = illiquid.\\nWhy it matters\\nEmergency expenses need liquid assets. Do not tie all your money in illiquid investments",
        "AdvContent": "Emergency fund\\nKeep 6 months of expenses in liquid assets (savings account or liquid fund). Non-negotiable.\\nLiquidity premium\\nIlliquid investments often give higher returns — like Fixed Deposits vs Savings Account — to compensate for low liquidity.\\nRisk\\nLiquidity crises happen. Banks can freeze withdrawals. Always diversify across liquid and illiquid assets."
    },
    {
        "file": "concept-indexfund.html",
        "Heading": "Index Fund",
        "One-line": "Automatically invest in the top companies of a market index without any fund manager deciding",
        "BegTitle": "Index Fund in one minute",
        "BegContent": "Nifty 50 = India's top 50 companies. An index fund copies this list exactly. If Reliance is 10% of Nifty, the fund puts 10% in Reliance. No manager decisions needed. It follows the index like a shadow",
        "IntContent": "Passive investing\\nIndex funds do not try to beat the market — they match it. Studies show most active managers fail to beat the index consistently.\\nVery low cost\\nNo stock picking = low management cost. Expense ratio as low as 0.10%.\\nConsistent performance\\nOver 15-20 years, Nifty 50 index funds have delivered 12-14% CAGR historically.\\nTransparency\\nYou know exactly what you own — the same stocks as the index. No surprises.",
        "AdvContent": "Warren Buffett's advice\\nEven the world's greatest investor recommends index funds for most regular investors.\\nSIP + Index Fund\\nOne of the most powerful beginner strategies: start a monthly SIP in a Nifty 50 index fund.\\nRisk\\nIf the entire market falls, so does your index fund. But over long term, markets have always recovered."
    },
    {
        "file": "concept-etf.html",
        "Heading": "ETF (Exchange Traded Fund)",
        "One-line": "A basket of stocks you can buy in one click — trades like a share on the stock exchange",
        "BegTitle": "ETF in one minute",
        "BegContent": "An ETF is like a pre-made lunch box. Instead of buying rice, dal, sabzi, roti separately, someone packages them together. You buy the box. Similarly, a Nifty 50 ETF gives you a tiny piece of all 50 Nifty companies in one purchase",
        "IntContent": "How ETF works\\nETFs track an index like Nifty 50 or Sensex. When index goes up, ETF goes up. Simple and transparent.\\nETF vs Mutual Fund\\nETFs trade on stock exchange in real time like shares. Mutual funds are priced once a day at NAV.\\nLow cost\\nETFs have very low expense ratios (0.05% to 0.20%). Actively managed mutual funds charge 0.5% to 2%.\\nTypes of ETFs\\nEquity ETF, Gold ETF, Debt ETF, International ETF — track different asset classes",
        "AdvContent": "Nifty BeES\\nIndia's most popular ETF tracks Nifty 50. One of the simplest, lowest-cost ways to invest in Indian stock market.\\nGold ETF\\nBuy gold without physical storage risk. Price tracks real gold.\\nRisk\\nETFs also fall when markets fall. But they will never go to zero unless all 50 companies collapse."
    },
    {
        "file": "concept-marketcapitalization.html",
        "Heading": "Market Capitalization",
        "One-line": "The total market value of a company — size measured in money.",
        "BegTitle": "Market Capitalization in one minute",
        "BegContent": "A company has 1 crore shares. Each share is priced at ₹500. Market cap = 1 crore × 500 = ₹500 crore. That is how the market values the entire company at any given moment.",
        "IntContent": "Categories in India\\nLarge cap: top 100 companies by market cap. Mid cap: 101-250. Small cap: beyond 250. Each has different risk profiles.\\nLarge cap = stable\\nReliance, TCS, HDFC Bank. These are massive, stable, less volatile.\\nMid cap = growth\\nGrowing companies with higher return potential. More volatile than large cap.\\nSmall cap = high risk\\nSmall companies. Huge upside potential. But can fall 50-70% easily in bad markets.",
        "AdvContent": "Investment strategy\\nYoung investors with long horizon can invest more in small-mid cap. Older investors prefer large cap stability.\\nMarket cap vs revenue\\nA company can have high market cap but low revenue. Investors are paying for future potential.\\nRisk\\nSmall cap stocks are thinly traded. Prices can move sharply up or down on low volume."
    },
    {
        "file": "concept-roi.html",
        "Heading": "ROI (Return On Investment)",
        "One-line": "How much money did you earn back for every rupee you put in?",
        "BegTitle": "ROI in one minute",
        "BegContent": "You invested ₹10,000 in a mutual fund. After one year you have ₹12,000. You made ₹2,000 profit. ROI = ₹2,000 ÷ ₹10,000 × 100 = 20%. For every ₹100 invested, you got ₹20 back. Simple.",
        "IntContent": "Formula\\nROI = (Final Value − Initial Investment) ÷ Initial Investment × 100\\nCompare investments\\nFD gave 6% ROI. Mutual fund gave 14% ROI. Clearly mutual fund won — for the same risk level.\\nTime matters\\n20% ROI over 1 year is great. 20% ROI over 10 years is poor. Always compare time period.\\nRisk-adjusted ROI\\nHigher ROI with lower risk = better investment. Do not chase ROI without considering risk.",
        "AdvContent": "Use for all decisions\\nHouse renovation ROI. Business investment ROI. Education ROI. ROI thinking helps everywhere.\\nCAGR is better\\nFor multi-year investments, use CAGR (compound annual growth rate) instead of simple ROI.\\nRisk\\nPast ROI does not guarantee future returns. Always factor in risk before comparing."
    }
]

import os
target_dir = r"c:\Users\user\OneDrive\Desktop\FinanceHive-Website"
for p in pages:
    html = template.replace("{HEADING}", p['Heading']).replace("{ONE_LINE}", p['One-line']).replace("{BEG_TITLE}", p['BegTitle']).replace("{BEG_CONTENT}", p['BegContent'])
    html = html.replace("{INT_CONTENT}", get_html_sub(p['IntContent']))
    html = html.replace("{ADV_CONTENT}", get_html_sub(p['AdvContent']))
    with open(os.path.join(target_dir, p['file']), 'w', encoding='utf-8') as f:
        f.write(html)
    print("Created", p['file'])
