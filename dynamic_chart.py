import matplotlib.pyplot as plt
import random
def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))
def main():
    print("Hello Dynamic user, let's create a chart of your choice!")
    user_input = input("Enter the names of the objects separated by commas: ")
    inputx = [item.strip() for item in user_input.split(",")]
 
    user_value = input("Enter your values separated by commas: ")
    try:
        valuey = [float(v) for v in user_value.split(",")]
    except ValueError:
        print("Error: Please enter numeric values only.")
        exit()

    if len(inputx) != len(valuey):
        print("Error: Number of names and values must match.")
        exit()

    user_title = input("Enter the title of the chart: ")
    chart_type = input("Enter 'Bar', 'Piechart', 'Line', or 'Scatter': ")
    name_inputx = input("Enter label for X-axis: ")
    name_valuey = input("Enter label for Y-axis: ")

    plt.title(user_title)

    if chart_type.lower() == "bar":
        colors = [random_color() for _ in inputx]
        plt.bar(inputx, valuey, color=colors)
        plt.xlabel(name_inputx)
        plt.ylabel(name_valuey)

    elif chart_type.lower() == "piechart":
        colors = [random_color() for _ in valuey]
        plt.pie(valuey, labels=inputx, autopct='%1.1f%%', startangle=90, colors=colors)
        plt.axis('equal')
    elif chart_type.lower() == "line":
        colors = [random_color() for _ in valuey]
        line_color = random_color()
        for i, (x, y) in enumerate(zip(range(len(inputx)), valuey)):
            plt.plot(x, y, marker='o', linestyle='', color=colors[i])
        plt.plot(range(len(inputx)), valuey, linestyle='-', color=line_color)
        plt.xticks(range(len(inputx)), inputx)
        plt.xlabel(name_inputx)
        plt.ylabel(name_valuey)


    elif chart_type.lower() == "scatter":
        x_positions = range(len(inputx))
        colors = [random_color() for _ in valuey]
        plt.scatter(x_positions, valuey, color=colors)
        plt.xticks(x_positions, inputx)
        plt.xlabel(name_inputx)
        plt.ylabel(name_valuey)


    else:
        print("Invalid chart type entered.")
        exit()
    plt.tight_layout()
   
    save = input("Do you want to save this chart as an image? (yes/no): ").strip().lower()
    if save == "yes":
        filename = input("Enter filename (e.g. chart.png): ").strip()
        try:
            plt.savefig(filename)
            print(f"Chart saved as {filename}")
        except Exception as e:
            print(f"Failed to save chart: {e}")
    plt.show()
if __name__ == "__main__":
    main()