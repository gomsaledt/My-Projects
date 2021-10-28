# Program to append hidden information at the end of a JPEG file
def insert_info(filename, info):
    with open(filename, "ab") as f:
        f.write(bytes(info, "utf-8"))


# Program to scan hidden Info from the end of JPEG file
def extract_info(filename):
    with open("taj.jpeg", "rb") as f:
        content = f.read()
        # FFD9 - End of JPEG file
        offset = content.index(bytes.fromhex('FFD9'))   
        
        f.seek(offset+2)
        info = f.read().decode()
    return info


print(extract_info("taj.jpeg"))
