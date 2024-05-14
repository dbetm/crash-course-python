if __name__ == "__main__":
    
    with open("reduce_results/results.txt", "r") as file:
        results = file.readlines()

        for result in results:
            key, total = result.split(": ")

            char_bar = "+"*int(total)
            print(f"{key}: {char_bar}")