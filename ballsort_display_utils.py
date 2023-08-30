from IPython.display import display, Javascript

def open_bs_window():
    dist_obj = Javascript("""
        const bsWindow = window.open('http://localhost:8080/', 'bswindow', 'height=600, width=600');
        window.bswin = bsWindow.window;
        """);
    display(dist_obj)
