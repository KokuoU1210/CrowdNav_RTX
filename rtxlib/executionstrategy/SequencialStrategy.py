from pprint import pprint

from colorama import Fore

from rtxlib import info, error
from rtxlib.execution import experimentFunction


def start_sequential_strategy(wf):
    """ executes all experiments from the definition file """
    info("> ExecStrategy   | Sequential", Fore.CYAN)
    wf.totalExperiments = len(wf.execution_strategy["knobs"])
    info(f"Total experiments: {wf.totalExperiments}")
    for exp_num, kn in enumerate(wf.execution_strategy["knobs"]):
        info(f"Total experiments: {wf.totalExperiments}")
        info(f"Running experiment: {exp_num + 1}/{wf.totalExperiments}")
        print("Setting for current experiment:")
        pprint(kn)
        experimentFunction(wf, {
            "knobs": kn,
            "ignore_first_n_results": wf.execution_strategy["ignore_first_n_results"],
            "sample_size": wf.execution_strategy["sample_size"],
        })
