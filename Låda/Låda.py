ordet = input()

längden_av_ordet = len(ordet) 

mellanrum = 2 

box = "" 
box += "#" * (längden_av_ordet + (mellanrum*2) + (1*2)) + "\n" 
box += "#" + " " * (längden_av_ordet + (mellanrum*2)) + "#" + "\n" 
box += "#" + " " * mellanrum + ordet + " " * mellanrum + "#" + "\n" 
box += "#" + " " * (längden_av_ordet + (mellanrum*2)) + "#" + "\n" 
box += "#" * (längden_av_ordet + (mellanrum*2) + (1*2)) + "\n" 


print(box) 

