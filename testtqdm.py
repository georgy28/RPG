from tqdm import trange, tqdm
from colorama import Fore


for i in trange(int(45),
                bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.RED, Fore.BLUE)):
    pass

tqdm(8)
