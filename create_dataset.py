import pandas as pd
import os

fake_data = {
    'title': [
        'BREAKING: Aliens land in New York City',
        'Government secretly puts chips in vaccines',
        'Scientists prove earth is flat',
        'Bill Gates controls the weather',
        'COVID vaccine turns people into robots',
        'Moon landing was filmed in Hollywood',
        'Obama born in Kenya confirmed',
        'Drinking bleach cures cancer says doctor',
        'Giant lizards run the government',
        'Pizza shop runs secret underground lab',
        '5G towers spread coronavirus',
        'Elvis Presley spotted at Walmart',
        'Water fluoridation causes mind control',
        'Chemtrails are government poison',
        'Bigfoot caught on camera in Texas'
    ],
    'text': [
        'Multiple witnesses report seeing UFOs land near Times Square last night.',
        'Anonymous source claims microchips are hidden inside vaccine doses.',
        'A group of independent researchers claim new evidence supports flat earth.',
        'Conspiracy theorists link weather patterns to Bill Gates foundation.',
        'False claims spread on social media about vaccine side effects.',
        'Theorists claim NASA faked the moon landing in a movie studio.',
        'Repeatedly debunked claim resurfaces on social media platforms.',
        'Dangerous medical misinformation spreads across online forums.',
        'Wild conspiracy theory claims reptilian aliens control world leaders.',
        'False rumors spread about a family pizza restaurant in Washington.',
        'Misinformation links 5G network towers to spread of COVID-19.',
        'Tabloid claims Elvis was seen alive shopping at a Walmart store.',
        'Anti-fluoride activists spread false claims about water supplies.',
        'Conspiracy theorists claim airplane contrails contain harmful chemicals.',
        'Blurry video footage claimed to show Bigfoot walking in Texas woods.'
    ],
    'label': [0]*15
}

real_data = {
    'title': [
        'President signs new climate change bill into law',
        'Stock markets rise after positive jobs report',
        'Scientists develop new cancer treatment method',
        'UN holds emergency meeting on global food crisis',
        'NASA successfully launches new Mars rover mission',
        'Supreme Court rules on landmark immigration case',
        'Tech companies face new data privacy regulations',
        'Researchers find new evidence of ancient civilization',
        'Global temperatures reach record high this decade',
        'WHO announces progress in malaria vaccine trials',
        'New study links exercise to improved mental health',
        'Congress passes infrastructure spending bill',
        'Electric vehicle sales hit record numbers in 2024',
        'International space station celebrates 25 years',
        'Renewable energy surpasses coal power generation'
    ],
    'text': [
        'The president signed comprehensive climate legislation targeting carbon emissions.',
        'Wall Street indices climbed after the labor department reported strong job growth.',
        'Medical researchers have developed a promising new approach to treating cancer cells.',
        'United Nations officials gathered to address the growing global food shortage crisis.',
        'NASA launched its latest Mars exploration rover on a mission to search for signs of life.',
        'The Supreme Court issued a major ruling affecting immigration policies across the country.',
        'New legislation will require technology companies to better protect user data and privacy.',
        'Archaeological discoveries suggest an ancient civilization existed earlier than thought.',
        'Climate scientists report that global average temperatures have hit a new record high.',
        'The World Health Organization announced significant progress in testing malaria vaccines.',
        'A large study confirms that regular physical exercise significantly improves mental health.',
        'The US Congress approved a major bill to fund road, bridge and broadband infrastructure.',
        'Sales of electric vehicles reached an all time high driven by new models and incentives.',
        'The international space station marked 25 years of continuous human habitation in orbit.',
        'For the first time renewable energy sources have generated more power than coal plants.'
    ],
    'label': [1]*15
}

fake_df = pd.DataFrame(fake_data)
real_df = pd.DataFrame(real_data)

os.makedirs('data', exist_ok=True)
fake_df.to_csv('data/Fake.csv', index=False)
real_df.to_csv('data/True.csv', index=False)

print("Dataset created successfully!")
print(f"Fake news samples: {len(fake_df)}")
print(f"Real news samples: {len(real_df)}")