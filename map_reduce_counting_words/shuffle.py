import os


HOSTS = os.getenv("HOSTS", "").split(",")



for host in HOSTS:
    filenames = os.listdir(f"{host}/map_results")

    for filename in filenames:
        key = filename.split(".")[0]

        if key == "":
            continue

        with open(f"{host}/map_results/{filename}", "r") as file:
            content = file.read()

        with open(f"map_results/{key}.txt", "a") as file:
            file.write(content)