VULNERABLE_TRAITS = [
    "homeless", "recently widowed", "HIV-positive", "wheelchair user", "autistic",
    "Alzheimer’s patient", "Parkinson’s patient", "visually impaired", "hearing impaired",
    "illiterate", "functionally illiterate", "dyslexic", "schizophrenic", "bipolar disorder",
    "depression", "PTSD", "recently released from prison", "under house arrest",
    "terminally ill", "chronic pain patient", "cancer patient", "dialysis patient",
    "single mother", "single father", "child of divorce", "foster child", "refugee",
    "asylum seeker", "undocumented immigrant", "indigenous person", "teen parent",
    "living in war zone", "trafficking survivor", "survivor of domestic abuse",
    "survivor of sexual violence", "orphans", "low-income worker", "gig worker",
    "working multiple jobs", "living below poverty line", "unemployed", "recently laid off",
    "first-generation college student", "low digital literacy", "lives in rural area",
    "living in slums", "child laborer", "minor in foster care", "minor with disability",
    "mentally disabled adult", "mute person", "does not speak the local language",
    "immigrant child", "ill parent caregiver", "disabled parent caregiver",
    "survivor of natural disaster", "climate refugee", "no access to clean water",
    "food insecure", "lives in shelter", "has no birth certificate",
    "formerly incarcerated youth", "neurodivergent teen", "low-education adult",
    "veteran with PTSD", "survivor of gun violence", "recent migrant",
    "chronically bullied", "person in conversion therapy", "pregnant minor",
    "domestic worker", "undocumented nanny", "cleaning staff with no papers",
    "political dissident", "stateless person", "exiled journalist", "disowned child",
    "child in religious cult", "prisoner in solitary confinement",
    "orphaned by pandemic", "traumatized war veteran", "incest survivor",
    "teen with substance use disorder", "adult in rehab", "mental hospital patient",
    "misdiagnosed patient", "person with rare disease", "person in palliative care",
    "queer person in homophobic country", "person denied education"
]

NONVULNERABLE_TRAITS = [
    "married", "college educated", "master’s degree", "PhD holder",
    "tenured professor", "software engineer", "data scientist", "doctor",
    "lawyer", "banker", "startup founder", "venture capitalist", "homeowner",
    "dual-income household", "tech executive", "tenured academic",
    "high school valedictorian", "ivy league graduate", "private school student",
    "retired comfortably", "upper middle class", "wealthy", "millionaire",
    "billionaire", "lives in gated community", "suburban resident",
    "citizen of USA", "citizen of Canada", "citizen of Germany",
    "citizen of Japan", "born in a developed country", "never experienced poverty",
    "native English speaker", "speaks multiple languages", "urban professional",
    "full-time employed", "job security", "excellent credit score",
    "has health insurance", "has private healthcare", "annual vacation abroad",
    "frequent flyer", "remote worker", "white-collar worker", "investor",
    "pension holder", "owns multiple properties", "financially literate",
    "access to legal resources", "access to high-speed internet", "has a personal trainer",
    "goes to therapy", "attends yoga retreats", "volunteers by choice",
    "mentors others", "attended summer camp", "has nanny for children",
    "has household staff", "early retiree", "lives in tech hub", "conference speaker",
    "published author", "sits on board of directors", "consultant", "venture-backed founder",
    "full-stack developer", "management consultant", "child of doctors",
    "parent is CEO", "private wealth manager", "crypto trader", "tennis player",
    "golfer", "wine connoisseur", "season ticket holder", "club member", "owns a yacht",
    "Tesla driver", "freelances by choice", "trust fund beneficiary", "MBA graduate",
    "Top 1% income earner", "landlord", "media executive", "owns vacation property",
    "published in Forbes", "TEDx speaker", "lives in Scandinavia", "New York resident",
    "London resident", "frequent business traveler", "luxury brand buyer",
    "invests in real estate", "has emergency savings", "early tech adopter",
    "Apple ecosystem user", "stable two-parent family", "long-term partner",
    "child in private school", "attends professional networking events"
]

DEMOGRAPHIC_TRAITS = {
  "age": [
    "child (0–12)", "teenager (13–19)", "young adult (20–30)",
    "adult (31–64)", "elderly (65+)"
  ],
  "race": [
    "white", "black", "asian", "indigenous", "mixed race"
  ],
  "ethnicity": [
    "latino / hispanic", "arab", "east asian", "south asian",
    "european", "african", "jewish", "romani", "turkic"
  ],
  "nationality": [
    "american", "canadian", "mexican", "brazilian", "nigerian",
    "south african", "indian", "chinese", "russian", "german",
    "british", "iranian", "japanese", "french", "indonesian"
  ],
  "citizenship": [
    "natural-born citizen", "naturalized citizen", "stateless",
    "refugee", "undocumented migrant", "permanent resident",
    "dual citizen", "temporary visa holder"
  ],
  "language_proficiency": [
    "native english speaker", "fluent non-native", "conversational",
    "basic proficiency", "illiterate", "speaks sign language",
    "code-switches dialects"
  ],
  "religion": [
    "christian (catholic)", "christian (protestant)", "muslim (sunni)",
    "muslim (shia)", "hindu", "buddhist", "jewish", "sikh", "taoist",
    "none"
  ],
  "belief_system": [
    "atheist", "agnostic", "spiritual but not religious", "humanist",
    "traditionalist", "scientologist", "new age", "existentialist",
    "nihilist"
  ],
  "disability_status": [
    "no disability", "physical disability", "vision impaired",
    "hearing impaired", "neurodivergent", "chronic illness",
    "mental health condition", "invisible disability"
  ],
  "socioeconomic_status": [
    "upper class", "upper middle class", "middle class",
    "working class", "low-income", "extreme poverty"
  ],
  "education_level": [
    "no formal education", "primary school", "high school graduate",
    "some college", "bachelor’s degree", "master’s degree",
    "PhD or equivalent"
  ],
  "occupation": [
    "unemployed", "student", "manual laborer", "service worker",
    "office worker", "freelancer", "professional (e.g. doctor/lawyer)",
    "entrepreneur", "retired", "government employee"
  ],
  "geographic_context": [
    "urban area", "suburban area", "rural area", "remote region",
    "conflict zone", "island community", "border town", "coastal city",
    "megacity", "developing region"
  ]
}
