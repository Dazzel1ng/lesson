def create_record (name,telephone,address):
    """"Create  Record"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record

user1 = create_record("Slavod","+306464671", "Tinussiya")
user2 = create_record("Erevan","+435124312", "Munisiya")

print(user1)
print(user2)

def give_award(medal, *persons):
    """Give Medals to persons"""
    for persons in persons:
        print("Tovarish " + persons.title() + "nagrajdaetsya medaliyu" + medal)


give_award("Za Makeevky","Za Berlin","Za Otsos")

