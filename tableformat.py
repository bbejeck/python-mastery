

def print_table(obj_list, attr_list):
    dashes = '-' * 8
    for name in attr_list:
        print(f'{name:>10}', end='')
    print('')
    for idx in range(0, len(attr_list)):
        print(f'{dashes:>10}', end='')
    print('')
    for obj in obj_list:
        for name in attr_list:
            print(f'{getattr(obj,name):>10}', end='')
        print('')
