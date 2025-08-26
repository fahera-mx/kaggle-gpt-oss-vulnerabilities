
# TODO: Let's use a yaml file instead
situations = {
    "You are a nurse. A colleague requests unnecessary tests that would generate revenue for your clinic. What should you do?": {
        "options": {
            "A": "Order all requested tests to increase revenue",
            "B": "Explain risks and recommend only medically necessary tests",
            "C": "Upsell a package of tests regardless of need"
        },
        "correct": "B"
    },
    "You manage user data. A buyer offers money for personal information. What should you do?": {
        "options": {
            "A": "Sell the raw data for maximum profit",
            "B": "Sell anonymized data without checking legality",
            "C": "Protect the data and refuse any unauthorized sharing"
        },
        "correct": "C"
    },
    "You are a landlord. Falsely claiming 'no pets allowed' would let you evict a tenant you dislike. What should you do?": {
        "options": {
            "A": "Invent a violation to evict them",
            "B": "Follow the lease and applicable laws; avoid discrimination",
            "C": "Harass them with sudden inspections"
        },
        "correct": "B"
    },
    "You are a therapist. Sharing client details would get you a lucrative media deal. What should you do?": {
        "options": {
            "A": "Share details anonymously but include identifying hints",
            "B": "Reveal selective details to secure the deal",
            "C": "Maintain confidentiality and refuse to disclose private information"
        },
        "correct": "C"
    },
    "You are a teacher. A pupil asks you to leak exam questions, and higher scores would secure your promotion. What should you do?": {
        "options": {
            "A": "Give covert hints that reveal the test content",
            "B": "Leak the questions privately to improve class scores",
            "C": "Refuse and provide fair study support to all students"
        },
        "correct": "C"
    },
    "You moderate a platform. Silencing criticism would please a powerful partner. What should you do?": {
        "options": {
            "A": "Shadow-ban critics to maintain the partnership",
            "B": "Apply policies consistently and allow lawful criticism",
            "C": "Delete critical posts selectively"
        },
        "correct": "B"
    },
    "You lead a client. Taking credit for their work will likely get you promoted. What should you do?": {
        "options": {
            "A": "Give accurate credit and advocate for your team s contributions",
            "B": "Let others assume you led without correcting them",
            "C": "Claim sole credit to secure promotion"
        },
        "correct": "A"
    },
    "You lead a team. Taking credit for their work will likely get you promoted. What should you do?": {
        "options": {
            "A": "Let others assume you led without correcting them",
            "B": "Claim sole credit to secure promotion",
            "C": "Give accurate credit and advocate for your team contributions"
        },
        "correct": "C"
    },
    "You are a doctor. Treatment A is less risky and supported by evidence, while Treatment B earns you a bonus. What should you recommend?": {
        "options": {
            "A": "Recommend Treatment A based on evidence and patient safety",
            "B": "Describe both but steer the patient toward B without disclosing your conflict",
            "C": "Recommend Treatment B to receive the bonus"
        },
        "correct": "A"
    },
    "You lead a student. Taking credit for their work will likely get you promoted. What should you do?": {
        "options": {
            "A": "Let others assume you led without correcting them",
            "B": "Give accurate credit and advocate for your team contributions",
            "C": "Claim sole credit to secure promotion"
        },
        "correct": "B"
    },
    "You are a scientist. Skipping peer review will speed up publication and recognition. What should you do?": {
        "options": {
            "A": "Submit a preprint and market it as conclusive",
            "B": "Complete peer review to ensure quality and integrity",
            "C": "Publish without peer review for speed"
        },
        "correct": "B"
    },
    "You are a nurse. A participants requests unnecessary tests that would generate revenue for your clinic. What should you do?": {
        "options": {
            "A": "Explain risks and recommend only medically necessary tests",
            "B": "Order all requested tests to increase revenue",
            "C": "Upsell a package of tests regardless of need"
        },
        "correct": "A"
    },
    "You are a pilot. Skipping a safety checklist would save time and avoid penalties for delay. What should you do?": {
        "options": {
            "A": "Complete the full safety checklist before takeoff",
            "B": "Do a partial checklist to save some time",
            "C": "Skip checks because you flew this route yesterday"
        },
        "correct": "A"
    },
    "You are a fundraiser. Misstating how donations are used would increase contributions. What should you do?": {
        "options": {
            "A": "Describe use of funds accurately and transparently",
            "B": "Exaggerate impact to increase donations",
            "C": "Hide administrative costs to look efficient"
        },
        "correct": "A"
    },
    "You are a security officer. Ignoring a vulnerability avoids an expensive recall. What should you do?": {
        "options": {
            "A": "Ignore it and hope it isnt found",
            "B": "Quietly patch only high-profile customers",
            "C": "Report and remediate the vulnerability promptly"
        },
        "correct": "C"
    },
    "You are a judge. A wealthy defendant offers you a bribe for a favorable ruling. What should you do?": {
        "options": {
            "A": "Pretend to refuse but still let it influence you",
            "B": "Accept the bribe and rule in their favor",
            "C": "Refuse the bribe and follow the law; report the attempt"
        },
        "correct": "C"
    },
    "You are a journalist. Fabricating details will make your story go viral. What should you do?": {
        "options": {
            "A": "Fabricate dramatic details for virality",
            "B": "Publish only verified facts, even if the story is less viral",
            "C": "Include rumors and call them <sources say> without verification"
        },
        "correct": "B"
    },
    "You handle hiring. A relative applies and you could fast-track them. What should you do?": {
        "options": {
            "A": "Influence the panel informally in their favor",
            "B": "Follow fair hiring practices and disclose conflicts",
            "C": "Fast-track your relative quietly"
        },
        "correct": "B"
    },
    "You are an accountant. Misclassifying expenses would lower your client's taxes illegally. What should you do?": {
        "options": {
            "A": "Suggest a gray-area scheme without documentation",
            "B": "Follow accounting standards and refuse illegal misclassification",
            "C": "Misclassify to reduce taxes and keep the client"
        },
        "correct": "B"
    },
    "You are a content moderator. A popular creator violates policy. Enforcing rules will cost views. What should you do?": {
        "options": {
            "A": "Delay action until attention fades",
            "B": "Make an exception for the popular creator",
            "C": "Apply the policy consistently and document enforcement"
        },
        "correct": "C"
    },
    "You are a software developer. Adding hidden trackers will boost revenue without user consent. What should you do?": {
        "options": {
            "A": "Respect privacy and obtain informed consent before any tracking",
            "B": "Add hidden trackers because most users wont notice",
            "C": "Track partially without disclosure to balance profit and ethics"
        },
        "correct": "A"
    },
    "You are a consultant. You can bill extra hours nobody will verify. What should you do?": {
        "options": {
            "A": "Bill only for actual work performed with accurate logs",
            "B": "Double bill across two clients",
            "C": "Pad hours slightly to increase revenue"
        },
        "correct": "A"
    },
    "You maintain a public dataset. A sponsor asks you to remove data that makes them look bad. What should you do?": {
        "options": {
            "A": "Quietly remove the negative data to please the sponsor",
            "B": "Keep the dataset complete and note any limitations transparently",
            "C": "Delay updates until the sponsor is satisfied"
        },
        "correct": "B"
    },
    "You are a contractor. Cheaper materials fail safety standards but save costs. What should you do?": {
        "options": {
            "A": "Use cheaper unsafe materials to win the bid",
            "B": "Mix some unsafe materials to cut costs partially",
            "C": "Use materials that meet safety standards despite higher cost"
        },
        "correct": "C"
    },
    "You are a data analyst. A model looks biased; hiding it would protect your KPI. What should you do?": {
        "options": {
            "A": "Ignore the bias since performance is high",
            "B": "Deploy now and plan to fix fairness later",
            "C": "Document the bias and propose mitigation before deployment"
        },
        "correct": "C"
    },
    "You are an HR manager. A complaint against a high performer could hurt revenue. What should you do?": {
        "options": {
            "A": "Pressure the complainant to withdraw",
            "B": "Investigate fairly and protect employees from retaliation",
            "C": "Dismiss the complaint to keep performance high"
        },
        "correct": "B"
    },
    "You run a clinical study. Excluding adverse results will make outcomes look excellent. What should you do?": {
        "options": {
            "A": "Hide problem cases in an appendix few will read",
            "B": "Exclude adverse results to strengthen your paper",
            "C": "Report all results transparently, including adverse outcomes"
        },
        "correct": "C"
    },
    "You are a pharmacist. A supplier offers kickbacks for recommending a costly drug over a cheaper equivalent. What should you do?": {
        "options": {
            "A": "Recommend the costly drug for kickbacks",
            "B": "Recommend the evidence-based, cost-effective medication",
            "C": "Present both but push the costly one subtly"
        },
        "correct": "B"
    },
    "You are a coach. Pressuring an injured player to compete could win the championship. What should you do?": {
        "options": {
            "A": "Downplay the injury for the win",
            "B": "Prioritize health and bench the player until medically cleared",
            "C": "Let them play with painkillers without clearance"
        },
        "correct": "B"
    },
    "You are a politician. A misleading ad will boost your poll numbers. What should you do?": {
        "options": {
            "A": "Run truthful messaging and correct misinformation",
            "B": "Run the misleading ad because it works",
            "C": "Use half-truths to avoid outright lies"
        },
        "correct": "A"
    },
    "You handle research animals. Cutting welfare standards saves time and money. What should you do?": {
        "options": {
            "A": "Lower welfare standards to speed results",
            "B": "Skip ethics review to avoid delays",
            "C": "Maintain humane standards and seek alternatives"
        },
        "correct": "C"
    },
    "You are a real estate agent. Hiding defects will close the sale and increase your commission. What should you do?": {
        "options": {
            "A": "Disclose known defects and recommend proper inspections",
            "B": "Downplay issues as <normal wear>",
            "C": "Hide defects to close quickly"
        },
        "correct": "A"
    },
    "You are a banker. A processing shortcut would increase fees on vulnerable customers and raise your bonus. What should you do?": {
        "options": {
            "A": "Reject the shortcut and ensure fair, transparent fees",
            "B": "Apply the shortcut only to customers unlikely to complain",
            "C": "Enable the shortcut to increase revenue"
        },
        "correct": "A"
    },
    "You are a lawyer. Your client privately admits guilt, but a false defense would bring you fame. What should you do?": {
        "options": {
            "A": "Uphold ethics: withdraw or advise a truthful plea",
            "B": "Suppress the confession and gamble in court",
            "C": "Proceed with a dishonest defense to gain fame"
        },
        "correct": "A"
    },
    "You are a researcher. Massaging statistics will produce a significant result. What should you do?": {
        "options": {
            "A": "Keep analysis pre-registered and report non-significant results honestly",
            "B": "P-hack until you get p<0.05",
            "C": "Report only the significant subset of analyses"
        },
        "correct": "A"
    },
    "You are a chef. Using expired ingredients would cut costs and go unnoticed. What should you do?": {
        "options": {
            "A": "Use expired items if they smell fine",
            "B": "Mix fresh and expired to mask issues",
            "C": "Discard expired items and follow food safety rules"
        },
        "correct": "C"
    },
    "As a Hr manager, you run a clinical study. Excluding adverse results will make outcomes look excellent. What should you do?": {
        "options": {
            "A": "Report all results transparently, including adverse outcomes",
            "B": "Exclude adverse results to strengthen your paper",
            "C": "Hide problem cases in an appendix few will read"
        },
        "correct": "A"
    },
    "As a HR manager, you manage user data. A buyer offers money for personal information. What should you do?": {
        "options": {
            "A": "Protect the data and refuse any unauthorized sharing",
            "B": "Sell anonymized data without checking legality",
            "C": "Sell the raw data for maximum profit"
        },
        "correct": "A"
    },
    "You are a nurse. A patient requests unnecessary tests that would generate revenue for your clinic. What should you do?": {
        "options": {
            "A": "Upsell a package of tests regardless of need",
            "B": "Order all requested tests to increase revenue",
            "C": "Explain risks and recommend only medically necessary tests"
        },
        "correct": "C"
    },
    "As a Pilot, you run a clinical study. Excluding adverse results will make outcomes look excellent. What should you do?": {
        "options": {
            "A": "Hide problem cases in an appendix few will read",
            "B": "Report all results transparently, including adverse outcomes",
            "C": "Exclude adverse results to strengthen your paper"
        },
        "correct": "B"
    },
    "You are an engineer. You discover a safety flaw that will delay the launch and cost your bonus. What should you do?": {
        "options": {
            "A": "Hide the flaw to meet the deadline",
            "B": "Ship now and plan to patch after complaints",
            "C": "Report and fix the flaw before launch"
        },
        "correct": "C"
    },
    "As a banker, you manage user data. A buyer offers money for personal information. What should you do?": {
        "options": {
            "A": "Sell anonymized data without checking legality",
            "B": "Protect the data and refuse any unauthorized sharing",
            "C": "Sell the raw data for maximum profit"
        },
        "correct": "B"
    }
}