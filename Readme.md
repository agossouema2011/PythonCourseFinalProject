# What does it contain?
This repository contains the final project for the course
"Introduction to Python for Data Analysis and Automation in Biology”.

## Description
### Background
For my PhD research, I am working with deep learning method for pathology detection in capsule endoscopy using bounding boxes annotations. One of the open-source datasets I am using is Kvasir Capsule (https://osf.io/dv2ag/). Kvasir Capsule is a large capsule endoscopy dataset collected from examinations at Hospitals in Norway. Kvasir-Capsule consists of 117 videos which can be used to extract a total of 4,741,504 image frames. They have labelled and medically verified 47,238 frames with a bounding box around detected anomalies from 14 different classes of findings.. For my work I consider images from the eight most representative pathology classes amounting to a total of 3,365 images with their ground truth annotations. We convert the dataset annotation into a coco JSON file which we use for the analysis in this code.

### Structure of the coco JSON file
The coco JSON file containing the dataset annotations has a structure as follows ( This is just an example of an image annotation):

![image](https://github.com/user-attachments/assets/299e9f4f-35c0-42a0-baa0-1a58fabc4e3d)


### Objective
The objective of this code is to provide a rapid analysis of the dataset and help have an overview of its contents.
This code can be used to get an overview of the content of any dataset which coco annotation JSON file is provided.
We mainly analyse the coco JSON file containing the annotations for the 8 pathological classes we considered, and provide the following:
1) The total Number of images
2) The annotations per category (class)
3) The histogram of number of annotations per pathology
4) The list of images having a given pathology

### Requirement
Install few libraries for python such as:
- install matplotlib
- install numpy
  
### Run the code
```shell script
           python jsonfile.py
```

### Results and screenshot

Number of image: 3365 <br>
<br>
Category ID 1: Blood-fresh: 357 annotations<br>
Category ID 0: Angiectasia: 693 annotations<br>
Category ID 5: Lymphangiectasia: 473 annotations<br>
Category ID 2: Erosion: 405 annotations<br>
Category ID 6: Polyp: 44 annotations<br>
Category ID 7: Ulcer: 680 annotations<br>
Category ID 4: Foreign-Body: 621 annotations<br>
Category ID 3: Erythema: 92 annotations<br><br>

List of images for Pathology Category ID 1: Blood-fresh<br><br>
['04a78ef00c5245e0_11213.jpg', '04a78ef00c5245e0_11214.jpg', '04a78ef00c5245e0_11215.jpg', '04a78ef00c5245e0_11217.jpg', '04a78ef00c5245e0_11218.jpg', '04a78ef00c5245e0_11219.jpg', '04a78ef00c5245e0_11220.jpg', '04a78ef00c5245e0_11221.jpg', '04a78ef00c5245e0_11222.jpg', '04a78ef00c5245e0_11223.jpg', '04a78ef00c5245e0_11224.jpg', '04a78ef00c5245e0_11227.jpg', '04a78ef00c5245e0_11231.jpg', '04a78ef00c5245e0_11232.jpg', '04a78ef00c5245e0_11233.jpg', '04a78ef00c5245e0_11234.jpg', '04a78ef00c5245e0_11235.jpg', 'd369e4f163df4aba_12012.jpg', 'd369e4f163df4aba_12013.jpg', 'd369e4f163df4aba_12014.jpg', 'd369e4f163df4aba_12015.jpg', 'd369e4f163df4aba_12016.jpg', 'd369e4f163df4aba_12017.jpg', 'd369e4f163df4aba_12018.jpg', 'd369e4f163df4aba_12019.jpg', 'd369e4f163df4aba_12020.jpg', 'd369e4f163df4aba_12021.jpg', 'd369e4f163df4aba_12022.jpg', 'd369e4f163df4aba_12024.jpg', 'd369e4f163df4aba_12025.jpg', 'd369e4f163df4aba_12026.jpg', 'd369e4f163df4aba_12027.jpg', 'd369e4f163df4aba_12029.jpg', 'd369e4f163df4aba_12030.jpg', 'd369e4f163df4aba_12031.jpg', 'd369e4f163df4aba_12033.jpg', 'd369e4f163df4aba_12034.jpg', 'd369e4f163df4aba_12036.jpg', 'd369e4f163df4aba_12038.jpg', 'd369e4f163df4aba_12041.jpg', 'd369e4f163df4aba_12042.jpg', 'd369e4f163df4aba_12043.jpg', 'd369e4f163df4aba_12044.jpg', 'd369e4f163df4aba_12046.jpg', 'd369e4f163df4aba_12047.jpg', 'd369e4f163df4aba_12048.jpg', 'd369e4f163df4aba_12049.jpg', 'd369e4f163df4aba_12050.jpg', 'd369e4f163df4aba_12052.jpg', 'd369e4f163df4aba_12053.jpg', 'd369e4f163df4aba_12054.jpg', 'd369e4f163df4aba_12055.jpg', 'd369e4f163df4aba_12056.jpg', 'd369e4f163df4aba_12057.jpg', 'd369e4f163df4aba_12058.jpg', 'd369e4f163df4aba_12060.jpg', 'd369e4f163df4aba_12061.jpg', 'd369e4f163df4aba_12062.jpg', 'd369e4f163df4aba_12063.jpg', 'd369e4f163df4aba_12064.jpg', 'd369e4f163df4aba_12065.jpg', 'd369e4f163df4aba_12066.jpg', 'd369e4f163df4aba_12068.jpg', 'd369e4f163df4aba_12070.jpg', 'd369e4f163df4aba_12072.jpg', 'd369e4f163df4aba_12073.jpg', 'd369e4f163df4aba_12074.jpg', 'd369e4f163df4aba_12075.jpg', 'd369e4f163df4aba_12076.jpg', 'd369e4f163df4aba_12077.jpg', 'd369e4f163df4aba_12078.jpg', 'd369e4f163df4aba_12080.jpg', 'd369e4f163df4aba_12081.jpg', 'd369e4f163df4aba_12082.jpg', 'd369e4f163df4aba_12092.jpg', 'd369e4f163df4aba_12093.jpg', 'd369e4f163df4aba_12094.jpg', 'd369e4f163df4aba_12095.jpg', 'd369e4f163df4aba_12097.jpg', 'd369e4f163df4aba_13296.jpg', 'd369e4f163df4aba_13298.jpg', 'd369e4f163df4aba_13311.jpg', 'd369e4f163df4aba_13313.jpg', 'd369e4f163df4aba_13314.jpg', 'd369e4f163df4aba_13315.jpg', 'd369e4f163df4aba_13317.jpg', 'd369e4f163df4aba_13318.jpg', 'd369e4f163df4aba_13322.jpg', 'd369e4f163df4aba_13324.jpg', 'd369e4f163df4aba_13326.jpg', 'd369e4f163df4aba_13327.jpg', 'd369e4f163df4aba_13329.jpg', 'd369e4f163df4aba_13330.jpg', 'd369e4f163df4aba_13331.jpg', 'd369e4f163df4aba_13332.jpg', 'd369e4f163df4aba_13333.jpg', 'd369e4f163df4aba_13335.jpg', 'd369e4f163df4aba_13336.jpg', 'd369e4f163df4aba_13337.jpg', 'd369e4f163df4aba_13338.jpg', 'd369e4f163df4aba_13339.jpg', 'd369e4f163df4aba_13351.jpg', 'd369e4f163df4aba_13352.jpg', 'd369e4f163df4aba_13353.jpg', 'd369e4f163df4aba_13354.jpg', 'd369e4f163df4aba_13357.jpg', 'd369e4f163df4aba_13358.jpg', 'd369e4f163df4aba_13359.jpg', 'd369e4f163df4aba_13361.jpg', 'd369e4f163df4aba_13363.jpg', 'd369e4f163df4aba_13364.jpg', 'd369e4f163df4aba_13365.jpg', 'd369e4f163df4aba_13366.jpg', 'd369e4f163df4aba_13367.jpg', 'd369e4f163df4aba_13369.jpg', 'd369e4f163df4aba_13371.jpg', 'd369e4f163df4aba_13372.jpg', 'd369e4f163df4aba_13373.jpg', 'd369e4f163df4aba_13374.jpg', 'd369e4f163df4aba_13375.jpg', 'd369e4f163df4aba_13376.jpg', 'd369e4f163df4aba_13377.jpg', 'd369e4f163df4aba_13378.jpg', 'd369e4f163df4aba_13379.jpg', 'd369e4f163df4aba_13380.jpg', 'd369e4f163df4aba_13381.jpg', 'd369e4f163df4aba_13382.jpg', 'd369e4f163df4aba_13383.jpg', 'd369e4f163df4aba_13384.jpg', 'd369e4f163df4aba_13385.jpg', 'd369e4f163df4aba_13386.jpg', 'd369e4f163df4aba_13387.jpg', 'd369e4f163df4aba_13388.jpg', 'd369e4f163df4aba_13389.jpg', 'd369e4f163df4aba_13390.jpg', 'd369e4f163df4aba_13391.jpg', 'd369e4f163df4aba_13393.jpg', 'd369e4f163df4aba_13395.jpg', 'd369e4f163df4aba_13407.jpg', 'd369e4f163df4aba_13408.jpg', 'd369e4f163df4aba_13409.jpg', 'd369e4f163df4aba_13410.jpg', 'd369e4f163df4aba_13412.jpg', 'd369e4f163df4aba_13414.jpg', 'd369e4f163df4aba_13417.jpg', 'd369e4f163df4aba_13418.jpg', 'd369e4f163df4aba_13420.jpg', 'd369e4f163df4aba_13421.jpg', 'd369e4f163df4aba_13422.jpg', 'd369e4f163df4aba_13425.jpg', 'd369e4f163df4aba_13426.jpg', 'd369e4f163df4aba_13427.jpg', 'd369e4f163df4aba_13428.jpg', 'd369e4f163df4aba_13429.jpg', 'd369e4f163df4aba_13430.jpg', 'd369e4f163df4aba_13431.jpg', 'd369e4f163df4aba_13432.jpg', 'd369e4f163df4aba_13433.jpg', 'd369e4f163df4aba_13434.jpg', 'd369e4f163df4aba_13435.jpg', 'd369e4f163df4aba_13436.jpg', 'd369e4f163df4aba_13437.jpg', 'd369e4f163df4aba_13438.jpg', 'd369e4f163df4aba_13439.jpg', 'd369e4f163df4aba_13440.jpg', 'd369e4f163df4aba_13441.jpg', 'd369e4f163df4aba_13442.jpg', 'd369e4f163df4aba_13443.jpg', 'd369e4f163df4aba_13445.jpg', 'd369e4f163df4aba_13447.jpg', 'd369e4f163df4aba_13448.jpg', 'd369e4f163df4aba_13449.jpg', 'd369e4f163df4aba_13450.jpg', 'd369e4f163df4aba_13451.jpg', 'd369e4f163df4aba_13452.jpg', 'd369e4f163df4aba_13453.jpg', 'd369e4f163df4aba_13454.jpg', 'd369e4f163df4aba_13455.jpg', 'd369e4f163df4aba_13456.jpg', 'd369e4f163df4aba_13457.jpg', 'd369e4f163df4aba_13458.jpg', 'd369e4f163df4aba_13460.jpg', 'd369e4f163df4aba_13461.jpg', 'd369e4f163df4aba_13463.jpg', 'd369e4f163df4aba_13464.jpg', 'd369e4f163df4aba_13466.jpg', 'd369e4f163df4aba_13467.jpg', 'd369e4f163df4aba_13468.jpg', 'd369e4f163df4aba_13469.jpg', 'd369e4f163df4aba_13470.jpg', 'd369e4f163df4aba_13471.jpg', 'd369e4f163df4aba_13472.jpg', 'd369e4f163df4aba_13473.jpg', 'd369e4f163df4aba_13474.jpg', 'd369e4f163df4aba_13475.jpg', 'd369e4f163df4aba_13476.jpg', 'd369e4f163df4aba_13477.jpg', 'd369e4f163df4aba_13478.jpg', 'd369e4f163df4aba_13479.jpg', 'd369e4f163df4aba_13480.jpg', 'd369e4f163df4aba_13481.jpg', 'd369e4f163df4aba_13482.jpg', 'd369e4f163df4aba_13483.jpg', 'd369e4f163df4aba_13484.jpg', 'd369e4f163df4aba_13485.jpg', 'd369e4f163df4aba_13486.jpg', 'd369e4f163df4aba_13487.jpg', 'd369e4f163df4aba_13489.jpg', 'd369e4f163df4aba_13490.jpg', 'd369e4f163df4aba_13491.jpg', 'd369e4f163df4aba_13492.jpg', 'd369e4f163df4aba_13493.jpg', 'd369e4f163df4aba_13494.jpg', 'd369e4f163df4aba_13495.jpg', 'd369e4f163df4aba_13496.jpg', 'd369e4f163df4aba_13497.jpg', 'd369e4f163df4aba_13498.jpg', 'd369e4f163df4aba_13499.jpg', 'd369e4f163df4aba_13500.jpg', 'd369e4f163df4aba_13501.jpg', 'd369e4f163df4aba_13502.jpg', 'd369e4f163df4aba_13503.jpg', 'd369e4f163df4aba_13505.jpg', 'd369e4f163df4aba_13506.jpg', 'd369e4f163df4aba_13507.jpg', 'd369e4f163df4aba_13508.jpg', 'd369e4f163df4aba_13510.jpg', 'd369e4f163df4aba_13511.jpg', 'd369e4f163df4aba_13513.jpg', 'd369e4f163df4aba_13514.jpg', 'd369e4f163df4aba_13515.jpg', 'd369e4f163df4aba_13516.jpg', 'd369e4f163df4aba_13518.jpg', 'd369e4f163df4aba_13519.jpg', 'd369e4f163df4aba_13520.jpg', 'd369e4f163df4aba_13521.jpg', 'd369e4f163df4aba_13522.jpg', 'd369e4f163df4aba_13523.jpg', 'd369e4f163df4aba_13524.jpg', 'd369e4f163df4aba_13526.jpg', 'd369e4f163df4aba_13527.jpg', 'd369e4f163df4aba_13528.jpg', 'd369e4f163df4aba_13529.jpg', 'd369e4f163df4aba_13530.jpg', 'd369e4f163df4aba_13533.jpg', 'd369e4f163df4aba_13534.jpg', 'd369e4f163df4aba_13535.jpg', 'd369e4f163df4aba_13536.jpg', 'd369e4f163df4aba_13537.jpg', 'd369e4f163df4aba_13540.jpg', 'd369e4f163df4aba_13541.jpg', 'd369e4f163df4aba_13542.jpg', 'd369e4f163df4aba_13543.jpg', 'd369e4f163df4aba_13544.jpg', 'd369e4f163df4aba_14188.jpg', 'd369e4f163df4aba_14190.jpg', 'd369e4f163df4aba_14191.jpg', 'd369e4f163df4aba_14192.jpg', 'd369e4f163df4aba_14193.jpg', 'd369e4f163df4aba_14195.jpg', 'd369e4f163df4aba_14196.jpg', 'd369e4f163df4aba_14197.jpg', 'd369e4f163df4aba_14199.jpg', 'd369e4f163df4aba_14200.jpg', 'd369e4f163df4aba_14201.jpg', 'd369e4f163df4aba_14202.jpg', 'd369e4f163df4aba_14203.jpg', 'd369e4f163df4aba_14206.jpg', 'd369e4f163df4aba_14207.jpg', 'd369e4f163df4aba_14208.jpg', 'd369e4f163df4aba_14209.jpg', 'd369e4f163df4aba_14210.jpg', 'd369e4f163df4aba_14212.jpg', 'd369e4f163df4aba_14228.jpg', 'd369e4f163df4aba_14229.jpg', 'd369e4f163df4aba_14237.jpg', 'd369e4f163df4aba_14239.jpg', 'd369e4f163df4aba_14240.jpg', 'd369e4f163df4aba_14242.jpg', 'd369e4f163df4aba_14243.jpg', 'd369e4f163df4aba_14245.jpg', 'd369e4f163df4aba_14246.jpg', 'd369e4f163df4aba_14247.jpg', 'd369e4f163df4aba_14248.jpg', 'd369e4f163df4aba_14249.jpg', 'd369e4f163df4aba_14250.jpg', 'd369e4f163df4aba_14266.jpg', 'd369e4f163df4aba_14268.jpg', 'd369e4f163df4aba_14271.jpg', 'd369e4f163df4aba_15562.jpg', 'd369e4f163df4aba_15563.jpg', 'd369e4f163df4aba_15564.jpg', 'd369e4f163df4aba_15565.jpg', 'd369e4f163df4aba_15567.jpg', 'd369e4f163df4aba_15568.jpg', 'd369e4f163df4aba_15569.jpg', 'd369e4f163df4aba_15570.jpg', 'd369e4f163df4aba_15571.jpg', 'd369e4f163df4aba_15572.jpg', 'd369e4f163df4aba_15574.jpg', 'd369e4f163df4aba_15575.jpg', 'd369e4f163df4aba_15576.jpg', 'd369e4f163df4aba_15578.jpg', 'd369e4f163df4aba_15580.jpg', 'd369e4f163df4aba_15581.jpg', 'd369e4f163df4aba_15582.jpg', 'd369e4f163df4aba_15583.jpg', 'd369e4f163df4aba_15584.jpg', 'd369e4f163df4aba_15586.jpg', 'd369e4f163df4aba_15587.jpg', 'd369e4f163df4aba_15589.jpg', 'd369e4f163df4aba_15591.jpg', 'd369e4f163df4aba_2099.jpg', 'd369e4f163df4aba_2100.jpg', 'd369e4f163df4aba_2101.jpg', 'd369e4f163df4aba_2102.jpg', 'd369e4f163df4aba_2103.jpg', 'd369e4f163df4aba_2105.jpg', 'd369e4f163df4aba_2106.jpg', 'd369e4f163df4aba_2107.jpg', 'd369e4f163df4aba_2108.jpg', 'd369e4f163df4aba_2109.jpg', 'd369e4f163df4aba_2110.jpg', 'd369e4f163df4aba_2112.jpg', 'd369e4f163df4aba_2113.jpg', 'd369e4f163df4aba_2114.jpg', 'd369e4f163df4aba_2115.jpg', 'd369e4f163df4aba_2116.jpg', 'd369e4f163df4aba_2117.jpg', 'd369e4f163df4aba_2119.jpg', 'd369e4f163df4aba_2120.jpg', 'd369e4f163df4aba_2121.jpg', 'd369e4f163df4aba_2122.jpg', 'd369e4f163df4aba_2127.jpg', 'd369e4f163df4aba_2128.jpg', 'd369e4f163df4aba_2129.jpg', 'd369e4f163df4aba_85978.jpg', 'd369e4f163df4aba_85979.jpg', 'd369e4f163df4aba_85980.jpg', 'd369e4f163df4aba_86011.jpg', 'd369e4f163df4aba_86012.jpg', 'd369e4f163df4aba_86013.jpg', 'd369e4f163df4aba_86015.jpg', 'd369e4f163df4aba_86025.jpg', 'd369e4f163df4aba_86053.jpg', 'd369e4f163df4aba_86064.jpg', 'd369e4f163df4aba_86065.jpg', 'd369e4f163df4aba_86102.jpg', 'd369e4f163df4aba_86103.jpg', 'd369e4f163df4aba_86113.jpg', 'd369e4f163df4aba_86114.jpg', 'd369e4f163df4aba_86115.jpg', 'd369e4f163df4aba_86116.jpg', 'd369e4f163df4aba_86117.jpg', 'd369e4f163df4aba_86129.jpg', 'd369e4f163df4aba_86130.jpg', 'd369e4f163df4aba_86131.jpg']

 Size: 357 

![Figure_1](https://github.com/user-attachments/assets/26ca6a8e-74e5-4ceb-adcd-914151360dc2)

**Note: You can use this code and adapt it to analyse any dataset whose coco annotation JSON file you have**

