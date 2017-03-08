

def tim_giao(tap_hop_1,tap_hop_2):
    """
    Tra ve giao cua hai tap hop
    :param tap_hop_1: tap_hop
    :param tap_hop_2: tap_hop
    :return: tap_hop
    """
    return tap_hop_1.intersect(tap_hop_2)

def tim_hop(tap_hop_1,tap_hop_2):
    """
    Tra ve hop cua hai tap hop
    :param tap_hop_1: tap_hop
    :param tap_hop_2: tap_hop
    :return: tap_hop
    """
    return tap_hop_1.union(tap_hop_2)