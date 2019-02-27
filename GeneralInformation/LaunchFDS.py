import os
import subprocess


# Function to start a sub-process and execute FDS.
def run_job(file_path, message=False):
    """
    Provided with a path to a simulation input file, a sub-process
    is created and the simulation conducted.

    :param file_path: path to the simulation input file
        to be executed
    :param message: Suppress output
    """

    # Get the current working directory to switch between locations for
    # conducting simulations.
    cwd = os.getcwd()
    # print(os.path.split(file_path))

    # Split path and file name.
    # Path is needed to change directory.
    # File name is needed to launch the simulation, as well as looking for an
    #  *.end file to determine if the simulation has already been conducted,
    # assuming that the CHID and file name are the same.
    wd, fn = os.path.split(file_path)
    end_file = fn[:-3] + "end"

    # Change directory for the execution of the simulation.
    os.chdir(wd)

    # Check if an *.end file exists to prevent running already completed
    # simulations.
    if not os.path.isfile(end_file):
        if message is True:
            print("* Run simulation...")
            print("  Job: '{}'".format(fn))

        subprocess.call("set OMP_NUM_THREADS=1 & fds {}".format(fn),
                        shell=True)

        if message is True:
            print("  Simulation completed.")
    else:
        if message is True:
            print("* End-file '{}' detected - simulation skipped.".format(
                end_file))

    # Return to the original working directory.
    os.chdir(cwd)
