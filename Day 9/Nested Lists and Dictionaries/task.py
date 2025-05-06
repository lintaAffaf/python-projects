#dictionary
travel_log={
    "lahore":["johar","dha","venus"],
    "islamabad":["monal","comsats"],
}

print(travel_log["lahore"][1])
#nested dictionary
travel_log={
    "lahore":["johar","dha","venus",["thokar","wapda"]],
    "islamabad":["monal","comsats"],
}
print(travel_log["lahore"][3][1])

#dictionary in a dictionary
travel_log={
    "lahore":["johar","dha","venus"],
    "islamabad":{
    "islamabad":["monal","comsats"]},
}
print(travel_log["islamabad"]["islamabad"][1])


