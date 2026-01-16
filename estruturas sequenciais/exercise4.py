file_size = float(input("What is the size of your file?"))
internet_velocity = float(input("How fast is your link of internet in mbps?"))
download_time_seconds = file_size * internet_velocity
download_time_minutes = math.ceil(download_time_seconds / 60)

print(f"O tempo de download será de {download_time_minutes} minutos")
