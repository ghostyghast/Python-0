def ft_tqdm(nums) -> None:
    """ft_tqdm(range) --> None
    function that takes a range and prints a progress bar
    based on how far it is in the iteration of the range"""
    length = len(nums)
    for x in nums:
        percent = (x / length) * 100
        bar = '█' * int(percent) + ' ' * (100 - int(percent))
        print(f"\r {percent:.0F}%|{bar}| {x}/{length}", end='\r')
        yield x
    bar = '█' * 100
    print(f"\r100%|{bar}| {length}/{length}")
