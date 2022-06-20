Each cable modem ( CM ) is capable to work on specific downstream frequency represented by channel id or group of such frequencies ( group of channels ) .

Given CM is currently registered on a group of channels [ 2,3,4,5 ] . 

Due to a noise at channel N3 it is required to move CM to another group of channels , which does not include the impaired channel N3 . 

New group of channels must has the same length or less . If multiple suitable groups found , bigger group is preferable .

If no suitable group found CM should be moved to the next bigger single channel ID found among all groups . 


1. Having the following list of available groups of channels :

       [1,2,3,4]

       [2,3,5,4]

       [4,5,6]

       [8,6,7,5]
     
       [6,10,8,9,7]

Expected result: [8,6,7,5]

2 Having the following list of available groups of channels:

     [3,4,5,6]

     [6,7,8,9,10]

     [4,3,5]

Expected result: [4] - as the next first channel ID not matching the impaired one

