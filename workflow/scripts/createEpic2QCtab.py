import pandas as pd
import os

dict_allsamp = {}
# for each sample, we read the log file and extract the number of called peaks
for f in snakemake.input["logFile"]:
    idName = os.path.basename(f).split(".")[0]
    with open(f, "r") as file:
        calledPeaks = file.read().strip().split(":")[1].strip()
        dict_allsamp[idName] = [calledPeaks]

df_info = pd.DataFrame.from_dict(dict_allsamp, orient="index")
if df_info.empty:
    df_info = pd.DataFrame(columns=["Called Peaks"])
else:
    df_info.columns = ["Called Peaks"]

df_info.to_csv(snakemake.output["tab"], sep="\t", index_label="Sample")