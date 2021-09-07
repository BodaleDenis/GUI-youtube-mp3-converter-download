import pytest
import sys
sys.path.append("./")
from src import DownloadList
from src import constexpr as const
from test_utils import *

dwn_list = DownloadList.DownloadList([])
dummy_list = [dummy_link_1, dummy_link_2, dummy_link_3]

def test_list_add():
    dwn_list.add_to_list(dummy_link_1)
    assert len(dwn_list.get_link_list()) == 1

def test_list_remove_element():
    dwn_list.set_link_list(dummy_list)
    dwn_list.remove_index(0)
    assert len(dwn_list.get_link_list()) == 2

def test_list_set_and_get():
    dwn_list.set_link_list([])
    assert dwn_list.get_link_list() == []
    dwn_list.set_link_list(dummy_list)
    assert dwn_list.get_link_list() == dummy_list

def test_list_empty_or_not():
    dwn_list.set_link_list([])
    assert dwn_list.is_list_empty() == True
    dwn_list.set_link_list(dummy_list)
    assert dwn_list.is_list_empty() == False
