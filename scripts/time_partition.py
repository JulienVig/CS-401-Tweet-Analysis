#!/usr/bin/env python
# coding: utf-8
from datetime import datetime, timedelta
from dateutil.relativedelta import *

def divide_month(first_day_dt, nb_of_partition, keyword):
    """
    @param nb_of_partition: number of parts
    """
    since_dt = first_day_dt #First day of the month
    until_dt = since_dt + relativedelta(months=+1) - timedelta(days=1) #Last day of the month 
    
    nb_days_in_month = (until_dt - since_dt).days + 1 #Nb of day in the month
    nb_days_in_partition = max(1, nb_days_in_month // nb_of_partition) #Length of partitions
    def dt_to_string(dt):
        """Convert datetime object to string"""
        return dt.strftime("%Y-%m-%d")
    
    start_dt = since_dt #Start date of partition
    end_dt = start_dt + timedelta(days=nb_days_in_partition - 1) #End date of partition (included)
    partition = []
    while end_dt <= until_dt:
        partition.append([keyword, dt_to_string(start_dt), dt_to_string(end_dt)])
        start_dt = end_dt + timedelta(days=1)
        end_dt = start_dt + timedelta(days=nb_days_in_partition - 1)
        
    
    #Extend last partition to the last day of month
    if partition[-1][2] != dt_to_string(until_dt): 
        partition[-1][2] = dt_to_string(until_dt)
    return partition

def create_keyword_partition(keyword, month_partition, start_dt=datetime(2012, 1, 1), end_dt=datetime(2014, 12, 31)):
    curr_dt = start_dt
    partition = []    
    while curr_dt < end_dt:
        partition += divide_month(curr_dt, month_partition, keyword)
        curr_dt += relativedelta(months=+1)
    return partition


