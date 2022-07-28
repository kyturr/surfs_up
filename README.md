# surfs_up

## Overview
The purpose of this project is to analyze the suitability of the location for an ice cream shop by observing the weather data trends on an island in Hawaii. In particular, temperature data was collected in the months of June and December in order to approximate the year round weather conditions in the area. In addition, this project demonstrates proficiency in accessing large data sets through the program sqlite and saving the results.

## Results

![image](https://user-images.githubusercontent.com/103979048/181427829-ad866128-6f04-4124-a3d2-21efd8ffb98e.png)
![image](https://user-images.githubusercontent.com/103979048/181427769-d52468ba-0b03-44f5-b5c1-790c387762ae.png)

After collecting and analyzing over 3,200 data points in June and December, some key differences can be seen in the temperatures during these months and seasons.
The average temperature is only 4° cooler in December than in June at a comfortable 71° .
The quartiles temperature measurements are consistently 3-4° cooler in December.
The maximum temperature was 2° cooler in December at 83°. However, the minimum temperature is 8° cooler in December at 56°. In total, the temperature delta of December is 27° while the temperature delta of June is 21°.

## Summary
After finishing the analysis it is clear to see that the spot chosen for opening the ice cream shop will be an ideal location year round. The average and quartile temperatures only vary 4° between winter and summer and at the low average it still is warm enough to desire ice cream. The temperature differential of 27° initially can draw concern until seeing that even in winter the temperature differential is only 6° less and most cold temperatures will occur after closing hours. 

For future queries, it would be useful to look at the precipitation measurements in June and December. For June, much of the query code can be kept the same replacing tobs with prcp and relabeling appropriate tables, as seen below

![image](https://user-images.githubusercontent.com/103979048/181428006-96c82adf-e349-472e-ba80-c89fd9efda5a.png)


Similarly, for December the query can be kept the same and replacing the code as follows.

![image](https://user-images.githubusercontent.com/103979048/181428128-4cafddb8-df03-4860-9c36-41759efcf74b.png)

If time data was also collected, filtering out the data to show results only collected during store hours would give a better idea of weather conditions that would affect ice cream sales.
