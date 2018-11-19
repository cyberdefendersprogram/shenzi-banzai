import sys
import argparse

def otx_options_handler():
    args = argparse.ArgumentParser()
    args.add_argument('-d', '--description',
                        const='description',
                        action='append_const',  
                        dest='optList',
                        default=[],
                        help='returns description of each pulse')
    args.add_argument('-t', '--tags',
                        const='tags',
                        action='append_const',
                        default=[],
                        dest='optList',
                        help='returns tags for each pulse')
    args.add_argument('-m', '--modified',
                        const='modified',
                        action='append_const',
                        dest='optList',
                        default=[],
                        help='return date modified for each pulse')
    args.add_argument('-i', '--id',
                        const='id',
                        action='append_const',
                        dest='optList',
                        default=[],
                        help='return pulse ids')
    args.add_argument('-au', '--author_name',
                        const='author_name',
                        action='append_const',
                        dest='optList',
                        default=[],
                        help='return author\'s name for each pulse') 
    args.add_argument('-ad', '--adversary',
                        const='adversary',
                        action='append_const',
                        dest='optList',
                        default=[],
                        help='return adversary title for pulses')
    args.add_argument('-ref', '--references',
                        const='references',
                        action='append_const',
                        dest='optList',
                        default=[],
                        help='return each pulses references')
    args.add_argument('-rev', '--revisions',
                        const='revisions',
                        action='append_const',
                        dest='optList',
                        default=[],
                        help='return pulse revisions')
    args.add_argument('search',
                        metavar='SEARCH QUERY',
                        type=str,
                        help='list search term',
                        default='crypto')
    options = args.parse_args()
    return options

def otx_pulse_print(options, pulses_json):
    '''
    Selects pulse information that is selected through options handler,
    and outputs JSON as 'selected_pulses'
    '''
    pulses = pulses_json["results"]
    selected_pulses = dict()
    for a_pulse in pulses:
        pulse_name = a_pulse.get('name')
        pulse_info = {category:info for category, info in a_pulse.items() if category in options}
        selected_pulses.update({pulse_name:pulse_info})
    return selected_pulses

'''
def export_pulses_to_csv(selected_pulses):
    csv_fieldnames = 
'''