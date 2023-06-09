def sec_conversion(total_seconds):
    seconds = total_seconds  % 60
    min = (total_seconds - seconds) % 3600
    hour = (total_seconds - seconds - min)
    sec = seconds
    min = min // 60
    hour = hour // 3600
    if hour == 0 and min == 0:
        return f"{sec}s"
    elif hour == 0 and sec == 0:
        return f"{min}m"
    elif min == 0 and sec == 0:
        return f"{hour}hr"
    elif hour == 0:
        return f"{min}m {sec}s"
    elif min == 0:
        return f"{hour}h {sec}s"
    elif sec == 0:
        return f"{hour}h {min}m"
    elif hour == 0 and min == 0 and sec == 0:
        return f"0s"
    else:
        return f"{hour}:{min}:{sec}"



def main():
    seconds_input = int(input("Enter the number of seconds you wish to convert: "))
    print("=" * 100)
    print(sec_conversion(seconds_input))
    print("=" * 100)


if __name__ == "__main__":
    main()
