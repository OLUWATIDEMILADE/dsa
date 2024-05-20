import os

class UniqueInt:
    @staticmethod
    def processFile(inputFilePath, outputFilePath):
        unique_integers = set()

        # Read and process the input file
        try:
            with open(inputFilePath, 'r') as inputFile:
                for line in inputFile:
                    line = line.strip()

                    if not line:
                        continue

                    parts = line.split()
                    if len(parts) != 1:
                        continue

                    try:
                        number = int(parts[0])
                        if -1023 <= number <= 1023:
                            unique_integers.add(number)
                    except ValueError:
                        continue
        except FileNotFoundError:
            print(f"Error: The file {inputFilePath} does not exist.")
            return
        except IOError as e:
            print(f"Error reading file {inputFilePath}: {e}")
            return

        # Write the sorted unique integers to the output file
        try:
            with open(outputFilePath, 'w') as outputFile:
                for number in sorted(unique_integers):
                    outputFile.write(f"{number}\n")
        except IOError as e:
            print(f"Error writing to file {outputFilePath}: {e}")

# Main execution
if __name__ == "__main__":
    input_folder = "dsa/hw01/sample_inputs/"
    output_folder = "dsa/hw01/sample_results/"

    # Ensure output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    input_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    for input_file in input_files:
        input_path = os.path.join(input_folder, input_file)
        output_path = os.path.join(output_folder, f"{input_file}_results.txt")
        UniqueInt.processFile(input_path, output_path)
