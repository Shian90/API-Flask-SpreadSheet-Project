def getDeliveryCharge(dataframe, sum, adv):
    deliveryCharge = 0
    for i in dataframe.index:
        if(dataframe.loc[i, "Area"][0:5] == "Dhaka" or dataframe.loc[i, "Area"] == "Inside Dhaka"):
            deliveryCharge = 100
            break
        else:
            if((sum-adv) > 0):
                deliveryCharge = 160
            else:
                deliveryCharge = 130
            break
    return int(deliveryCharge)
