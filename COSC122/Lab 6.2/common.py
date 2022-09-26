from quicksort import *


def read_data(filename):
    """ Returns a list of integers read from the file """
    with open(filename) as infile:
        numbers = [int(line) for line in infile]
    return numbers


def common_items(list_x, list_y):
    """ Takes two sorted lists as input (ie, both lists are in ascending order).
    Returns a list containing all the items in list_x that are also in list_y.
    Returns an empty list if there are none.

    The resulting list should be in order and only contain one instance of each
    item that appears in both lists, ie, common items should only be listed once.
    NOTE: You should use a method similar to the merge function in mergesort,
    that is, use a while loop and a couple of indices. Don't use any for loops!

    First write code for dealing with two lists that each contain only uniques values.
    When you have that running, update it so that it deals with lists that don't
    contain all unique values, see the commented doctests below

    NOTES:
    Your function will need to use only one while loop.
    Your function shouldn't use expressions like:
       - item in alist
       - for item in alist

    >>> common_items([0,1,2,3],[1,2,3,4])
    [1, 2, 3]
    >>> common_items([0,1,2,3],[0,1,2,3])
    [0, 1, 2, 3]
    >>> common_items([0,1,2,3],[5,6,7,8])
    []
    >>> common_items([],[5,6,7,8])
    []
    >>> common_items([1,2,3,4],[])
    []
    >>> common_items([],[])
    []
    """
    # add the following doctests (and some of your own)
    # when ready for lists of non-unique items
    # >>> common_items([0,1,2,3],[0,0,2,4])
    # [0, 2]
    # >>> common_items([0,1,2,2,5,5,6,6,7],[0,0,2,4,5,5,5,7])
    # [0, 2, 5, 7]

    # ---start student section---
    list_x_values = []
    common_item_values = []
    index = 0 
    while index < len(list_x):  
        list_x_values.append(list_x[index])
        index += 1
    index = 0
    while index < len(list_y):    
        if list_y[index] in list_x_values and list_y[index] not in common_item_values:
            common_item_values.append(list_y[index])
        index += 1
    return common_item_values         
    # ===end student section===

list_x = read_data("./data/ordered_16.txt")
list_y = read_data("./data/ordered_17.txt")
monkey = [5510, 5515, 5526, 5533, 5535, 5539, 5541, 5544, 5549, 5551, 5552, 5553, 5554, 5555, 5556, 5559, 5561, 5563, 5571, 5576, 5579, 5589, 5591, 5595, 5597, 5599, 5600, 5601, 5604, 5606, 5607, 5610, 5611, 5614, 5616, 5618, 5620, 5622, 5623, 5625, 5626, 5629, 5630, 5631, 5632, 5636, 5644, 5656, 5663, 5668, 5669, 5671, 5674, 5675, 5676, 5681, 5682, 5691, 5692, 5695, 5696, 5697, 5698, 5704, 5706, 5707, 5708, 5716, 5717, 5719, 5721, 5725, 5728, 5730, 5731, 5733, 5734, 5737, 5738, 5739, 5740, 5746, 5747, 5748, 5749, 5750, 5752, 5757, 5763, 5766, 5768, 5771, 5772, 5779, 5781, 5782, 5785, 5787, 5788, 5794, 5797, 5800, 5803, 5812, 5815, 5822, 5825, 5826, 5827, 5830, 5831, 5833, 5837, 5841, 5843, 5845, 5850, 5853, 5857, 5863, 5864, 5865, 5872, 5876, 5880, 5881, 5885, 5887, 5890, 5891, 5900, 5903, 5905, 5907, 5918, 5924, 5927, 5928, 5929, 5931, 5932, 5943, 5945, 5946, 5949, 5954, 5955, 5957, 5960, 5966, 5969, 5971, 5979, 5985, 5991, 5992, 5993, 5998, 6003, 6006, 6009, 6011, 6013, 6014, 6016, 6019, 6025, 6027, 6032, 6033, 6034, 6036, 6037, 6047, 6051, 6053, 6054, 6056, 6057, 6063, 6068, 6069, 6075, 6078, 6079, 6081, 6082, 6088, 6093, 6095, 6096, 6098, 6099, 6100, 6103, 6104, 6107, 6114, 6119, 6120, 6122, 6123, 6124, 6129, 6137, 6144, 6154, 6158, 6160, 6162, 6164, 6166, 6169, 6175, 6177, 6187, 6189, 6192, 6195, 6196, 6197, 6198, 6204, 6208, 6209, 6211, 6213, 6215, 6225, 6227, 6229, 6230, 6235, 6244, 6247, 6250, 6251, 6254, 6260, 6261, 6262, 6263, 6265, 6269, 6273, 6274, 6276, 6280, 6291, 6293, 6298, 6299, 6300, 6304, 6308, 6310, 6313, 6315, 6317, 6318, 6320, 6328, 6332, 6335, 6342, 6344, 6347, 6348, 6352, 6353, 6355, 6361, 6362, 6364, 6376, 6380, 6383, 6388, 6392, 6393, 6397, 6399, 6402, 6404, 6407, 6411, 6420, 6423, 6426, 6427, 6431, 6440, 6443, 6446, 6451, 6453, 6458, 6460, 6463, 6465, 6466, 6469, 6472, 6473, 6474, 6477, 6478, 6479, 6483, 6484, 6490, 6497, 6498, 6501, 6503, 6505, 6514, 6516, 6523, 6525, 6526, 6528, 6529, 6531, 6537, 6539, 6542, 6543, 6546, 6548, 6551, 6552, 6556, 6566, 6578, 6591, 6594, 6604, 6607, 6608, 6609, 6612, 6614, 6617, 6624, 6631, 6633, 6640, 6651, 6652, 6654, 6656, 6659, 6661, 6669, 6673, 6674, 6675, 6677, 6688, 6691, 6693, 6694, 6698, 6707, 6708, 6713, 6714, 6717, 6721, 6722, 6724, 6728, 6746, 6748, 6755, 6766, 6770, 6775, 6776, 6784, 6786, 6789, 6793, 6794, 6802, 6804, 6813, 6815, 6824, 6826, 6828, 6834, 6838, 6842, 6848, 6849, 6851, 6853, 6858, 6859, 6865, 6867, 6870, 6880, 6885, 6888, 6889, 6894, 6898, 6901, 6902, 6909, 6910, 6912, 6924, 6927, 6932, 6936, 6937, 6945, 6946, 6951, 6955, 6968, 6972, 6978, 6981, 6982, 6983, 6986, 6987, 6988, 6989, 6995, 6997, 7000, 7001, 7003, 7004, 7007, 7012, 7013, 7015, 7024, 7027, 7033, 7057, 7069, 7075, 7076, 7079, 7086, 7089, 7090, 7095, 7099, 7105, 7106, 7116, 7117, 7122, 7131, 7137, 7147, 7150, 7152, 7154, 7157, 7158, 7162, 7165, 7170, 7175, 7176, 7180, 7182, 7185, 7189, 7193, 7195, 7196, 7200, 7204, 7209, 7210, 7211, 7217, 7219, 7224, 7226, 7228, 7229, 7234, 7239, 7241, 7255, 7260]
print(len(monkey))
print(common_items(list_x, list_y))
if __name__ == "__main__":
    doctest.testmod()
