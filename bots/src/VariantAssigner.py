from statistics import variance
from src.BotVariants import BotVariants
import random

def getVariants(num_bots: int) -> list:
    # return getRandomAssignment(num_bots)
    return getLogicalAssignment(num_bots)

def getRandomAssignment(num_bots: int) -> list[BotVariants]:
    variant_list = random.choices(list(BotVariants), weights=None, k=num_bots)
    return variant_list

def getLogicalAssignment(num_bots: int) -> list:
    # currently assign pro bot for all the bots
    variant_list = [BotVariants.PRO_BOT]*num_bots
    return variant_list