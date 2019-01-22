class FabricCutter:
    def __init__(self, input_file):
        self.input = input_file


    def get_overlaps(self):
        with open(self.input) as fabric:
            overlap_counter = 0
            all_square_inch_coordinates = []
            for fabric_cut in fabric:
                print(fabric_cut)
                describer_array = fabric_cut.split(' ')
                describer_array[2] = describer_array[2].split(',')
                describer_array[2][1] = describer_array[2][1][:-1]
                describer_array[3] = describer_array[3].split('x')
                describer_array[3][1] = describer_array[3][1][:-1]
                print(describer_array)
                for col in range(int(describer_array[2][0]),
                                 int(describer_array[2][0] + describer_array[3][0])):
                    for row in range(int(describer_array[2][1]),
                                     int(describer_array[2][1]) + int(describer_array[3][1])):
                        sq_inch_coord = (col, row)
                        print(sq_inch_coord)
                        if sq_inch_coord in all_square_inch_coordinates:
                            overlap_counter += 1
                        all_square_inch_coordinates.append(sq_inch_coord)
        return overlap_counter


if __name__ == "__main__": 
    fabric_cutter = FabricCutter('003-no_matter_how_you_slice_it.txt')
    print(fabric_cutter.get_overlaps())