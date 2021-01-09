from functions.getTotalPricefunction import getTotalPrice
from functions.getAdvancefunction import getAdvance
from functions.getWeightChargefunction import getWeightCharge
from functions.getDeliveryChargefunction import getDeliveryCharge
from functions.getContactNumberfunction import getContactNumber
from functions.getAddressfunction import getAddress
from functions.getProductsfunction import getProducts


def makeMessage(dataframe, name):
    sum = getTotalPrice(dataframe)
    adv = getAdvance(dataframe)
    wc = getWeightCharge(dataframe)
    deliveryCharge = getDeliveryCharge(dataframe, sum, adv)
    contactNumber = getContactNumber(dataframe)
    address = getAddress(dataframe)

    message = name + "\n"
    message = getProducts(dataframe, message)
    message += "\nTotal - " + str(sum) + " BDT\n"
    message += "Weight charge - " + str(wc) + " BDT\n"
    message += "Advanced - " + str(adv) + " BDT\n"
    message += "Due - " + \
        str(sum - adv + wc) + " BDT + Delivery Charge - " + \
        str(deliveryCharge) + " BDT\n"
    message += "\nDelivery Details:\n"
    message += "Contact Number: " + contactNumber + "\n"
    message += "Address: " + address + "\n"
    message += "\n"
    return message
