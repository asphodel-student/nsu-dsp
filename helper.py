import matplotlib.pyplot as plt


def show_plots_helper(
        arguments: list[list],
        function_values: list[list[float]],
        functions_labels: list[str],
        window_title: str = 'Figure',
        x_label: str = 'x', y_label: str = 'y'):
    _union = zip(arguments, function_values, functions_labels)
    for x, y, label in _union:
        plt.plot(x, y, label=label)

    plt.title(window_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.tight_layout()
    plt.grid(True)
    plt.legend()
    plt.show()