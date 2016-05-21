import os, sys, pdb, re

class AAPDonationStats(object):

    def __init__ (self):
        input_file_obj = open ('input_file_2.txt', 'r')
        input_file_buffer = input_file_obj.read ()
        self.input_contents_by_line_list = input_file_buffer.split('\n')

    def get_state_with_num_of_donations (self):
        state_dict = {}

        for line in self.input_contents_by_line_list:
            field_value_list = line.split('\t')

            if len(field_value_list) ==1:
                # This this is the last line
                break

            state_name = field_value_list[2].upper()
            try:
                state_dict [state_name] = state_dict [state_name] +1
            except KeyError:
                state_dict [state_name] = 1

        sorted_state_list = sorted (state_dict.items(), key= lambda x: x[1], reverse=True)

        return sorted_state_list

    def get_n_persons_with_top_donations (self, top_n):
        person_name_dict={}

        for line in self.input_contents_by_line_list:
            field_value_list = line.split('\t')

            if len(field_value_list) ==1:
                # This this is the last line
                break

            person_name = field_value_list[0].upper()
            state_name = field_value_list[2].upper()
            person_name_dict [(person_name, state_name)] = int(field_value_list[4])

        sorted_person_name_list = sorted (person_name_dict.items(), key= lambda x: x[1], reverse=True)


        return sorted_person_name_list [:top_n]

    def get_persons_with_repeated_donations (self):
        person_name_dict={}

        for line in self.input_contents_by_line_list:
            field_value_list = line.split('\t')

            if len(field_value_list) ==1:
                # This this is the last line
                break

            person_name = field_value_list[0].upper()
            state_name = field_value_list[2].upper()

            try:
                person_name_dict [(person_name, state_name)] = person_name_dict [(person_name, state_name)] +1
            except KeyError:
                person_name_dict [(person_name, state_name)] = 1

        sorted_person_name_list = sorted (person_name_dict.items(), key= lambda x: x[1], reverse=True)
        repeated_donation_list = [(person_tuple, num_of_donations) for (person_tuple, num_of_donations) in sorted_person_name_list if num_of_donations > 1]


        return repeated_donation_list

    def get_favourite_time_of_donations (self):
        fav_time_dict={}
        time_hr_regex = re.compile (r'.*\s([0-9]*)\:[0-9]*([a-zA-Z]*)$', re.I)

        for line in self.input_contents_by_line_list:
            field_value_list = line.split('\t')

            if len(field_value_list) ==1:
                # This this is the last line
                break

            date_time = field_value_list[5]
            match = time_hr_regex.match (date_time)
            time = "%s %s" % (match.group(1), match.group(2))

            try:
                fav_time_dict [time] = fav_time_dict [time] +1
            except KeyError:
                fav_time_dict [time] = 1


        favourite_time_of_donation_list = sorted (fav_time_dict.items(), key= lambda x: x[1], reverse=True)
        favourite_time_of_donation_list = [(time, "%s" % (math.ceil(count*100/total_entries))) for (time, count) in favourite_time_of_donation_list]
        
        return favourite_time_of_donation_list


if __name__ == "__main__":
    stats = AAPDonationStats()

    print "get_state_with_num_of_donations\n %s\n\n" % (str(stats.get_state_with_num_of_donations ()))
    print "get_n_persons_with_top_donations\n %s\n\n" % (str(stats.get_n_persons_with_top_donations (5)))
    print "get_persons_with_repeated_donations\n %s" % stats.get_persons_with_repeated_donations ()
    print "get_favourite_time_of_donations\n %s" % stats.get_favourite_time_of_donations ()

    '''
    print " %s" % stats.
    print " %s" % stats.
    print " %s" % stats.
    print " %s" % stats.
    print " %s" % stats.
    print " %s" % stats.
    '''
    sys.exit(0)
