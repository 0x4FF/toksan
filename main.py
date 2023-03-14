import argparse
import json

class toksan:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        
    def remove_keys(self, user_input, output_txt):
        with open(self.input_file, 'r') as f:
            data = json.load(f)
            
        # recursive function to remove keys from nested dictionaries and lists
        def remove_keys_recursive(obj):
            if isinstance(obj, dict):
                for key in list(obj.keys()):
                    if key == user_input:
                        del obj[key]
                    else:
                        remove_keys_recursive(obj[key])
            elif isinstance(obj, list):
                for i in range(len(obj)):
                    remove_keys_recursive(obj[i])
                    
        # remove the specified keys from the top-level dictionary
        remove_keys_recursive(data)
            
        with open(self.output_file, 'w') as f:
            json.dump(data, f, indent=4)
            
        if output_txt:
            with open(output_txt, 'w') as f:
                def write_keys_recursive(obj, prefix=''):
                    if isinstance(obj, dict):
                        for key in obj.keys():
                            if prefix:
                                full_key = prefix + '.' + key
                            else:
                                full_key = key
                            if isinstance(obj[key], (dict, list)):
                                write_keys_recursive(obj[key], full_key)
                            else:
                                f.write(full_key + '\n')
                    elif isinstance(obj, list):
                        for i in range(len(obj)):
                            if isinstance(obj[i], (dict, list)):
                                write_keys_recursive(obj[i], prefix + f'[{i}]')
                            else:
                                f.write(prefix + f'[{i}]' + '\n')
                write_keys_recursive(data)
                
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remove keys or nested dictionaries from a JSON file.')
    parser.add_argument('input', metavar='INPUT_FILE', help='input JSON file')
    parser.add_argument('output', metavar='OUTPUT_FILE', help='output JSON file')
    parser.add_argument('-t', '--text', metavar='TEXT_FILE', help='write remaining keys or values to a text file')
    parser.add_argument('-k', '--key-to-remove', metavar='KEY', required=True, help='key or value to remove from JSON')
    args = parser.parse_args()
    
    editor = toksan(args.input, args.output)
    editor.remove_keys(args.key_to_remove, args.text)
