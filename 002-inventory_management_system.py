class Inventory:
    def __init__(self, input_file):
        self.input = input_file
        self.inventory_listing = []
        self.twos_count, self.threes_count = self.compute_twos_and_threes_count()


    def compute_twos_and_threes_count(self):
        with open(self.input) as inventory_listing:
            twos_count = threes_count = 0
            for box_code in inventory_listing:
                self.inventory_listing.append(box_code)
                two_count_found = three_count_found = False
                for letter in box_code:
                    if (box_code.count(letter) == 2 and not two_count_found):
                        twos_count += 1
                        two_count_found = True
                    elif (box_code.count(letter) == 3 and not three_count_found):
                        threes_count += 1
                        three_count_found = True
        return (twos_count, threes_count)


    def get_special_boxes_common_codes(self):
        # import pdb; pdb.set_trace()
        self.inventory_listing.sort()
        for index, box_code in enumerate(self.inventory_listing):
            if index == 0:
                continue
            diff_found = False
            diff_limit_exceeded = False
            diff_index = -1
            for index_, xter in enumerate(box_code):
                if (xter != self.inventory_listing[index-1][index_]):
                    if not diff_found:
                        diff_found = True
                        diff_index = index_
                    else:
                        diff_limit_exceeded = True
                        break
            if diff_found and not diff_limit_exceeded:
                return "{}{}".format(box_code[:diff_index], box_code[diff_index+1:])
        return "nothing found here..."




    def get_checksum(self):
        return self.twos_count * self.threes_count


if __name__ == "__main__":
    inventory = Inventory('002-inventory_management_system.txt')
    print(inventory.get_checksum())
    print(inventory.get_special_boxes_common_codes())