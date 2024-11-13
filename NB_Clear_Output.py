import nbformat
from IPython.display import clear_output

def clear_notebook(notebook_filename):
    """
    Clears all outputs in the specified Jupyter notebook file.

    Parameters:
    -----------
    notebook_filename : str
        The path to the Jupyter notebook file (e.g., "my_notebook.ipynb").
    
    Usage:
    ------
    1. Import and call this function from a Jupyter notebook:
       from clear_notebook import clear_notebook
       clear_notebook("your_notebook.ipynb")
    
    2. Or run it directly from the command line:
       python clear_notebook.py your_notebook.ipynb
    
    This will clear all cell outputs and reset execution counts for the entire notebook.
    """
    # Load the notebook
    with open(notebook_filename, "r") as f:
        nb = nbformat.read(f, as_version=4)

    # Clear output from all cells
    for cell in nb.cells:
        if "outputs" in cell:
            cell["outputs"] = []
        if "execution_count" in cell:
            cell["execution_count"] = None

    # Save the notebook with cleared outputs
    with open(notebook_filename, "w") as f:
        nbformat.write(nb, f)

    clear_output()
    print(f"All outputs have been cleared from {notebook_filename}.")

# Optional: Uncomment the following lines to make the script runnable from the command line
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python clear_notebook.py <notebook_filename>")
    else:
        notebook_filename = sys.argv[1]
        clear_notebook(notebook_filename)
