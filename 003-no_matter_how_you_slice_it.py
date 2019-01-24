class FabricCutter:
    def __init__(self, input_file):
        self.input = input_file


    def get_overlaps(self):
        with open(self.input) as fabric:
            overlap_counter = 0
            all_square_inch_coordinates = {}
            for fabric_cut in fabric:
                print(fabric_cut)
                describer_array = fabric_cut.split(' ')
                describer_array[2] = describer_array[2].split(',')
                describer_array[2][1] = describer_array[2][1][:-1]
                describer_array[3] = describer_array[3].split('x')
                describer_array[3][1] = describer_array[3][1][:-1]
                print(describer_array)
                first_x, first_y = int(describer_array[2][0]) + 1, int(describer_array[2][1]) + 1
                width = int(describer_array[3][0])
                height = int(describer_array[3][1])

                for col in range(int(describer_array[2][0]) + 1,
                                 int(describer_array[2][0]) + 1 + int(describer_array[3][0])):
                    for row in range(int(describer_array[2][1]) + 1,
                                     int(describer_array[2][1]) + 1 + int(describer_array[3][1])):
                        # import pdb; pdb.set_trace()
                        sq_inch_coord = (col, row)
                        print('{}{}'.format(describer_array[0], sq_inch_coord))
                        try:
                            all_square_inch_coordinates[str(sq_inch_coord)] += 1
                        except KeyError:
                            all_square_inch_coordinates[str(sq_inch_coord)] = 1


            for coord, count in all_square_inch_coordinates.items():
                print('{}-->{}'.format(coord, count))
                if count > 1:
                    overlap_counter += 1
                        
        return overlap_counter


if __name__ == "__main__": 
    fabric_cutter = FabricCutter('003-no_matter_how_you_slice_it.txt')
    print(fabric_cutter.get_overlaps())