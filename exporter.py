import pandas as pd

def export_to_excel(cases, save_path):
    df = pd.DataFrame(cases)
    df.to_excel(save_path, index=False)