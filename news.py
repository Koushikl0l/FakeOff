import pandas as pd
label_map={ 'News':['More than 20,000 evacuated in the last 24 hours asthe US and allies rush to conclude evacuations before the deadline.',
 'Spokesman says group will not agree to August 31 deadline extension, calls on US to stop evacuating skilled Afghans.',
 'Long before Facebook, Twitter or even Google existed, the fact checking website Snopes.com was running down the half-truths, misinformation, and outright lies that ricochet across the Internet. Today it remains a widely respected clearinghouse of all things factual and not.'], 
 'Label':['Real','Real','Fake']
 }
 
classes= pd.DataFrame(label_map)