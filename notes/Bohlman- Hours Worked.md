|Date              |Hours Worked      |Worked On|
|---|---|---|
|9/15/2016         |2                 |Introduction to AO, overview of the future projects, specifics for the project in terms of software|
|9/16/2016         |2                 |Installed, Notepad++, Git, Anaconda, pip. All seem to be functioning (No idea how to use most of them...). Photulis install failed (building wheel failed). Awaiting further instruction for troubleshooting + instruction|
|9/17/2016         |4                 |Troubleshooted with Ubuntu computer for use with dewar, Practiced Python on Codecademy (syntax, strings/console output, conditionals/control flow, functions)|
|9/19/2016         |2                 |Worked on dewar Ubuntu computer configuration, but couldn't connect to Internet. Assembled the dewar flask and started running the vacuum in order to purge it of air.|
|9/20/2016         |3                 |Completed Functions and Lists/Dictionaries in Codeacademy's Python course. Finished GitHub introductory tutorial|
|9/21/2016         |2.25              |Opened dewar, tried to install astropy, ds9 and other necessary python programs, but couldn't. Starting thread on pyds9 to discuss error. Put temperature sensor inside of dewar and proceeded to reseal it in order to vacuum it again. Awaiting further instructions.|
|9/23/2016         |4.25              |tried to install astropy (no avail), learned how to work with fits images in python, started project of graphing integration time of fits images versus count, finished with plot of ints vs counts|
|9/27/2016         |3.5               |worked with Phil and cooled the dewar with liquid nitrogen, project notes are on githubs|
|9/28/2016         |1                 |worked with Phil on clio computer, got all of the drivers unzipped and installed, but Phil has to work with them to make sure they're installed correctly. Computer project is now at standstill for me. Opened up dewar again to install new equipment, but that will happen later.|
|9/29/2016         |2.25              |worked with python in analyzing fits images, uploaded the best line fit (up to 2000 ints) and the plot of ints vs counts, attempted to work on true counts vs. measured counts, very nearly there.|
|10/03/2016        |2                 |worked with python in analyzing the error of the counts of each of the fits images, by using the desired linear relationship, a quadratic relationship, a cubic relationship, and a quartic relationship.|
|10/05/2016        |2                 |worked with python in actually finishing the correct true counts vs. measured counts plots, cleaned up code, and made separate plots of true vs measured c, a linear fit to good data of that, a quadratic fit to good data of that, a cubic fit to good data of that, and a quartic fit to good data of that|
|10/06/2016        |3.25              |worked with python in seeing which polynomial matched up with the linear fit the best for a bit, but then started working with the dewar. Opened the new detector and tried to install it, however, some problems were incurred. The detector was eventually successfully installed, a temp. sensor was attached to it, and the dewar was closed and the vacuum pump started pumping.|
|10/07/2016        |3.5 (3 on TS)     |dewar dewar DEWAR|
|10/10/2016        |4.5               |cooling the dewar: an exercise in patience and lack of liquid nitrogen|
|10/13/2016        |5                 |cooling the dewar, take 2|
|10/18/2016        |4                 |worked on python, separated everything in modules, figured out jagged line problem, discussed why the polynomial error lines do not work with the desired relationship|
|10/19/2016        |3                 |worked on python, trying to get linearity to work, separated detector from dewar and found out equipment was alright, WEAR GLOVES|
|10/21/2016        |3                 |worked on python, started writing report, after adjusting and organizing some stuff, found that second order was almost fitting the desired relationship|
|10/25/2016        |2.5               |worked on python, updated all 3 files and organized all of the notes, data, and code, on github and on laptop. Uploaded all to github. Discussed options for filling dewar, will probably happen beginning of next week. Cranked out a very rough copy of the report, to discuss with Katie later.|
|10/26/2016        |3                 |discussed very first draft of scientific journal, Katie gave me notes, brought up idea of testing original data set in order to check the process of my code, tested original data: coefficients of linear lined up fairly well, third order did not. Maybe something to do with polyfit, come up with different way to find curve|
|10/28/2016        |2.25               |worked on analyzing data from 2013 to see if it matches Katie's results, it did not for me, discussed possible sources of error in terms of what she did and I did (placed some things to work on below), discussed her leaving until the 23 and what that entails for what I have to do to stay on top of things and update her.|
|11/1/2016         |2                |worked on the fix for ds9, got stuck, emailed Katie for guidance, starting working on making sure a second order equation would have no error in my second order error, found out that for perfectly second ordered equations, there's an error of about 10^-13. For perfect third order equations, error is 10^-12. Unsure if that has an effect on my data.|
|11/3/2016         |3.25              |worked on fix for ds9, tried reinstalling certain programs like cygwin to see if that was the root of the problem and posted to forum, tried to clean up code for original data to make it fit better, worked on new linearity report for original data. uploaded that |
|11/4/2016         |3                  |Attempted a fix to ds9, contributor says that he's still using appveyor to fix the program, will try more next week and see if cygwin is updated, started wrapping up original data linearity report and program for analysis of the original data, uploaded those|
|11/8/2016         |2.5             |Spoke with Katie on skype to update each other on the progress being made for data, organized to do list into bullet list/formatted with md, error wasn't due to pixel count due to both 200 through 350 and going from 0 to 200, Katie did mean for the counts, I believe I did the same thing (I added them up and divided by 5), started playing with linear coefficients to see if changing them helps, will finish next time|
|11/10/2016        |3               |Finished organizing/commented the programs used to analyze the original data, sucked at making an md file so I decided to create a pull request and work on that later|
|11/15/2016       |2.5              |Finished the md file, needs to be approved and added to master branch? (not exactly sure on this, but it's finished in the pull request,  updated report with more explanations, tinerked with my program to calculate coefficients, will upload that on Github tomorrow.|
|11/16/2016       |3                |Tried altering coefficients on error of linearity program to what was on the report, CANNOT USE THIRD ORDER COEFFICIENTS BECAUSE I HAVE NO CLUE WHAT THEY ARE (ones in the report aren't the correct ones at all.... do I need to look in the idl file?), worked extensive only coding/ the original report/ looking at idl file to find comparisons between what I did and what Katie did, uploaded those files onto github|
|11/18/2016       |3                |I did stuff last Friday but didn't record it and I can't remember it :( I believe it was along the lines of consolidating my code to one file (which I will upload), organizing my project files for this, and working on the project reports for both, as well as emailing Katie explaining what I was doing.|
|11/22/2016       |2                |Read http://matplotlib.org/api/pyplot_summary.html, looking for useful coding practices to make my graphs better, got started on implementing those pieces of code into the actual code files, tomorrow I will redo the graphs to see what works best and then upload everything to github.|
|11/23/2016       |2                |finished organizing the files on here and the project files on my laptop, finished writing the code for the better graphs, upload a sample graph to the github page, uploaded the updated coding files I wrote|
|11/28/2016       |2                |caught up with Katie on projects, discussed fit lines as well as scheduling for this semester and next semester, changed all graphs to have legend/be cleaner, uploaded them to the github page|
|11/29/2016       |3                |Replaced all images in reports with updated graphs, uploaded new reports, worked on idl fit with Katie, updated my own wrongdoing in my code, organized/deleted files in github, uploaded updated files|
|11/30/2016       |3                |Played with coefficients to determine if there was a good fit for any of the polynomial fits for the data, compared my findings with Katie's, applied corrections to 2014 data/programming set|
|12/2/2016       |2               |Edited the reports to include a more current analysis, uploaded them to the github page, finished organizing/deleting items on the github page|
|12/6/2016       |3.5              |Fixed code and came up with coefficients that were similar to Katie's coefficients, tried to apply corrections to data in order to finish this project, failed so I will come back tomorrow and hopefully finish it before the end of the semester|
|12/7/2016       |3             |tried to fix code to apply linearity correctly, original coefficients were put in, but the graph ended up being the same as before, trying to find why the correction does not hold as a straight line when I apply it to the data, fixed it and came up with a correct graph, updated reports, uploaded everything to the github page, wrapped up the remaining topics of this year|
|1/11/2017       |4             |refreshed myself on what I did last year, starting organizing my code so that it's legible and concise and started consolidating my results into the report format, deleted and optimized code so that I could get it to it's final state, tried to fix error of linearity graph by comparing it to Katie's graph, almost got it but it's still messed up|
|1/12/2017       |2             |Fixed report and freshened up code for the original data, uploaded it to github. Katie is going to review the report and tell me her thoughts, at which point I'll correct my report as needed, and then try to fix the newer data, because I left that project at an unfinished point because I was having problems with it, and I have solved the issues now.|
|1/13/2017       |2.5             |Katie had already looked at my report and marked it up, so I attempted to fix the comments on it. Got through fixing all of it, updated my code and finally cleaned it up, and put it all on the github. My departure from linearity graph is still a little eh, but I tried fixing it the best I could. Katie said she'll graph the data herself soon to see what the gets for third/fourth order for departure from linearity. Organized work files on computer and on github, consolidated code and organized everything so the process will become automated once I fix the later data set's code, started repurposing report for new data in order to make it up to speed so the fixing of the code can be a litle bit easier later|
|1/17/2017       |2             |Applied corrections to old code in order to analyze the newer data set, did that, fixed the report for the new data, uploaded both files to github, error of linearity is still off so I'll have to check out what fixes I will have to make to the code|
|1/18/2017       |4             |Tried to troubleshoot the lienarity graphs, sort of fixed them, but didn't get it to what I precisely wanted. That being said, I tightened up all my graphs and the report, and I can safetly say that I have finished them, to a ceratin extent.|
|1/19/2017       |1             |Writing up/editing reports and uploading them to github|
|1/24/2017       |2             |Discussing spacegrant due dates and what needs to be done in order to meet those dates, working on reports and wrapping those up as well, uploaded fixed reports and code to github|
|1/25/2017       |2.5             |Recieved both corrected reports back and edited them, renamed and corrected python files, and reuploaded all to github, Katie recieved them both and will correct them/look at the updated code in time for tomorrow. From then on, I have to refine the code and start making a presentation out of it|
|1/26/2017       |2             |Katie looked over code/reports that I wrote, I worked on my symposium prep and the paragraph for linearity|
|1/27/2017       |3.5            |Katie was trying to transfer over a different data set, I downloaded it and recieved instructions on how to analyze it. I finished my research on detectors and updated/uploaded my new reports. Uploaded my symposium prep document to the github page, probably won't need to open that for awhile|
|1/31/2017       |2.5            |Started writing coding files for next data set, uploaded my progresson those to github|
|2/1/2017       |2            |Decided to try and import 4 files and do the correctiosn on them in order to gain a better understanding of what to do. Started on it, placed the code for it on top of the file I made yesterday, uploaded to github.|
|2/2/2017       |2            |Attempted to code the process of writing images, subtract the two images, and then making a new image. At the conclusion of my shift, I got my program to output a file, but like, it doesn't have anything on it. I need to find a way to translate values from one array to another in my program, and i will focus on that tomorrow. Code/picture outputted is uploaded|
|2/3/2017       |1            |Emailed Katie about my weekly progress, continued trying to fix my numpy arrays|
|2/8/2017       |2            |Literally give up holy crap. Troubleshooting for ~2 hours trying to engineer my program to read in these files and outputting files. Having problems with data remaing in objects and not being pushed to lists, and with numpy arrays.|
|2/9/2017       |2            |No work yesterday because I has the stomach flu :(, but I'm back today! Awaiting Katie's response, but I'm reallt trying here to import data, discovered problem was with rrading in fits cube, wrote out a band aid solution taht kinda helped the problem, as I am able to read in values now, but I am still outputting black images. Code is updated.|
|2/10/2017       |2.5            |Fixed the read ins and got the counts for every pixel in the first 4 pictures, but now need to take the list and output it to a picture. Maybe do that with a numpy array...|
|2/14/2017       |2          |Got my program to work for the first 4 images. It reads in an image, reads in every pixel, applys the correction to the pixel, puts every new value into an array, and generates an image and prints that image out.Problems I had with making this included the itemset() function, scidata arguments, and just working with numpy arrays in general. However, I feel like the program now works. Uploaded the working program and the fixed 4 images|
|2/15/2017       |2          |Organized my program, and worked on subtracting the paired images from each other. Got a completely white image, so I'm going to have to refine my program tomorrow and see where the problem is.|
|2/16/2017       |2          |tried to subtract the images better, so I don't get whitespace. Got it to work for the first 2 images, modified my code to produce it for the next two images. In the near future, I will modidy my code to work universally with different files.|
|2/17/2017       |2          |Started organizing my code to optimize it, waiting for Katie's response so I know what to do with the numbering of the pictures.|
|2/21/2017       |2          |Can't work tomorrow, have a dr's appt at one ish. Anyways, today, I started taking in all of the files names so I can run the program for every single file. I then tried to work on the code for subtracting the files after taking them in in groups of 4|
|2/23/2017       |2          |Analyzed my program to make sure it works tried to add the rest of the file names to the program. Trying to optimize my code.|
|2/24/2017       |4          |Redid my code and gotit up to the specifications required to subtract all of the images, realized that there may be a problem with my coefficients, as the fixed images are having counts less than the original counts for the images. WHich doesn't make sense. What we are looking for is a slight increase in image counts at any given point, so we have to look at the coefficients I derived in order to see what the hell is going on.|
|2/28/2017       |1.5          |Worked on my abstract a little, uplaoded the rough draft|
|3/1/2017        |3.5          |Katie graded my abstract so I corrected it, finished long form abstract, finished the short form abstract, I worked on the coefficients for calibrating the second data setand realized I put the wrong coefficients in, images now fixed.|
|3/2/2017        |2          |Finzalized my abstract to 158 words, started working on the presentation (uploaded it)|


2 MONTHS TO PRESENTING IN PHOENIX
 
**To do:**
* Ask about hotel accomadations during the symposium
* wait on pyds9 fix
* do stuff with the detector in the dewar
* work on a graph of a horizontal or vertical slice of pixels so it looks sort of like a gaussian
     |                       _        
     |                      / \
     |                    /     \
     |              _   /         \    _
     |_____________/ \_/            \_/  \________________________
     |
     |____________________________________________________________

On the x axis, it's each pixel
On the y axis, it's number of counts
**Important dates:**
* March 22, 2017 - Symposium Abstracts DUE NOTE: Late abstracts will not be accepted without a compelling reason and Space Grant Management concurrence.
* TBA - Mentor & Guest RSVPs DUE
* April 7, 2017 -  Presentations DUE
* April 14, 2017 -  ASCEND Presentations DUE
* April 21, 2017 - Statewide Symposium Banquet
* April 22, 2017 - Statewide Symposium
