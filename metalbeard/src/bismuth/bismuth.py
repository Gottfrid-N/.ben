import sys
import metalbeard.src.metalbeard as metalbeard

input_path = None
output_path = None

########
# MAIN #
########
def main():
    global input_path
    global output_path
    
    args = sys.argv
    
    try: input_path = args[1]
    except: input_path = "A:\\Projects\\.shhtml\\metalbear\\bismuth\\src\\put\\input.txt"
    try: output_path = args[2]
    except: output_path = "A:\\Projects\\.shhtml\\metalbear\\bismuth\\src\\put\\output.txt"
    
    print(input_path, output_path, test)

if __name__ == "__main__":
    main()